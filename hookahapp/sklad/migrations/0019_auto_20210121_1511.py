# Generated by Django 3.1 on 2021-01-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0018_auto_20210121_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flavour',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='mix',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
