# Generated by Django 4.2.1 on 2023-05-19 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meseros',
            new_name='Clientes',
        ),
    ]