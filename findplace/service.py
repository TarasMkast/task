import requests
import googlemaps
import json
import time
from django.http import Http404
from .form import *


class Service:

    def __init__(self, addres, type_place):
        self.addres = addres
        self.type_place = type_place

    try:
        API_KEY = 'AIzaSyDAsI_DWSuJT1VkzsHS0sdcunUwjdkCUQo'
        gmap = googlemaps.Client(key=API_KEY)
    except requests.ConnectionError as e:
            print()
            print("There is no Internet connection!")
            print("Error", e)

    def location(self, key=API_KEY):
        addres = self.addres
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?parameters'
        extend = {'address': addres, 'key': key}
        r = requests.get(serviceurl, params=extend)
        todos = json.loads(r.text)
        rs = todos['results']
        loc = rs[0]['geometry']['location']
        loclat = str(loc['lat'])
        loclng = str(loc['lng'])
        location = (loclat + ', ' + loclng)
        return location

    def get_places(self, gmap = gmap):
        type_place = self.type_place
        location = self.location()
        places_result = gmap.places_nearby(location=location, radius=1000, open_now=False, type=type_place)
        return places_result

    def get_distance(self, places_result = None, key=API_KEY, gmap = gmap):
        location = self.location()
        if places_result is None:
            places_result = self.get_places()

        serviceurl = "https://maps.googleapis.com/maps/api/distancematrix/json?"
        data = []
        for place in places_result['results']:
            name = place['name']
            start = location
            my_place_id = place['place_id']
            my_fields = ['formatted_address', 'name', 'type']
            place_details = gmap.place(place_id=my_place_id, fields=my_fields)
            details = place_details['result']['formatted_address']
            end = "|" + details + ","
            extend = {'units': 'metric', 'origins': start, 'destinations': end, 'key': key, 'departure_time': 'now',
                    'mode': 'driving', 'traffic_model': 'best_guess'}

            r = requests.get(serviceurl, params=extend)
            js = r.json()
            data.append(name + (str(', ')) + js['destination_addresses'][0] + str(',  ') +
                    js['rows'][0]['elements'][0]['distance']['text'])

        return data

    def next_page(self, gmap = gmap):
        service = Service(PlaceForm.address, PlaceForm.type_place)
        a = service.get_places()
        try:

            time.sleep(3)
            places_result = gmap.places_nearby(page_token=a['next_page_token'])

        except:
            raise Http404("Дані відсутні, поверніть назад на головну сторінку ")

        return places_result





















# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# import requests
# import googlemaps
# import json
# from .form import PlaceForm
# from django import forms
# import time
#
# def service():
#     API_KEY = 'AIzaSyDAsI_DWSuJT1VkzsHS0sdcunUwjdkCUQo'
#     gmap = googlemaps.Client(key=API_KEY)
#     def location(addres=PlaceForm.address, key=API_KEY):
#         serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?parameters'
#         extend = {'address': addres, 'key': key}
#
#         try:
#             r = requests.get(serviceurl, params=extend)
#
#         except requests.ConnectionError as e:
#             print()
#             print("There is no Internet connection!")
#             print("Error", e)
#
#         todos = json.loads(r.text)
#         rs = todos['results']
#         loc = rs[0]['geometry']['location']
#         loclat = str(loc['lat'])
#         loclng = str(loc['lng'])
#         location = (loclat + ', ' + loclng)
#         return location
#
#     def get_places(type_place=PlaceForm.type_place, location=location(), key=API_KEY):
#         try:
#             gmap = googlemaps.Client(key=key)
#             places_result = gmap.places_nearby(location=location, radius=1000, open_now=False, type=type_place)
#         except requests.ConnectionError as e:
#             print()
#             print("There is no Internet connection!")
#             print("Error", e)
#         return places_result
#
#         # def get_distance(places_result=get_places(), location=location(), key=API_KEY):
#         #     serviceurl = "https://maps.googleapis.com/maps/api/distancematrix/json?"
#         #     data = []
#         #
#         #     gmap = googlemaps.Client(key=key)
#         #     for place in places_result['results']:
#         #         name = place['name']
#         #         start = location
#         #         my_place_id = place['place_id']
#         #         my_fields = ['formatted_address', 'name', 'type']
#         #         place_details = gmap.place(place_id=my_place_id, fields=my_fields)
#         #         # type_info = place['types']
#         #         details = place_details['result']['formatted_address']
#         #         end = "|" + details + ","
#         #         extend = {'units': 'metric', 'origins': start, 'destinations': end, 'key': key, 'departure_time': 'now',
#         #               'mode': 'driving', 'traffic_model': 'best_guess'}
#         #
#         #         try:
#         #
#         #             r = requests.get(serviceurl, params=extend)
#         #
#         #         except requests.ConnectionError as e:
#         #
#         #             print()
#         #             print("There is no Internet connection!")
#         #             print("Error", e)
#         #
#         #         js = r.json()
#         #         data.append(name + (str(', ')) + js['destination_addresses'][0] + str(',  ') +
#         #                  js['rows'][0]['elements'][0]['distance']['text'])
#         #
#         #     return data
#     return {'location': location(), 'get_places':get_places()}
#
#
#
#
# def get_distance(arg):
#     API_KEY = 'AIzaSyDAsI_DWSuJT1VkzsHS0sdcunUwjdkCUQo'
#     def get_distancee(places_result, location=service()['location'], key=API_KEY):
#         serviceurl = "https://maps.googleapis.com/maps/api/distancematrix/json?"
#         data = []
#
#         gmap = googlemaps.Client(key=key)
#         for place in places_result['results']:
#             name = place['name']
#             start = location
#             my_place_id = place['place_id']
#             my_fields = ['formatted_address', 'name', 'type']
#             place_details = gmap.place(place_id=my_place_id, fields=my_fields)
#             # type_info = place['types']
#             details = place_details['result']['formatted_address']
#             end = "|" + details + ","
#             extend = {'units': 'metric', 'origins': start, 'destinations': end, 'key': key, 'departure_time': 'now',
#                       'mode': 'driving', 'traffic_model': 'best_guess'}
#
#             try:
#
#                 r = requests.get(serviceurl, params=extend)
#
#             except requests.ConnectionError as e:
#
#                 print()
#                 print("There is no Internet connection!")
#                 print("Error", e)
#
#             js = r.json()
#             data.append(name + (str(', ')) + js['destination_addresses'][0] + str(',  ') +
#                         js['rows'][0]['elements'][0]['distance']['text'])
#
#         return data
#     return get_distancee()