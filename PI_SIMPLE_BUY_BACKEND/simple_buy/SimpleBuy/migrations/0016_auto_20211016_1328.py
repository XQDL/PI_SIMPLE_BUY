# Generated by Django 3.0.4 on 2021-10-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleBuy', '0015_auto_20211016_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='itens_nf',
            name='frete',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='itens_nf',
            name='valor_unitario',
            field=models.FloatField(default=0),
        ),
    ]
