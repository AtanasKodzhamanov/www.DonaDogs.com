# Generated by Django 4.1.3 on 2022-11-12 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0039_dog_adoption_country_bg_dog_adoption_country_eng_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dog',
            old_name='active',
            new_name='status',
        ),
    ]