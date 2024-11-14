# myapp/forms.py
from django import forms
from .models import OtelMemnuniyet
from captcha.fields import CaptchaField

class OtelMemnuniyetForm(forms.ModelForm):

    captcha = CaptchaField()
    class Meta:
        model = OtelMemnuniyet
        fields = ['musteri_adi', 'yorum', 'yildiz', 'resim', 'video']  # Resim ve video alanları eklendi
        widgets = {
            'musteri_adi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınızı girin', 'required': 'required'}),
            'yorum': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Yorumunuzu buraya yazın...', 'style': 'height: 100px', 'required': 'required'}),
            'yildiz': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'resim': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

