# Generated by Django 4.2.5 on 2023-11-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpreferences', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpreference',
            old_name='color',
            new_name='leader1',
        ),
        migrations.AddField(
            model_name='userpreference',
            name='leader2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userpreference',
            name='leader3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]