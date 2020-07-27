from django.shortcuts import render

from django.shortcuts import render
from .service import Service
from .form import PlaceForm
from .models import History


def main(request):

    if request.method == "POST":
        PlaceForm.type_place = request.POST.get('type_place')
        PlaceForm.address = request.POST.get('address')
        PlaceForm.email_user = request.POST.get('email')
        a = History(email=PlaceForm.email_user, type_object=PlaceForm.type_place)
        a.save()
        service = Service(PlaceForm.address, PlaceForm.type_place)
        placeform = PlaceForm()
        datacontex = {'place': service.get_distance(), 'location': service.location(), 'form': placeform}
        return render(request, 'findplace/index.html', context=datacontex)
    else:

        placeform = PlaceForm()
        datacontex = {'form': placeform, 'location': '48.918765,24.710918'}

    return render(request, 'findplace/index.html', context=datacontex)


def next_page(request):
    if request.method == "POST":
        service = Service(PlaceForm.address, PlaceForm.type_place)
        places_result = service.next_page()
        placeform = PlaceForm()
        datacontex = {'place': service.get_distance(places_result), 'location': service.location(), 'form': placeform}
    return render(request, 'findplace/index.html', context=datacontex)



