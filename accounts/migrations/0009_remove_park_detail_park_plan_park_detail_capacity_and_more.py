# Generated by Django 4.2.13 on 2024-05-12 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_park_detail_capacity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='park_detail',
            name='park_plan',
        ),
        migrations.AddField(
            model_name='park_detail',
            name='capacity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='park_detail',
            name='park_plan_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
