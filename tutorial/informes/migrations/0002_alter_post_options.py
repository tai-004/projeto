# Generated by Django 4.0.2 on 2022-06-27 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('post', 'post'),)},
        ),
    ]
