# Generated by Django 3.0.6 on 2020-06-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdate', models.DateField()),
                ('Moviename', models.CharField(max_length=30)),
                ('Hero', models.CharField(max_length=30)),
                ('Heroine', models.CharField(max_length=30)),
                ('Rating', models.IntegerField()),
            ],
        ),
    ]