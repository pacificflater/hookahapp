# Generated by Django 3.0.6 on 2020-07-29 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0009_auto_20200729_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flavour',
            name='flavour_type',
        ),
        migrations.AddField(
            model_name='flavour',
            name='flavour_type',
            field=models.ManyToManyField(null=True, to='sklad.FlavourType'),
        ),
    ]
