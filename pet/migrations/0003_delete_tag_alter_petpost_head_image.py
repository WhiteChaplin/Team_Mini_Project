# Generated by Django 4.1.4 on 2022-12-21 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_remove_petpost_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AlterField(
            model_name='petpost',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='pet/images/%Y/%m/%d/'),
        ),
    ]