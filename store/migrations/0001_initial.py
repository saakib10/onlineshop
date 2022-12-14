# Generated by Django 3.1.7 on 2022-03-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200, null=True)),
                ('item_price', models.FloatField(null=True)),
                ('item_discount_price', models.FloatField(blank=True, null=True)),
                ('item_front_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('item_back_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('item_description', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, null=True)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
