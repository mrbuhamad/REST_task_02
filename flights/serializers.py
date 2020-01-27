from rest_framework import serializers

from .models import Flight, Booking


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailSerilizer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields =['flight', 'date', 'id', 'passengers']

class BookingupdateSerilizer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields =['date', 'passengers']
