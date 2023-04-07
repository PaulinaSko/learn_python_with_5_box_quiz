import datetime
from random import randint
import sqlite3
from django.db import models


# Create your models here.


class Flashcards(models.Model):
    ID = models.IntegerField(primary_key=True)
    box_ID = models.IntegerField(default=1)
    question = models.CharField(max_length=256)
    answers = models.CharField(max_length=256, default="No answer")

    def __str__(self):  
        return f"Question: {self.question} Answer: {self.answers}"
