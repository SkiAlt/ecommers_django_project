# Generated by Django 5.0.6 on 2024-07-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
