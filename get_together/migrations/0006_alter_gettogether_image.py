# Generated by Django 4.2.7 on 2023-11-24 11:12

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("get_together", "0005_alter_category_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gettogether",
            name="image",
            field=django_resized.forms.ResizedImageField(
                blank=True,
                crop=None,
                force_format="WEBP",
                keep_meta=True,
                quality=75,
                scale=None,
                size=[300, None],
                upload_to="get_together/",
            ),
        ),
    ]
