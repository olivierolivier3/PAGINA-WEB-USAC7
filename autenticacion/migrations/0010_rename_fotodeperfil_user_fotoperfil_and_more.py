# Generated by Django 4.2.5 on 2023-10-25 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0009_rename_foto_de_perfil_user_fotodeperfil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Fotodeperfil',
            new_name='FotoPerfil',
        ),
        migrations.AddField(
            model_name='user',
            name='FechaNacimiento',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
