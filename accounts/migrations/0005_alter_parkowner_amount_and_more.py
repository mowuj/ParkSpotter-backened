# Generated by Django 4.2.13 on 2024-05-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_parkowner_amount_alter_parkowner_payment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkowner',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='parkowner',
            name='payment_method',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
