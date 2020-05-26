from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Parkings, Bookingslite
from django.core import serializers

class Inicio(TemplateView):
    template_name= 'index.html'


class BusquedaAjax(TemplateView):
    model = Parkings

    def get(self, request, *args, **kwargs):

        lon1 = request.GET['lon1']
        lon2 = request.GET['lon2']  
        lat1 = request.GET['lat1']  
        lat2 = request.GET['lat2']   

        kwargs = {'lon__gte': lon1,'lon__lte': lon2,'lat__gte': lat1,'lat__lte': lat2} 
        parking = Parkings.objects.filter(**kwargs)
        data = serializers.serialize('json',parking,fields=('name','provider','lmpPID','address','lon','lat', 'country', 'region', 'area', 'PID', 'who', 'is_used', 'cancelable', 'cancel_mn', 'cancel_msg', 'max_height', 'hour_price', 'day_price', 'access_msg', 'user_val', 'lmp_val', 'ben_val', 'gen_val', 'car_pc', 'human_pc', 'slug','booking_url'))
        return HttpResponse(data, content_type='application/json')  

class BookingsliteSearchAjax(TemplateView):
    model = Bookingslite

    def get(self, request, *args, **kwargs):
        
        lon1 = request.GET['lon1']
        lon2 = request.GET['lon2']  
        lat1 = request.GET['lat1']  
        lat2 = request.GET['lat2']   
        kwargs = {'lon__gte': lon1,'lon__lte': lon2,'lat__gte': lat1,'lat__lte': lat2} 
        bookingslite = Bookingslite.objects.filter(**kwargs)
        data = serializers.serialize('json',bookingslite,fields=('timestamp', 'when', 'short_code', 'lat', 'lon', 'position', 'parking_found', 'selected_name', 'selected_lmpPID', 'trello_url',))
        return HttpResponse(data, content_type='application/json')



# class Bookingtime(TemplateView):
#     model = Bookingslite

#     def get(self, request, *args, **kwargs):
        
#         lon1 = request.GET['lon1']
#         lon2 = request.GET['lon2']  
#         lat1 = request.GET['lat1']  
#         lat2 = request.GET['lat2']   
#         kwargs = {'lon__gte': lon1,'lon__lte': lon2,'lat__gte': lat1,'lat__lte': lat2} 
#         bookingslite = Bookingslite.objects.filter(timestamp="2020-05-06T20:26:38+02:00")
#         data = serializers.serialize('json',bookingslite,fields=('timestamp', 'when', 'short_code', 'lat', 'lon', 'position', 'parking_found', 'selected_name', 'selected_lmpPID', 'trello_url',))
#         return HttpResponse(data, content_type='application/json')