# Generated by Django 3.1.1 on 2020-10-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edurevisions', '0008_compositionclass4_videofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compositionclass4',
            name='videofile',
        ),
        migrations.AlterField(
            model_name='compositionclass4',
            name='image_url',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]
