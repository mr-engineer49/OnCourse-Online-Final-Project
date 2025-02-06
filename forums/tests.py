from django.test import TestCase
from django.urls import reverse  # Import reverse function
from .models import Forum
from courses.models import Course
from users.models import CustomUser  # Import CustomUser model

class ForumModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(username='testuser', password='12345')
        cls.course = Course.objects.create(title='Test Course', instructor=cls.user, description='This is a test course.', price=100.00)
        cls.forum = Forum.objects.create(name='Test Forum', course=cls.course)

    def test_forum_name(self):
        forum = Forum.objects.get(id=self.forum.id)
        self.assertEqual(forum.name, 'Test Forum')

    # def test_forum_detail_access(self):
    #     response = self.client.get(f'/forums/{self.forum.id}/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'This is a test forum.')  # Update with actual expected content

    def test_forum_list_access(self):
        response = self.client.get(reverse('forums:forum_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Forum')  # Update with actual expected content
