# Generated by Django 4.1 on 2023-03-29 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0003_cards_delete_flashcards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='box_ID',
            field=models.IntegerField(default=1),
        ),
    ]
