# Generated by Django 3.2.1 on 2021-06-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0011_auto_20210608_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
