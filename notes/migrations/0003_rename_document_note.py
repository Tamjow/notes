# Generated by Django 3.2.3 on 2021-05-22 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_document_expiration_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Document',
            new_name='Note',
        ),
    ]
