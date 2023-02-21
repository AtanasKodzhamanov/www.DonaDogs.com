# Generated by Django 4.1.6 on 2023-02-21 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0091_longpost_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='longpost',
            name='background_color',
            field=models.CharField(blank=True, help_text='Въведете шестнадесетичен код на цвета, за да промените цвета на текста (#F5F5F5).', max_length=7),
        ),
        migrations.AddField(
            model_name='longpost',
            name='text_color',
            field=models.CharField(blank=True, help_text='Въведете шестнадесетичен код на цвета, за да промените цвета на текста (#414141).', max_length=7),
        ),
    ]
