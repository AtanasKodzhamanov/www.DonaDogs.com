# Generated by Django 4.1.3 on 2022-11-14 21:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0047_alter_donations_year_month"),
    ]

    operations = [
        migrations.AddField(
            model_name="people",
            name="virtual_adopter",
            field=models.CharField(
                blank=True, choices=[("Y", "Y"), ("N", "N")], default="No", max_length=2
            ),
        ),
    ]
