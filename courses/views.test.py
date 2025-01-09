from django.test import TestCase, Client
from django.urls import reverse
from courses.models import Course, Lesson
from courses.forms import LessonCreationForm

class TestAddLesson(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(title='Test Course', description='Test Description')

    def test_add_lesson_with_valid_data(self):
        # Create a form with valid data
        valid_data = {
            'title': 'Test Lesson',
            'description': 'Test Description',
            'video': 'test_video.mp4',
        }
        form = LessonCreationForm(data=valid_data)
        self.assertTrue(form.is_valid())

        # Submit the form
        response = self.client.post(reverse('courses:add_lesson', args=[self.course.pk]), valid_data)

        # Check if the lesson is added to the course
        self.assertEqual(response.status_code, 302)  # Redirect to course list
        self.assertEqual(Lesson.objects.count(), 1)
        self.assertEqual(Lesson.objects.first().course, self.course)