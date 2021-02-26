# Generated by Django 3.1.7 on 2021-02-25 06:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sub_district', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('floor_view', models.CharField(max_length=50)),
                ('unit_type', models.CharField(max_length=10)),
                ('condition', models.TextField(max_length=15)),
                ('price_per_month', models.IntegerField()),
                ('price_per_year', models.IntegerField()),
                ('sqft', models.DecimalField(decimal_places=1, max_digits=5)),
                ('facility', models.TextField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
    ]
