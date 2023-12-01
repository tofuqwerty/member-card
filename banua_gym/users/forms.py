from django.forms import ModelForm
from .models import QRCode

class MemberForm(ModelForm):
    class Meta:
        model = QRCode
        fields = '__all__'