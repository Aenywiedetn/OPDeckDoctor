# Generated by Django 4.2.5 on 2023-09-23 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0005_deck_decklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='img',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='card1',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='card2',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='card3',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='card4',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='card5',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='card6',
        ),
        migrations.AddField(
            model_name='deck',
            name='color1',
            field=models.CharField(default='Pure'),
        ),
        migrations.AddField(
            model_name='deck',
            name='color2',
            field=models.CharField(default='Pure'),
        ),
        migrations.AddField(
            model_name='deck',
            name='format',
            field=models.CharField(default='XXX'),
        ),
        migrations.AddField(
            model_name='deck',
            name='leader',
            field=models.CharField(default='lider'),
        ),
        migrations.AddField(
            model_name='deck',
            name='set',
            field=models.CharField(default='OP00'),
        ),
        migrations.AlterField(
            model_name='deck',
            name='id',
            field=models.CharField(default='decklistaDodatek_numer', primary_key=True, serialize=False),
        ),
    ]
