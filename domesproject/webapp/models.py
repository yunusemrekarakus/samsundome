from django.db import models

# Create your models here.
class Hizmet(models.Model):
    baslik = models.CharField(max_length=200)  # Başlık için kısa metin alanı
    metin = models.TextField()  # Hizmet açıklaması için uzun metin alanı
    resim = models.ImageField(upload_to='hizmet_resimleri/')  # Resim yüklemek için alan

    def __str__(self):
        return self.baslik
    
    class Meta:
        verbose_name = "Hizmet"
        verbose_name_plural = "Hizmetler"  # Admin panelinde "Hizmets" yerine "Hizmetler" görünür




class OtelMemnuniyet(models.Model):
    MUKEMMEL = 5
    COK_IYI = 4
    IYI = 3
    ORTA = 2
    KOTU = 1

    YILDIZ_SECENEKLERI = [
        (MUKEMMEL, '5 - Mükemmel'),
        (COK_IYI, '4 - Çok İyi'),
        (IYI, '3 - İyi'),
        (ORTA, '2 - Orta'),
        (KOTU, '1 - Kötü'),
    ]

    musteri_adi = models.CharField(max_length=200)  # Müşterinin adı
    yorum = models.TextField(blank=True, null=True)  # Müşteri yorumu
    yildiz = models.IntegerField(choices=YILDIZ_SECENEKLERI)  # 1-5 arasında yıldız değerlendirmesi
    resim = models.ImageField(upload_to='memnuniyet_resimleri/', blank=True, null=True)  # Müşteri resmi
    video = models.FileField(upload_to='memnuniyet_videolari/', blank=True, null=True)  # Müşteri videosu
    ip_adresi = models.GenericIPAddressField(null=True, blank=True)  # Müşterinin IP adresi
    konum = models.CharField(max_length=255, null=True, blank=True)  # Müşterinin konum bilgisi
    cihaz_bilgisi = models.CharField(max_length=255, null=True, blank=True)  # Müşterinin cihaz bilgisi
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)  # Yorum tarihi
    yayınla = models.BooleanField(default=False)  # Yorum onaylanmadıkça False olacak

    def __str__(self):
        return f"{self.musteri_adi} - {self.yildiz} Yıldız"

    class Meta:
        verbose_name = "Otel Memnuniyeti"
        verbose_name_plural = "Otel Memnuniyetleri"



class İzleyizi(models.Model):
    ip_address = models.GenericIPAddressField()
    visit_time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    device_info = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Web Site Trafiği"
        verbose_name_plural = "Web Site Trafiği"

    def __str__(self):
        return f"Ziyaretçi İp Adresi :{self.ip_address} ------------------------------------------------------------------------------------------- Ziyaret Tarihi ve Saati {self.visit_time}"
    


class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    description = models.TextField(verbose_name="Açıklama", blank=True, null=True)
    image = models.ImageField(upload_to="gallery/", verbose_name="Fotoğraf")
    alt_text = models.CharField(
        max_length=200, 
        verbose_name="Alt Metin", 
        help_text="Görselin SEO için açıklaması"
    )
    slug = models.SlugField(
        max_length=200, 
        unique=True, 
        verbose_name="URL Yapısı",
        help_text="SEO için başlığa uygun bir kısa URL yapısı"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")
    
    class Meta:
        verbose_name = "Galeri"
        verbose_name_plural = "Galeri"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    

class VideoGallery(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    description = models.TextField(verbose_name="Açıklama", blank=True, null=True)
    video_file = models.FileField(upload_to="videos/", verbose_name="Video Dosyası")
    start_time = models.IntegerField(verbose_name="Başlangıç Süresi (saniye)", default=0)
    end_time = models.IntegerField(verbose_name="Bitiş Süresi (saniye)", default=10)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")
    
    class Meta:
        verbose_name = "Video Galeri"
        verbose_name_plural = "Video Galeri"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    

class Ekip(models.Model):
    isim = models.CharField(max_length=100)  # Ekip üyesinin ismi
    resim = models.ImageField(upload_to='team_images/')  # Ekip üyesinin fotoğrafı
    vasif = models.CharField(max_length=100)  # Ekip üyesinin vasfı (pozisyonu)
    instagram_url = models.URLField(max_length=200, blank=True, null=True)  # Instagram profili için URL

    class Meta:
        verbose_name = "Ekip"
        verbose_name_plural = "Ekip"
    def __str__(self):
        return self.isim
    

class Content(models.Model):
    baslik1 = models.CharField(max_length=200, verbose_name="Başlık 1")
    baslik2 = models.CharField(max_length=200, verbose_name="Başlık 2", blank=True, null=True)
    icerik = models.TextField(verbose_name="İçerik")
    button_text = models.CharField(max_length=100, verbose_name="Buton Metni", blank=True, null=True)
    button_link = models.URLField(verbose_name="Yönlendirme Linki", blank=True, null=True)
    resim = models.ImageField(upload_to='images/', verbose_name="Resim", blank=True, null=True)
    
    class Meta:
        verbose_name = "Carousel"
        verbose_name_plural = "Carousel"


    def __str__(self):
        return self.baslik1
    
class Association(models.Model):
    name = models.CharField(max_length=255, verbose_name="Dernek Adı")
    member_number = models.CharField(max_length=50, verbose_name="Dernek Üye Numarası")
    logo = models.ImageField(upload_to='association_logos/', verbose_name="Dernek Logosu")

    class Meta:
        verbose_name = "Dernek"
        verbose_name_plural = "Dernek"
    def __str__(self):
        return self.name
    



class Hakkimizda(models.Model):
    baslik = models.CharField(max_length=255)
    icerik = models.TextField()
    resim = models.ImageField(upload_to='hakkimizda_resim/')
    musteri_say = models.CharField(max_length=10)

    def __str__(self):
        return self.baslik
