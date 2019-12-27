from django.forms import ModelForm
from .models import KayitModel

class KayitForm(ModelForm):

     class Meta:
        model = KayitModel
        
        fields = ('adi', 'soyadi','cinsiyet','tcKimlikNo','eposta')
        labels = {"adi":"Adı",
        "soyadi":"Soyadı",
        "cinsiyet":"Cinsiyet",
        "tcKimlikNo":"TC Kimlik No",
        "eposta":"E Mail"}