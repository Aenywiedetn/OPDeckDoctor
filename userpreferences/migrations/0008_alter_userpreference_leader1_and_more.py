# Generated by Django 4.2.5 on 2023-11-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpreferences', '0007_alter_userpreference_leader1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreference',
            name='leader1',
            field=models.CharField(default=''),
        ),
        migrations.AlterField(
            model_name='userpreference',
            name='leader2',
            field=models.CharField(default=''),
        ),
        migrations.AlterField(
            model_name='userpreference',
            name='leader3',
            field=models.CharField(default=''),
        ),
    ]
