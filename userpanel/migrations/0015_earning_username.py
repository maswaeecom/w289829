# Generated by Django 4.0.4 on 2022-10-26 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanel', '0014_alter_newlotteries_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='earning',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
