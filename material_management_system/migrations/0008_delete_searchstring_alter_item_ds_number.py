# Generated by Django 4.0.6 on 2022-08-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_management_system', '0007_searchstring_alter_item_feature'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SearchString',
        ),
        migrations.AlterField(
            model_name='item',
            name='ds_number',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]