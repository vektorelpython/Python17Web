from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class KayitModel(models.Model):
    kayit_eden = models.ForeignKey('auth.user',on_delete="CASCADE",default=1)
    adi = models.CharField(max_length=200,verbose_name="Adı")
    soyadi = models.CharField(max_length=200)
    cinsiyetCh = [("1","Erkek"),("2","Kız")]
    cinsiyet = models.CharField(max_length=10,choices=cinsiyetCh)
    eposta = models.EmailField()
    tcKimlikNo = models.BigIntegerField()
    kayit_zaman = models.DateTimeField(default=timezone.now)
    zaman = models.DateTimeField(null=True,blank=True)


    def __str__(self):
        return str(self.tcKimlikNo)


    class Meta:
        db_table = 'kayitlar'