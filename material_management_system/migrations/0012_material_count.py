# Generated by Django 4.0.6 on 2022-08-26 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_management_system', '0011_remove_material_is_group_item_is_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
