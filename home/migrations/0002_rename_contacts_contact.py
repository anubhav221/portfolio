# Generated by Django 4.0.3 on 2022-03-11 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Contact',
        ),
    ]