import sqlite3
from logging import getLogger
from random import randint
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


LOGGER = getLogger()
DB_NAME = "flashcards.db"

def get_database_connection():
con = sqlite3.connect(DB_NAME)

def read_data_from_db():
    sql_query = ''' SELECT id, question, box_nr, answer FROM flashcards; '''

    con = get_database_connection()
    cur = con.cursor()

    cur.execute(sql_query)
    results = cur.fetchall()

    cur.close()
    con.close()

    return results

def hello(request):
    return HttpResponse('Hello, world!')


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


def error_404(request, exception):
    return render(request, 'notfound.html')


def error_500(request):
    return render(request, 'notfound.html')


def test_func(self):
    return super().test_func() and self.request.user.is_superuser
