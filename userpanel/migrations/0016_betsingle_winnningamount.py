# Generated by Django 4.0.4 on 2022-10-26 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanel', '0015_earning_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='betsingle',
            name='winnningamount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
