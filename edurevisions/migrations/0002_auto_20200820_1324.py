# Generated by Django 3.1 on 2020-08-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edurevisions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='secondary_revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.FloatField()),
                ('subject', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.RenameModel(
            old_name='revision',
            new_name='primary_revision',
        ),
    ]
