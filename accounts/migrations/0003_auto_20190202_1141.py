# Generated by Django 2.1.5 on 2019-02-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190202_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='perfil',
            field=models.CharField(max_length=30),
        ),
    ]