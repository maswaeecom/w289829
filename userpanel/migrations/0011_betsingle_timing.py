# Generated by Django 4.0.4 on 2022-10-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanel', '0010_newlotteries_timing_newlotteriesthreem_timing'),
    ]

    operations = [
        migrations.AddField(
            model_name='betsingle',
            name='timing',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
