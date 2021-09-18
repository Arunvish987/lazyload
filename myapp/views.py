from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    numbers = Number.objects.all()
    return render(request, 'myapp/index.html', {'numbers': numbers})

def load_word(request):
    number_id = request.GET.get('number')               #-------get current number id
    words = Word.objects.filter(number_id=number_id)   #------get words with respct to number id
    return render(request, 'myapp/word_dropdown.html', {'words': words})

