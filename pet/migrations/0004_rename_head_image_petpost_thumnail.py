# Generated by Django 4.1.4 on 2022-12-22 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0003_delete_tag_alter_petpost_head_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petpost',
            old_name='head_image',
            new_name='thumnail',
        ),
    ]
