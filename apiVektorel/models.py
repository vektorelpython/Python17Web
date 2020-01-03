from django.db import models

class Music(models.Model):
    isim = models.CharField(max_length=200)

    class Meta:
        db_table = 'muzikler'
