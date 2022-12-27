# Generated by Django 4.1.4 on 2022-12-25 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0015_alter_postcategory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendpost',
            name='post_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pet.postcategory'),
        ),
        migrations.AddField(
            model_name='showoffpost',
            name='post_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pet.postcategory'),
        ),
    ]
