# Generated by Django 4.0.6 on 2022-08-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_management_system', '0016_bom_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='bom',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
