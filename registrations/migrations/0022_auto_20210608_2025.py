# Generated by Django 3.2.1 on 2021-06-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0021_auto_20210608_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker_model',
            name='Preferred_Work_Location',
        ),
        migrations.AddField(
            model_name='worker_model',
            name='Preferred_Work_Location',
            field=models.ManyToManyField(null=True, to='registrations.Work_Loc'),
        ),
    ]
