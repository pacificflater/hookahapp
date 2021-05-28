# Generated by Django 3.0.6 on 2020-08-14 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0012_manufacturer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='type',
            field=models.IntegerField(choices=[('TE', 'Tea'), ('TC', 'Tobacco')], null=True),
        ),
    ]
