# Generated by Django 3.2.8 on 2021-11-09 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(blank=True, max_length=64, null=True)),
                ('link', models.CharField(max_length=64)),
                ('fiyat', models.IntegerField()),
                ('fiyat_birimi', models.CharField(choices=[('Dollar', 'Dollar'), ('TL', 'TL'), ('Euro', 'Euro')], max_length=8)),
                ('image', models.ImageField(upload_to='urun/')),
                ('aciklama', models.TextField()),
                ('olus_tarih', models.DateTimeField(auto_now_add=True)),
                ('guncelleme_tarih', models.DateTimeField(auto_now=True)),
                ('ust_kategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='category.urun')),
            ],
        ),
    ]