from django.test import TestCase
from django.contrib.auth.models import User
from .models import MemberProfile, SaveBook, Purchase
from django.urls import reverse
import json

class MemberProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass123")

    def test_profile_creation(self):
        profile = MemberProfile.objects.create(
            user=self.user,
            profile_description="Book lover",
            fav_book="1984",
            cur_book="Dune",
            fav_author="Orwell",
            fav_genres="Sci-Fi",
            public=True
        )
        self.assertEqual(profile.user.username, "testuser")
        self.assertEqual(profile.fav_book, "1984")

    def test_profile_defaults(self):
        profile = MemberProfile.objects.create(user=self.user)
        self.assertFalse(profile.public)  # Default value
        self.assertIsNone(profile.fav_book)  # Nullable field

class SaveBookModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass123")
    def test_save_book(self):
        save_book = SaveBook.objects.create(
            user=self.user,
            title="Book lover",
            author="Orwell",
            book=3

        )
        self.assertEqual(save_book.user.username, "testuser")
        self.assertEqual(save_book.title, "Book lover")
        self.assertEqual(save_book.author, "Orwell")
        self.assertEqual(save_book.book, 3)

class PurchaseModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="pass123"
        )

    def test_purchase_creation(self):
        purchase = Purchase.objects.create(
            user=self.user,
            title="1984",
            author="George Orwell",
            book=1
        )

        self.assertEqual(purchase.user.username, "testuser")
        self.assertEqual(purchase.title, "1984")
        self.assertEqual(purchase.author, "George Orwell")
        self.assertEqual(purchase.book, 1)

# view tests
class ViewLoggingInOutTest(TestCase):

    def test_membership_success(self):

        response = self.client.post(
            reverse('membership'),
            data=json.dumps({
                'username': 'testuser',
                'email': 'test@test.com',
                'password1': 'pass123',
                'password2': 'pass123',
                'firstname': 'John',
                'lastname': 'Doe'
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 202)
        self.assertEqual(User.objects.count(), 1)

        user = User.objects.get(username='testuser')

        self.assertEqual(user.email, 'test@test.com')

    def login_pass_mixmatch_test(self):
        response = self.client.post(
            reverse('membership'),
            data=json.dumps({
                'username': 'testuser',
                'email': 'test@test.com',
                'password1': 'pass123',
                'password2': 'wrongpass',
                'firstname': 'John',
                'lastname': 'Doe'
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(User.objects.count(), 0)