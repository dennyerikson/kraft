# Generated by Django 2.1.5 on 2019-09-07 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0007_auto_20190826_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesa', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('observacao', models.TextField(max_length=190)),
            ],
        ),
    ]
