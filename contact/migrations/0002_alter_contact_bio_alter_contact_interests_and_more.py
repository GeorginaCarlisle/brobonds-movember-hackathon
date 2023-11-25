# Generated by Django 4.2.7 on 2023-11-25 01:03

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):
    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="bio",
            field=djrichtextfield.models.RichTextField(max_length=250),
        ),
        migrations.AlterField(
            model_name="contact",
            name="interests",
            field=djrichtextfield.models.RichTextField(max_length=100),
        ),
        migrations.AlterField(
            model_name="contact",
            name="why_you_want_to_become_a_facilitator",
            field=djrichtextfield.models.RichTextField(max_length=250),
        ),
    ]
