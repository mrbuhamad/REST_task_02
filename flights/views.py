from rest_framework.generics import (ListAPIView, RetrieveAPIView,
 RetrieveUpdateAPIView, DestroyAPIView)
from datetime import datetime

from .models import Flight, Booking
from .serializers import (FlightSerializer,
 BookingSerializer, BookingDetailSerilizer, BookingupdateSerilizer)


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer

class BookingDetailView(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDetailSerilizer
	lookup_field ='id'
	lookup_url_kwarg = 'booking_id'

class BookingUpdateView(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingupdateSerilizer
	lookup_field ='id'
	lookup_url_kwarg = 'booking_id'

class BookingdeleteView(DestroyAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDetailSerilizer
	lookup_field ='id'
	lookup_url_kwarg = 'booking_id'


