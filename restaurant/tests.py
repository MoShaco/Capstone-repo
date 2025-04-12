from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Booking, Menu
from decimal import Decimal
from datetime import datetime
class MenuTests(TestCase):
    """
    This class will test Menu endpoints
    """

    def setUp(self):
        self.client = APIClient()
        self.menu_data = {
            "title": "Mango Ice Cream",
            "price": Decimal("2.5"),
            "inventory": 10
        }
        self.menu = Menu.objects.create(**self.menu_data)

    def test_get_menu(self):
        url = reverse('menuitem-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    

    def test_create_menu(self):
        url = reverse('menuitem-list')
        response = self.client.post(url, self.menu_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)

    def test_invalid_menu_id(self):
        url = reverse('menuitem-details', args=[5])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class BookingTest(TestCase):
    """
    This class tests Booking endpoints
    """
    def setUp(self):
        self.client = APIClient()
        self.booking_data = {
            "name": "Mohammed Shaco",
            "no_of_guests": 4,
            "booking_date": datetime.today().date()
        }
        self.booking = Booking.objects.create(**self.booking_data)
        self.user = User.objects.create_user(username='username', password='password')

    def test_unauthenticated_user_get_bookings(self):
        url = reverse('booking-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_get_booking(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('booking-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_booking(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('booking-list')
        response = self.client.post(url, self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)
    

    def test_create_booking_invalid_data(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('booking-list')
        data = {
            "name": "",
            "no_of_guests": 0,
            "booking_date": "not-a-date"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)