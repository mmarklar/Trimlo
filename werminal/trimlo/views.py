from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, "board.html", {})

def board(request, pk):
    board = get_object_or_404(Board, pk=pk)
    context = {
        "board": board, 
        "columns": board.column_set.all()
    }
    return render(request, "board.html", context) 

def column_test(request):
    column = Column(title="Column title")
    card = Card(title="Test title", description="this is the description")
    card2 = Card(title="Test titl2e", description="this is the descriptio2n")
    card3 = Card(title="Test titl2e", description="this is the descriptio2n")
    card4 = Card(title="Test titl2e", description="this is the descriptio2n")
    card5 = Card(title="Test titl2e", description="this is the descriptio2n")
    card6 = Card(title="Test titl2e", description="this is the descriptio2n")
    card7 = Card(title="Test titl2e", description="this is the descriptio2n")
    card8 = Card(title="Test titl2e", description="this is the descriptio2n")
    card9 = Card(title="Test titl2e", description="this is the descriptio2n")
    return render(request, "partials/column.html", {"column": column, "cards": [card, card2, card3, card4, card5, card6, card7, card8, card9, card, card, card, card]})
    #return render(request, "partials/column.html", {"column": column, "cards": [card, card2, card3, card4]})
