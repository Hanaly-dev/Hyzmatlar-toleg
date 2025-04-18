# Generated by Django 5.2 on 2025-04-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tolegler', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hyzmat',
            options={'verbose_name_plural': 'Hyzmatlar'},
        ),
        migrations.AlterModelOptions(
            name='profil',
            options={'verbose_name_plural': 'Profiller'},
        ),
        migrations.AlterModelOptions(
            name='toleg',
            options={'verbose_name_plural': 'Tölegler'},
        ),
        migrations.AddField(
            model_name='hyzmat',
            name='hyzmat_barada',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hyzmat',
            name='suraty',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]
