# Generated by Django 2.1.5 on 2019-04-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190412_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='aniversario',
            field=models.DateField(blank=True, null=True),
        ),
    ]
