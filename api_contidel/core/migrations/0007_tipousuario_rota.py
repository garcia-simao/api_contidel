# Generated by Django 4.2.5 on 2023-11-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_tipo_de_entidade_usuario_tipo_de_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipousuario',
            name='rota',
            field=models.CharField(default='ndjwi', max_length=100),
            preserve_default=False,
        ),
    ]