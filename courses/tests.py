from django.test import TestCase
from django.urls import reverse
from .models import Course, Lesson
from users.models import CustomUser

class CourseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(username='testuser', password='12345')
        cls.course = Course.objects.create(title='Test Course', instructor=cls.user, description='This is a test course.', price=100.00)

    def test_course_title(self):
        course = Course.objects.get(id=self.course.id)
        self.assertEqual(course.title, 'Test Course')

    def test_course_price(self):
        course = Course.objects.get(id=self.course.id)
        self.assertEqual(course.price, 100.00)

    def test_lesson_creation(self):
        lesson = Lesson.objects.create(title='Test Lesson', course=self.course)
        self.assertEqual(lesson.title, 'Test Lesson')
        self.assertEqual(lesson.course, self.course)

    def test_course_detail_access(self):
        response = self.client.get(f'/courses/{self.course.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test course.')  # Update with actual expected content

    def test_course_list_access(self):
        response = self.client.get(reverse('courses:course_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Course')  # Update with actual expected content
