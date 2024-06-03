# Generated by Django 4.2.13 on 2024-06-03 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_subscriptionpackage_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkowner',
            name='subscription_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parkowner',
            name='subscription_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parkowner',
            name='subscription_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='accounts.subscriptionpackage'),
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
