# Generated by Django 2.1.5 on 2019-01-24 12:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appkraft', '0009_compras_quantidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra_Id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Andamento', 'Andamento'), ('Finalizada', 'Finalizada'), ('Orçamento', 'Orçamento')], max_length=10)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='compras',
            name='codigo_compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appkraft.Compra_Id'),
        ),
    ]
