# from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from main.models import (Experience, Rating, User, Location, Property,
                         Booking)
from main.serializers import PropertySerializer

PROPERTY_URL = reverse('main:property-list')


def sampleExperience(**params):
    """Create and return a location"""
    defaults = {
        'title': 'Test experience',
        'category': 'Sports',
        'description': 'Test sports experience',
        'price': 30.00,
        'imgUrl': 'mockImagePlaceholder'
    }
    defaults.update(params)

    return Experience.objects.create(**defaults)


def sampleRating(**params):
    """Create a rating"""
    defaults = {
        'score': 5
    }
    defaults.update(params)

    return Rating.objects.create(**defaults)


def sampleUser(**params):
    """Create a rating"""
    defaults = {
        'firstName': 'raymond',
        'lastName': 'yau',
        'email': 'test@test.com'
    }
    defaults.update(params)

    return User.objects.create(**defaults)


def sampleLocation(experience, **params):
    """Create and return a location"""
    defaults = {
        'city': "Glasgow",
        'country': 'UK',
        'imgUrl': 'mockImagePlaceholder',
        'experiences': experience
    }
    defaults.update(params)

    return Location.objects.create(**defaults)


def sampleProperty(name, location, **params):
    """Create and return a sample property"""
    defaults = {
        'name': name,
        'beds': 1,
        'price': 55.50,
        'roomType': "Double",
        'address': "23 Earl St, Glasgow, G14 0BA, UK",
        'location': location,
        'lat': 55.876885,
        'lng': -4.347243,
        'maxGuests': 2,
        'rooms': 1,
        'tagline': 'Great spacious property for rent',
        'info': 'Information about this property',
    }
    defaults.update(params)

    return Property.objects.create(**defaults)


def sampleBooking(user, prop, rating, startDate, endDate):
    defaults = {
        'user': user,
        'property': prop,
        'startDate': startDate,
        'endDate': endDate
    }
    # defaults.update(params)

    return Booking.objects.create(**defaults)


class PropertyApiTests(TestCase):
    """Test property API access"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_available_properties(self):
        """Test retrieving a list of properties"""
        # Create an experience
        exp = sampleExperience()

        # Create a rating
        sampleRating()

        # Create a user
        sampleUser()

        # Create a sample location
        loc = sampleLocation(exp)

        # Create 2 sample properties
        sampleProperty('prop1', loc)
        sampleProperty('prop2', loc)

        # Create 2 sample bookings
        # sampleBooking(user, prop1, rating,
        #               '2020-09-05T15:00:00.127325Z',
        #               '2020-09-05T15:00:00.127325Z')
        # sampleBooking(user, prop1, rating,
        #               '2020-09-26T15:00:00.127325Z',
        #               '2020-09-30T15:00:00.127325Z')

        res = self.client.get(PROPERTY_URL)

        properties = Property.objects.all()
        # setting many=True returns a list of items
        serializer = PropertySerializer(properties, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['count'], len(serializer.data))
        # self.assertEqual(res.data, serializer.data)
