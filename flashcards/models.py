import datetime
from django.db import models


# Create your models here.


class Flashcards(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box_number = models.IntegerField(default=1)

    def __str__(self):
        return f"Question: {self.question} Answer: {self.answer}"
