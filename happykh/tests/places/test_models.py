"""Tests for models of places app"""
import pytest
from django.db.utils import IntegrityError
from places.models import Place, Address
from users.models import User
from ..utils import BaseTestCase


@pytest.mark.django_db
class PlaceTestCase(BaseTestCase):
    """Tests for place model"""

    def setUp(self):
        """Create user and place objects"""
        self.regular_user = User.objects.create_user(email='any@mail.com',
                                                     password='password')
        self.place_address = Address.objects.create(
            address='address',
            latitude=50.12345,
            longitude=45.1345
        )
        self.place_info = {'user': self.regular_user,
                           'name': 'name',
                           'description': 'description',
                           'address': self.place_address
                           }
        self.place = Place.objects.create(
            user=self.place_info['user'],
            name=self.place_info['name'],
            description=self.place_info['description'],
            address=self.place_info['address']
        )

    def test_place_creation(self):
        """Testing default place attributes"""
        place = self.place
        self.assertIsInstance(place, Place)
        self.assertEqual(self.place_info['name'], place.name)
        self.assertEqual(self.place_info['description'], place.description)
        self.assertEqual(self.place_info['address'], place.address)

    def test_deletion_user(self):
        """Testing Place model behavior after deleting a user"""
        user_on_delete = self.regular_user

        User.objects.get(email="any@mail.com").delete()
        with self.assertRaises(Place.DoesNotExist) as dne:
            Place.objects.get(user=user_on_delete)
        self.assertEqual(type(dne.exception), Place.DoesNotExist)


@pytest.mark.django_db
class AddressTestCase(BaseTestCase):
    """Tests for address model"""

    def setUp(self):
        self.address_info = {'address': 'some str',
                             'latitude': 50.12345,
                             'longitude': 36.23456}
        self.successful_created_address = Address.objects.create(
            address=self.address_info['address'],
            latitude=self.address_info['latitude'],
            longitude=self.address_info['longitude']
        )

    def test_successful_creation(self):
        self.assertIsInstance(self.successful_created_address, Address)
        self.assertEqual(self.address_info['address'],
                         self.successful_created_address.address)
        self.assertEqual(self.address_info['latitude'],
                         self.successful_created_address.latitude)
        self.assertEqual(self.address_info['longitude'],
                         self.successful_created_address.longitude)

    def test_creation_without_location(self):
        with self.assertRaises(IntegrityError) as error:
            Address.objects.create(address=self.address_info['address'])
        self.assertEqual(type(error.exception), IntegrityError)

    def test_creation_without_address_string(self):
        self.assertIsInstance(Address.objects.create(
                                latitude=self.address_info['latitude'],
                                longitude=self.address_info['longitude']),
                              Address)
