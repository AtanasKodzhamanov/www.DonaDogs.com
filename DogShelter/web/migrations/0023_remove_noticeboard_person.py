# Generated by Django 4.1 on 2022-11-06 03:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0022_noticeboard_person"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="noticeboard",
            name="person",
        ),
    ]
