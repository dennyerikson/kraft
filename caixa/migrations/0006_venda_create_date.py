# Generated by Django 2.1.5 on 2019-08-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0005_auto_20190412_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='create_date',
            field=models.DateField(auto_now=True),
        ),
    ]
