# Generated by Django 2.1.5 on 2019-02-27 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190202_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='perfil',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='perfil',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='accounts.Perfil'),
            preserve_default=False,
        ),
    ]
