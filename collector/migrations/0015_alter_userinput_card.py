# Generated by Django 4.2.5 on 2024-05-02 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0014_alter_card_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinput',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.card', to_field='idx'),
        ),
    ]
