# Generated by Django 2.2.3 on 2019-12-30 18:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Kayit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kayitmodel',
            name='kayit_eden',
            field=models.ForeignKey(default=1, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='kayitmodel',
            name='adi',
            field=models.CharField(max_length=200, verbose_name='Adı'),
        ),
    ]