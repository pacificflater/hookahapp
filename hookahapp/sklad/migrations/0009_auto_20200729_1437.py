# Generated by Django 3.0.6 on 2020-07-29 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0008_auto_20200720_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlavourType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='flavour',
            name='flavour_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sklad.FlavourType'),
        ),
    ]
