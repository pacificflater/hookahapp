# Generated by Django 3.1 on 2020-08-15 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0015_auto_20200815_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacturer',
            name='type',
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sklad.manufacturertype'),
        ),
    ]
