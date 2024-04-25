from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    column = Column(title="Column title")
    card = Card(title="Test title", description="this is the description")
    return render(request, "partials/column.html", {"column": column, "cards": [card]})
