from django.contrib import admin
from .models import Profile
from .models import QRCode
from django.utils.html import format_html

# Register your models here.
# admin.site.register(Profile)

@admin.register(QRCode)
class QRCodeDataAdmin(admin.ModelAdmin):
    list_display = ('nama', 'alamat', 'nohp', 'join_member', 'habis_member','display_foto', 'display_qr_image')
    
    def display_foto(self, obj):
        print("cek ",obj.foto.url)
        return format_html('<img src="{}" style="max-width:260px; max-height:200px"/>'.format(obj.foto.url))
     
    display_foto.allow_tags = True
    display_foto.short_description = 'Foto'
    
    def display_qr_image(self, obj):
        # This function returns HTML with the QR code image
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.qr_image.url))
        # return f'<img src="{obj.qr_image.url}" width="50" height="50" />'

    display_qr_image.allow_tags = True
    display_qr_image.short_description = 'QR Code'
    
    

    def save_model(self, request, obj, form, change):
        # Override the save_model method to generate and save the QR code
        obj.save_qr_code()
        super().save_model(request, obj, form, change)
