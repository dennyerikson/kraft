# Generated by Django 2.1.5 on 2019-02-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appkraft', '0010_auto_20190124_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='foto',
            field=models.ImageField(default='exit', upload_to='appkraft'),
            preserve_default=False,
        ),
    ]
