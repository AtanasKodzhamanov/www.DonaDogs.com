# Generated by Django 4.1.3 on 2022-12-18 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0069_alter_donation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersubscriber',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='newslettersubscriber',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]