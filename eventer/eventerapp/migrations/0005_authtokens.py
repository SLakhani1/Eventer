# Generated by Django 3.1.3 on 2020-12-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventerapp', '0004_auto_20201202_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthTokens',
            fields=[
                ('email', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('token', models.JSONField()),
            ],
        ),
    ]
