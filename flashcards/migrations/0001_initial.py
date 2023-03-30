from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcards',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('box_number', models.IntegerField(default=1)),

            ],
        ),
    ]
