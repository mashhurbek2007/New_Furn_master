# Generated by Django 4.0.6 on 2022-08-20 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0024_alter_profile_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telephone',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
