# Generated by Django 4.0.6 on 2022-08-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0015_profile_card_number_profile_facebook_profile_github_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
