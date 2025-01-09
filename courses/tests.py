from django.test import TestCase
from .models import Course, Lesson

class CourseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Course.objects.create(title='Test Course', description='This is a test course.', price=100.00)

    def test_course_title(self):
        course = Course.objects.get(id=1)
        self.assertEqual(course.title, 'Test Course')

    def test_course_price(self):
        course = Course.objects.get(id=1)
        self.assertEqual(course.price, 100.00)