# Generated by Django 3.0.6 on 2020-06-06 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobsApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banglorejobs',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='chennaijobs',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='hydjobs',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='punejobs',
            old_name='data',
            new_name='date',
        ),
    ]
