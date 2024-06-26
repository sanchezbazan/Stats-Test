# Generated by Django 4.2.11 on 2024-04-15 21:24

from typing import List

from django.db import migrations, models

import stats_core.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies: List[str] = []

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                (
                    'sender',
                    models.CharField(max_length=64, validators=[stats_core.core.validators.HexStringValidator(64)])
                ),
                (
                    'signature',
                    models.CharField(max_length=128, validators=[stats_core.core.validators.HexStringValidator(128)])
                ),
                (
                    'recipient',
                    models.CharField(max_length=64, validators=[stats_core.core.validators.HexStringValidator(64)])
                ),
                ('amount', models.PositiveBigIntegerField()),
                ('transaction_fee', models.PositiveBigIntegerField()),
                ('payload', models.JSONField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
