# Generated by Django 4.2.5 on 2023-10-25 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0006_rename_picture_user_perfil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Perfil',
            new_name='picture',
        ),
    ]