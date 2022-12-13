# Generated by Django 4.1.2 on 2022-12-13 07:22

import DogShelter.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0066_aboutphoto_about_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_pic_1',
            field=models.URLField(blank=True, default='', help_text='Снимка 1 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic_10',
            field=models.URLField(blank=True, default='', help_text='Снимка 10 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic_2',
            field=models.URLField(blank=True, default='', help_text='Снимка 2 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic_3',
            field=models.URLField(blank=True, default='', help_text='Снимка 3 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic_4',
            field=models.URLField(blank=True, default='', help_text='Снимка 4 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic_5',
            field=models.URLField(blank=True, default='', help_text='Снимка 5 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic_6',
            field=models.URLField(blank=True, default='', help_text='Снимка 6 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic_7',
            field=models.URLField(blank=True, default='', help_text='Снимка 7 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic_8',
            field=models.URLField(blank=True, default='', help_text='Снимка 8 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic_9',
            field=models.URLField(blank=True, default='', help_text='Снимка 9 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='about',
            name='section_desc_bg',
            field=models.TextField(blank=True, default='', help_text='Описание на секцията на Български.', validators=[DogShelter.web.validators.validate_bulgarian]),
        ),
        migrations.AlterField(
            model_name='about',
            name='section_desc_eng',
            field=models.TextField(blank=True, default='Info coming soon...', help_text='Описание на секцията на Английски.', validators=[DogShelter.web.validators.validate_english]),
        ),
        migrations.AlterField(
            model_name='about',
            name='section_title_bg',
            field=models.TextField(blank=True, default='', help_text='Заглавие на секцията на Български.', max_length=100, validators=[DogShelter.web.validators.validate_bulgarian]),
        ),
        migrations.AlterField(
            model_name='about',
            name='section_title_eng',
            field=models.TextField(blank=True, default='', help_text='Заглавие на секцията на Английски.', max_length=100, validators=[DogShelter.web.validators.validate_english]),
        ),
        migrations.AlterField(
            model_name='aboutphoto',
            name='url',
            field=models.URLField(max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='adoption_country_bg',
            field=models.CharField(blank=True, default='', help_text='Държава на осиновяване на Български.', max_length=60, validators=[DogShelter.web.validators.validate_bulgarian]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='adoption_country_eng',
            field=models.CharField(blank=True, default='', help_text='Държава на осиновяване на Английски.', max_length=60, validators=[DogShelter.web.validators.validate_english]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='adoption_pic_after_1',
            field=models.URLField(blank=True, default='', help_text='Снимка 1 на кучето след осиновяване.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='adoption_pic_after_2',
            field=models.URLField(blank=True, default='', help_text='Снимка 2 на кучето след осиновяване.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='adoption_pic_after_3',
            field=models.URLField(blank=True, default='', help_text='Снимка 3 на кучето след осиновяване.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='name_bg',
            field=models.CharField(default='', help_text='Име на куче на Български.', max_length=60, validators=[DogShelter.web.validators.validate_bulgarian]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='name_eng',
            field=models.CharField(help_text='Име на куче на Английски.', max_length=60, null=True, unique=True, validators=[DogShelter.web.validators.validate_english]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='pic_2',
            field=models.URLField(blank=True, default='', help_text='Албумна снимка.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='pic_3',
            field=models.URLField(blank=True, default='', help_text='Албумна снимка.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='pic_4',
            field=models.URLField(blank=True, default='', help_text='Албумна снимка.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='pic_5',
            field=models.URLField(blank=True, default='', help_text='Албумна снимка.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='profile_pic',
            field=models.URLField(help_text='Профилна снимка.', max_length=300, null=True, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='story_bg',
            field=models.TextField(blank=True, default='', help_text='История на кучето на Български.', validators=[DogShelter.web.validators.validate_bulgarian]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='story_eng',
            field=models.TextField(blank=True, default='', help_text='История на кучето на Английски.', validators=[DogShelter.web.validators.validate_english]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='va_name_bg',
            field=models.CharField(blank=True, default='', help_text='Име на виртуален осиновител на Български.', max_length=60, validators=[DogShelter.web.validators.validate_bulgarian]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='va_name_eng',
            field=models.CharField(blank=True, default='', help_text='Име на виртуален осиновител на Английски.', max_length=60, validators=[DogShelter.web.validators.validate_english]),
        ),
        migrations.AlterField(
            model_name='donation',
            name='person_name_bg',
            field=models.CharField(default='', help_text='Име на дарителя на Български.', max_length=60, validators=[DogShelter.web.validators.validate_bulgarian]),
        ),
        migrations.AlterField(
            model_name='donation',
            name='person_name_eng',
            field=models.CharField(default='', help_text='Име на дарителя на Английски.', max_length=60, validators=[DogShelter.web.validators.validate_english]),
        ),
        migrations.AlterField(
            model_name='donationstory',
            name='donation_pic_1',
            field=models.URLField(blank=True, default='', help_text='Снимка 1 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='donationstory',
            name='donation_pic_2',
            field=models.URLField(blank=True, default='', help_text='Снимка 2 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='donationstory',
            name='donation_pic_3',
            field=models.URLField(blank=True, default='', help_text='Снимка 3 в секцията.', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='donationstory',
            name='donation_text_bg',
            field=models.TextField(blank=True, default='', help_text='Текст на дарението на Български (за секцията със снимки на дарания).', validators=[DogShelter.web.validators.validate_bulgarian]),
        ),
        migrations.AlterField(
            model_name='donationstory',
            name='donation_text_eng',
            field=models.TextField(blank=True, default='', help_text='Текст на дарението на Английски (за секцията със снимки на дарания).', validators=[DogShelter.web.validators.validate_english]),
        ),
        migrations.AlterField(
            model_name='noticeboard',
            name='note_bg',
            field=models.TextField(blank=True, default='', help_text='Съобщение на Български.', validators=[DogShelter.web.validators.validate_bulgarian]),
        ),
        migrations.AlterField(
            model_name='noticeboard',
            name='note_eng',
            field=models.TextField(blank=True, default='', help_text='Съобщение на Английски.', validators=[DogShelter.web.validators.validate_english]),
        ),
        migrations.AlterField(
            model_name='noticeboard',
            name='note_pic_1',
            field=models.URLField(blank=True, default='', help_text='Снимка 1 в съобщението (не задължителни).', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
        migrations.AlterField(
            model_name='noticeboard',
            name='note_pic_2',
            field=models.URLField(blank=True, default='', help_text='Снимка 2 в съобщението (не задължителни).', max_length=300, validators=[DogShelter.web.validators.validate_url]),
        ),
    ]
