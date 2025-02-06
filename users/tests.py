from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class UserTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_user_registration(self):
        response = self.client.post(reverse('users:register'), {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword',
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'is_instructor': False,
            'is_learner': True,
            'is_institution': False,
        })
        print(response)  # Debugging line to check the response


    def test_user_login(self):
        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful login

    def test_user_profile_access(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('users:user_profile'))
        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after logout

