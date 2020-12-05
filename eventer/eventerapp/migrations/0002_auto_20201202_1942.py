# Generated by Django 3.1.3 on 2020-12-02 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayName', models.CharField(blank=True, max_length=200)),
                ('emailId', models.CharField(blank=True, max_length=200)),
                ('responseStatus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('eventId', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('summary', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('createdBy', models.CharField(blank=True, max_length=200)),
                ('organizedBy', models.CharField(blank=True, max_length=200)),
                ('startDate', models.DateField(blank=True)),
                ('startTime', models.TimeField(blank=True)),
                ('endDate', models.DateField(blank=True)),
                ('endTime', models.TimeField(blank=True)),
                ('location', models.CharField(blank=True, max_length=400)),
                ('hangoutLink', models.CharField(blank=True, max_length=1000)),
                ('attachmentLink', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Reminders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(blank=True, max_length=200)),
                ('minutes', models.IntegerField(blank=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventerapp.events')),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.AddField(
            model_name='attendees',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventerapp.events'),
        ),
    ]