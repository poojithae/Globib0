from django.shortcuts import render, get_object_or_404
from .models import Destination 

def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, ('index'))

def contact(request):
    return render(request, 'contact.html')

def news(request):
    return render(request, 'news.html')

def elements(request):
    return render(request, 'elements.html')

#def destinations(request, destination_id):
    #destination = get_object_or_404(Destination, pk=destination_id)
    #return render(request, 'destinations.html', {'destination': destination})

def destinations(request):
    return render(request, 'destinations.html')
