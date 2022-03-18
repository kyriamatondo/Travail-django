from django.shortcuts import render
from .db_membres import membres

def home_view(request):
    return render(request, 'home.html')

def membres_view(request):
    return render(request, 'membres.html', context={'membres':membres})

def contact_view(request):
    return render(request, 'contact.html')