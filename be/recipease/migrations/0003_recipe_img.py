# Generated by Django 2.2.4 on 2019-08-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipease', '0002_auto_20190814_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='img',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
