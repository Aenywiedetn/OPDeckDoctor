# Generated by Django 4.2.5 on 2023-10-31 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='counter2k',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='cost',
            field=models.CharField(default=''),
        ),
        migrations.AlterField(
            model_name='card',
            name='counter',
            field=models.BooleanField(default=False),
        ),
    ]