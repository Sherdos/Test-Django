# Generated by Django 4.2 on 2023-04-15 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='image',
            field=models.ImageField(default=1, upload_to='question/image/', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
