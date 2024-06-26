# Generated by Django 4.2.11 on 2024-04-15 21:24

from typing import List

import django.core.validators
from django.db import migrations, models

import stats_core.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies: List[str] = []

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'owner',
                    models.CharField(
                        blank=True,
                        max_length=64,
                        null=True,
                        validators=[stats_core.core.validators.HexStringValidator(64)]
                    )
                ),
                (
                    'transaction_fee',
                    models.PositiveBigIntegerField(
                        default=1, validators=[django.core.validators.MinValueValidator(1)]
                    )
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
