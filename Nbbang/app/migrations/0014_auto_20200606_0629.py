# Generated by Django 3.0.6 on 2020-06-06 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200606_0607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='franchise',
            old_name='kakaolLnk',
            new_name='kakaoLink',
        ),
        migrations.RenameField(
            model_name='others',
            old_name='kakaolLink',
            new_name='kakaoLink',
        ),
        migrations.RenameField(
            model_name='ott',
            old_name='appLink',
            new_name='kakaoLink',
        ),
    ]