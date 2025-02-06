from django.test import TestCase
from .models import Webinar
from courses.models import Course  # Import the Course model
from django.core.exceptions import FieldError
from users.models import CustomUser  # Import the CustomUser model




class WebinarModelTest(TestCase):


    def setUp(self):
        # Create a course
        self.course = Course.objects.create(title='Test Course', description='Test Description')
        # Create a user
        self.user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='test123')
        # Create a webinar
        self.webinar = Webinar.objects.create(course=self.course, title='Test Webinar', description='Test Description', date='2022-12-31', time='18:00', user=self.user)
        # Create a second webinar
        self.webinar2 = Webinar.objects.create(course=self.course, title='Test Webinar 2', description='Test Description 2', date='2022-12-30', time='16:00', user=self.user)
        # Create a third webinar
        self.webinar3 = Webinar.objects.create(course=self.course, title='Test Webinar 3', description='Test Description 3', date='2022-12-29', time='14:00', user=self.user)



