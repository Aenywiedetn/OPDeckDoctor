# Generated by Django 4.2.5 on 2024-05-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0013_rename_id_card_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='idx',
            field=models.CharField(default='', unique=True),
        ),
    ]
