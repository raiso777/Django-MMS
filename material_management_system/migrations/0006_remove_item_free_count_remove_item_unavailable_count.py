# Generated by Django 4.0.6 on 2022-08-23 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material_management_system', '0005_alter_item_expected_count_alter_item_free_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='free_count',
        ),
        migrations.RemoveField(
            model_name='item',
            name='unavailable_count',
        ),
    ]
