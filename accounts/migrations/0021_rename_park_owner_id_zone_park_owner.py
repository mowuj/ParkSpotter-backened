# Generated by Django 4.2.13 on 2024-05-18 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_zone_park_owner_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zone',
            old_name='park_owner_id',
            new_name='park_owner',
        ),
    ]
