# Generated by Django 4.0.6 on 2022-08-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_management_system', '0013_remove_material_status_material_is_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='total_cost',
            field=models.FloatField(default=0.0),
        ),
    ]
