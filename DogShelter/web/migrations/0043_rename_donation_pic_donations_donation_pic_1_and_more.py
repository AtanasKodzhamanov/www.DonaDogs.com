# Generated by Django 4.1.3 on 2022-11-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0042_alter_dog_adoption_country_bg_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="donations",
            old_name="donation_pic",
            new_name="donation_pic_1",
        ),
        migrations.RemoveField(
            model_name="donations",
            name="donation_amount",
        ),
        migrations.RemoveField(
            model_name="donations",
            name="donation_currency",
        ),
        migrations.RemoveField(
            model_name="donations",
            name="donation_date",
        ),
        migrations.RemoveField(
            model_name="donations",
            name="person",
        ),
        migrations.AddField(
            model_name="about",
            name="location",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Gallery", "Gallery"),
                    ("About", "About"),
                    ("Infirmery", "Infirmery"),
                    ("Adoptions", "Adoptions"),
                    ("Virtual", "Virtual"),
                    ("Donations", "Donations"),
                ],
                default="Donations",
                max_length=25,
            ),
        ),
        migrations.AddField(
            model_name="about",
            name="section_title_bg",
            field=models.TextField(blank=True, default="", max_length=100),
        ),
        migrations.AddField(
            model_name="donations",
            name="donation_pic_2",
            field=models.URLField(blank=True, default="", max_length=300),
        ),
        migrations.AddField(
            model_name="donations",
            name="donation_pic_3",
            field=models.URLField(blank=True, default="", max_length=300),
        ),
        migrations.AddField(
            model_name="donations",
            name="donation_pic_4",
            field=models.URLField(blank=True, default="", max_length=300),
        ),
        migrations.AddField(
            model_name="donations",
            name="donation_pic_5",
            field=models.URLField(blank=True, default="", max_length=300),
        ),
        migrations.AddField(
            model_name="donations",
            name="order",
            field=models.IntegerField(default=99),
        ),
        migrations.AddField(
            model_name="donations",
            name="section_title_bg",
            field=models.TextField(blank=True, default="", max_length=150),
        ),
        migrations.AddField(
            model_name="donations",
            name="section_title_eng",
            field=models.TextField(blank=True, default="", max_length=150),
        ),
    ]
