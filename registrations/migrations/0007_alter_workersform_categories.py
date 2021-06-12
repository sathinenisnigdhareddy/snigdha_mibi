# Generated by Django 3.2.1 on 2021-06-08 02:38

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0006_alter_workersform_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workersform',
            name='categories',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('orange', 'Oranges'), ('cantaloupe', 'Cantaloupes'), ('mango', 'Mangoes'), ('honeydew', 'Honeydews')], max_length=32),
        ),
    ]
