# Generated by Django 4.2.13 on 2024-05-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_booking_subscription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='slot',
            field=models.IntegerField(choices=[]),
        ),
    ]
