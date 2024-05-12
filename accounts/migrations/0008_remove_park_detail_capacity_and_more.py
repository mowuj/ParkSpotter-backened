# Generated by Django 4.2.13 on 2024-05-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_park_detail_park_plan_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='park_detail',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='park_detail',
            name='park_plan_text',
        ),
        migrations.AddField(
            model_name='park_detail',
            name='park_plan',
            field=models.CharField(blank=True, choices=[], max_length=2),
        ),
    ]