# Generated by Django 3.0.4 on 2021-10-17 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleBuy', '0019_auto_20211017_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='descricao',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]