from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import UserProfile, Court, Reservation, Group


class UserProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_create_user_profile(self):
        profile = UserProfile.objects.create(
            user=self.user,
            name='Juan Pérez',
            age=25,
            location='Madrid',
            gender_type='male'
        )

        self.assertEqual(profile.name, 'Juan Pérez')
        self.assertEqual(profile.age, 25)
        self.assertEqual(profile.location, 'Madrid')
        self.assertEqual(profile.gender_type, 'male')

    def test_user_profile_str(self):
        profile = UserProfile.objects.create(
            user=self.user,
            name='Juan Pérez',
            age=25,
            location='Madrid',
            gender_type='male'
        )
        self.assertEqual(str(profile), 'Juan Pérez, 25, Madrid, male')


class CourtTests(TestCase):
    def test_create_court(self):
        court = Court.objects.create(
            name='Pista Central',
            location='Barcelona',
            latitude=41.3851,
            longitude=2.1734,
            court_type='Sports pavilion'
        )

        self.assertEqual(court.name, 'Pista Central')
        self.assertEqual(court.location, 'Barcelona')
        self.assertEqual(court.court_type, 'Sports pavilion')

    def test_court_str(self):
        court = Court.objects.create(
            name='Pista Central',
            location='Barcelona',
            court_type='Sports pavilion'
        )
        self.assertEqual(str(court), 'Pista Central, Barcelona, Sports pavilion')


class ReservationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.court = Court.objects.create(
            name='Pista Central',
            location='Barcelona',
            court_type='Sports pavilion'
        )

    def test_create_reservation(self):
        reservation = Reservation.objects.create(
            user=self.user,
            court=self.court,
            date='2025-06-04',
            start_time='10:00',
            finish_time='11:00',
            name_reservation='Reserva matinal'
        )

        self.assertEqual(reservation.date, '2025-06-04')
        self.assertEqual(reservation.start_time, '10:00')
        self.assertEqual(reservation.finish_time, '11:00')
        self.assertEqual(reservation.name_reservation, 'Reserva matinal')


class GroupTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass123')
        self.user2 = User.objects.create_user(username='user2', password='pass123')
        self.court = Court.objects.create(
            name='Pista Central',
            location='Barcelona',
            court_type='Sports pavilion'
        )
        self.reservation = Reservation.objects.create(
            user=self.user1,
            court=self.court,
            date='2025-06-04',
            start_time='10:00',
            finish_time='11:00'
        )

    def test_create_group(self):
        group = Group.objects.create(
            name='Grupo de Voleyball',
            court=self.court,
            reservation=self.reservation,
            description='Grupo para jugar al Voleyball'
        )
        group.users.add(self.user1, self.user2)

        self.assertEqual(group.name, 'Grupo de Voleyball')
        self.assertEqual(group.description, 'Grupo para jugar al Voleyball')
        self.assertEqual(group.users.count(), 2)
        self.assertEqual(group.court, self.court)
        self.assertEqual(group.reservation, self.reservation)

    def test_group_str(self):
        group = Group.objects.create(
            name='Grupo de Voleyball',
            court=self.court,
            reservation=self.reservation
        )
        self.assertEqual(str(group), 'Grupo de Voleyball')