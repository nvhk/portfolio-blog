from django.shortcuts import render
from .models import Praca

# Create your views here.
def home(request):
    prace = Praca.objects
    return render(request, 'prace/home.html', {'prace':prace})
