# Generated by Django 4.1.2 on 2022-12-24 03:08

import DogShelter.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0073_dog_adoption_story_bg_dog_adoption_story_eng'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationstory',
            name='donation_pic_4',
            field=models.URLField(blank=True, default='', help_text='Снимка 4 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AddField(
            model_name='donationstory',
            name='priority',
            field=models.IntegerField(default=0, help_text='Приоритетът ще определя .'),
        ),
    ]
