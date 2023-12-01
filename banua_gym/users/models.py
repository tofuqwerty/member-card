from django.db import models
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from PIL import Image
import base64


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed
    
 
# # Create your models here.
# class Member(models.Model):
#     Nama = models.CharField(db_column='nama', max_length=100, blank=False)
#     Alamat = models.TextField(db_column='alamat', max_length=1000, blank=False)
#     Nohp = models.CharField(db_column='nohp', max_length=100, blank=False)
#     Join_Member = models.CharField(db_column='join_member',max_length=100, blank=False)
#     Habis_Member = models.CharField(db_column='habis_member',max_length=100, blank=False)
    
class QRCode(models.Model):
   
    nama = models.CharField(db_column='nama', max_length=100, blank=False)
    alamat = models.TextField(db_column='alamat', max_length=1000, blank=False)
    nohp = models.CharField(db_column='nohp', max_length=100, blank=False)
    join_member = models.CharField(db_column='join_member',max_length=100, blank=False)
    habis_member = models.CharField(db_column='habis_member',max_length=100, blank=False)
    foto = models.ImageField(upload_to='images/',  blank=True, null=True)
    qr_image = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def __str__(self):
        return self.nama

    # save method
    def save_qr_code(self):
        # Generate QR code and save it to the model
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data("http://127.0.0.1:8000" + self.get_absolute_url())
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        
        
        
        # Convert the PIL Image to a BytesIO object
        buffer = BytesIO()
        img.save(buffer, format="PNG")

        # Create a unique filename for the QR code
        filename = f'qrcode_{self.nama}.png'

        # Create a Django ContentFile and InMemoryUploadedFile
        file = ContentFile(buffer.getvalue())
        self.qr_image.save(filename, InMemoryUploadedFile(file, None, filename, 'image/png', len(buffer.getvalue()), None))
        


    def get_absolute_url(self):
        # Replace this with the actual URL or path you want the QR code to point to
        nama=base64.b64encode(self.nama.encode('utf-8')).decode('utf-8')
        return f'/profile/{nama}/'
    


