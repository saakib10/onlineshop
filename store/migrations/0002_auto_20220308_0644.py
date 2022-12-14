# Generated by Django 3.1.7 on 2022-03-08 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.itemcategory'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
