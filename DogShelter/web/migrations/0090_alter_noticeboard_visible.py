# Generated by Django 4.1.6 on 2023-02-21 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0089_noticeboard_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticeboard',
            name='visible',
            field=models.BooleanField(default=True, help_text='Скриване или показване на публикацията. Показва се по подразбиране.'),
        ),
    ]