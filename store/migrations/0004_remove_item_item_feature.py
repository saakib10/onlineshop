# Generated by Django 3.1.7 on 2022-03-10 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_item_item_feature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_feature',
        ),
    ]
