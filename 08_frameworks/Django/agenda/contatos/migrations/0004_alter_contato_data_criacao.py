# Generated by Django 3.2.9 on 2021-12-21 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_alter_contato_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(),
        ),
    ]
