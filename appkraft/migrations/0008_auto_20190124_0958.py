# Generated by Django 2.1.5 on 2019-01-24 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appkraft', '0007_compras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='codigo_produto',
            field=models.IntegerField(),
        ),
    ]
