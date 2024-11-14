from django.contrib import admin
# Register your models here.
from .models import Hizmet,OtelMemnuniyet, İzleyizi, Gallery,VideoGallery,Ekip, Content,Association, Hakkimizda

admin.site.register(Hizmet)



class OtelMemnuniyetAdmin(admin.ModelAdmin):
    list_display = ('musteri_adi', 'yildiz', 'yayınla', 'olusturulma_tarihi')
    list_filter = ('yayınla', 'yildiz')
    search_fields = ('musteri_adi', 'yorum')
    readonly_fields = ('ip_adresi', 'konum', 'cihaz_bilgisi')
    actions = ['yorumlari_onayla']
    

    def yorumlari_onayla(self, request, queryset):
        queryset.update(onayli=True)
    yorumlari_onayla.short_description = "Seçilen yorumları onayla"

admin.site.register(OtelMemnuniyet, OtelMemnuniyetAdmin)

class İzyeliciAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'visit_time','location', 'device_info')
    list_display = ["visit_time", "ip_address"]
    def has_add_permission(self, request):
        # Yeni kayıt ekleme izinleri devre dışı bırakılıyor
        return False

    def has_change_permission(self, request, obj=None):
        # Var olan kayıtları değiştirme izinleri devre dışı bırakılıyor
        return False
    def has_delete_permission(self, request, obj=None):
        # Var olan kayıtları değiştirme izinleri devre dışı bırakılıyor
        return False
admin.site.register(İzleyizi, İzyeliciAdmin)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")



@admin.register(Ekip)
class EkipAdmin(admin.ModelAdmin):
    list_display = ('isim', 'vasif', 'instagram_url', 'resim')
    search_fields = ('isim', 'vasif')

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('baslik1', 'baslik2', 'button_text', 'button_link', 'resim')
    search_fields = ('baslik1', 'baslik2', 'icerik')

admin.site.register(Association)

admin.site.register(Hakkimizda)