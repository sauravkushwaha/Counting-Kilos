from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'Goa'
    dest1.desc = 'The City That Never Sleeps...'
    dest1.img = 'destination_5.jpg'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Ladakh'
    dest2.desc = 'Dream...'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Mumbai'
    dest3.desc = 'Beautiful City...'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750
    dest3.offer = False

    dest4 = Destination()
    dest4.name = 'Hyderabad'
    dest4.desc = 'Biryani...'
    dest4.img = 'destination_4.jpg'
    dest4.price = 650
    dest4.offer = True
    
    dest5 = Destination()
    dest5.name = 'Delhi'
    dest5.desc = 'Heart...'
    dest5.img = 'destination_7.jpg'
    dest5.price = 650
    dest5.offer = True

    dests = [dest1, dest2, dest3, dest4, dest5 ]

    return render(request, "index.html", {'dests': dests})

def contact(request):
    return render(request, "contact.html")