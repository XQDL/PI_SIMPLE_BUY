# Generated by Django 3.0.4 on 2021-10-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleBuy', '0012_ordemfornecimento_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemfornecimento',
            name='situacao',
            field=models.CharField(default='COMPRADOR_NEGOCIANDO', max_length=200),
        ),
    ]
