from django.shortcuts import render, redirect
from .forms import OtelMemnuniyetForm, OtelMemnuniyet
from .models import İzleyizi, Gallery,VideoGallery, Hizmet,Ekip, Content, Association, Hakkimizda,OtelMemnuniyet

import requests

from django.utils import timezone

def home(request):
    yorumlar = OtelMemnuniyet.objects.filter(yayınla=True)
    galeri = Gallery.objects.all()
    video = VideoGallery.objects.all()
    carousel = Content.objects.all()
    
    return render(request, 'index.html', {'yorumlar': yorumlar, 'galeri': galeri, 'videolar' : video, 'carousel': carousel})

def association_info(request):
    # Dernek bilgilerini alıyoruz, yalnızca ilk kayıt alınır
    association = Association.objects.first() 
    return {
        'association': association
    }
    
def about(request):
    ekipler = Ekip.objects.all()
    hakkimda = Hakkimizda.objects.all()
    return render (request,'about.html', {'ekip': ekipler, 'abt': hakkimda})

def contact(request):
    return render (request,'contact.html')


# def project(request):
#     return render (request, 'project.html')

def tesekkurler(request):
    return render (request, "succesfull.html")

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # İlk IP'yi al
    else:
        ip = request.META.get('REMOTE_ADDR')  # Eğer yoksa doğrudan al
    return ip

def get_location(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    if response.status_code == 200:
        return response.json()  # JSON olarak konum bilgisi döner
    return None

def otel_memnuniyet_view(request):
    if request.method == "POST":
        form = OtelMemnuniyetForm(request.POST, request.FILES)
        if form.is_valid():
            # IP ve diğer bilgileri al
            ip = get_client_ip(request)
            location = get_location(ip)
            user_agent = request.META.get('HTTP_USER_AGENT', 'Bilinmiyor')  # Cihaz bilgisi

            # Formu veritabanına kaydetmeden önce diğer bilgileri ekle
            memnuniyet = form.save(commit=False)
            memnuniyet.ip_adresi = ip  # IP adresini kaydet
            memnuniyet.konum = location.get('city', 'Bilinmiyor')  # Konumu kaydet
            memnuniyet.cihaz_bilgisi = user_agent  # Cihaz bilgilerini kaydet

            # Formu veritabanına kaydet
            memnuniyet.save()  # Eksik olan kaydetme işlemi

            # Formu temizle ve başarı sayfasına yönlendir
            form = OtelMemnuniyetForm()  # Formu temizlemek için yeniden oluştur
            return redirect('succesfull')
        else:
            # Form geçersizse, form ile beraber hata mesajı gönder
            return render(request, 'otel_satisfaction.html', {'form': form, 'error': "Hatalı girdiniz!"})
    else:
        # GET isteği ise boş formu döndür
        form = OtelMemnuniyetForm()
    
    return render(request, 'otel_satisfaction.html', {'form': form})


def onaylanmis_yorumlar_view(request):
    yorumlar = OtelMemnuniyet.objects.filter(yayınla=True)
    services = Hizmet.objects.all()
    return render(request, 'service.html', {'yorumlar': yorumlar, 'service': services})

