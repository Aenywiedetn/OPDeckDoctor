# Generated by Django 4.2.5 on 2023-11-14 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0006_alter_userinput_number_owned_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.CharField(default=''),
        ),
    ]
