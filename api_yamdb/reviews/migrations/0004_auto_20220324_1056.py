# Generated by Django 2.2.16 on 2022-03-24 07:56

import reviews.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220324_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(validators=[reviews.validators.custom_year_validator], verbose_name='Год выхода'),
        ),
    ]
