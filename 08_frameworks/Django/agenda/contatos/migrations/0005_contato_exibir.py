# Generated by Django 3.2.9 on 2021-12-21 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_alter_contato_data_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='exibir',
            field=models.BooleanField(default=True),
        ),
    ]