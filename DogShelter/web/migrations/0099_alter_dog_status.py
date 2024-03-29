# Generated by Django 4.1.6 on 2023-02-23 03:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0098_alter_longpost_location_alter_noticeboard_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dog",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Active", "Active"),
                    ("New", "New"),
                    ("Dead", "Dead"),
                    ("Adopted", "Adopted"),
                    ("Sick", "Sick"),
                ],
                default="New",
                help_text="Статус на кучето: Активно, Починало, Осиновено, Болно. Активните кучета ще се показват в началната страница. Болните в страницата на клиниката. Осиновените в страницата за осиновяване. Починалите не се показват никъде. ДА СЕ ПОПЪЛВА НА ВРЕМЕ СЪГЛАСУВАНО СЪС СТАТУСА ВЪВ ФЕЙСБУК!",
                max_length=10,
            ),
        ),
    ]
