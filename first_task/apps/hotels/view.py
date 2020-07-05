from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Hotel, Room


app_name = 'hotels'


def hotels(request):
    hotels_list = Hotel.objects.order_by('-id')
    return render(request, 'hotels/hotels.html', {'hotels_list': hotels_list})


def hotel(request, hotel_id):
    try:
        h = Hotel.objects.get(id=hotel_id)
    except:
        raise Http404("Отель не найден!")

    try:
        r = Room.objects.filter(hotel_id=hotel_id)
    except:
        raise Http404("Комнаты не найдены!")

    return render(request, 'hotels/hotel.html', {'h': h, 'r': r})


def room(request, hotel_id, id):
    try:
        r = Room.objects.get(id=id)
    except:
        raise Http404("Комната не найдена!")

    h = Room.objects.get(id=id).hotel

    return render(request, 'rooms/room.html', {'r': r, 'h': h})
