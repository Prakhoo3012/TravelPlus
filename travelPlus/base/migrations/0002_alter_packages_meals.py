# Generated by Django 4.2.5 on 2023-09-10 14:12

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="packages",
            name="meals",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("breakfast", "Breakfast"),
                    ("lunch", "Lunch"),
                    ("dinner", "Dinner"),
                ],
                max_length=64,
            ),
        ),
    ]
