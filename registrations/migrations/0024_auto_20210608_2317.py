# Generated by Django 3.2.1 on 2021-06-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0023_auto_20210608_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='workers',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
