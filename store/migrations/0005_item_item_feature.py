# Generated by Django 3.1.7 on 2022-03-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_item_item_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_feature',
            field=models.CharField(choices=[('YE', 'Freshman'), ('NO', 'Sophomore')], default='NO', max_length=2),
        ),
    ]
