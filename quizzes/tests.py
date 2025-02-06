from django.test import TestCase
from .models import Question, Answer
from users.models import CustomUser
from .forms import QuestionForm, AnswerForm
from courses.models import Course, Lesson

class QuizTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(username='testuser', password='12345')
        cls.course = Course.objects.create(title='Test Course', instructor=cls.user, description='This is a test course.', price=100.00)
        cls.lesson = Lesson.objects.create(title='Test Lesson', course=cls.course)
        cls.question = Question.objects.create(course=cls.course, lesson=cls.lesson, text='What is the capital of France?')

    def test_question_creation(self):
        question = Question.objects.create(course=self.course, lesson=self.lesson, text='What is the capital of Germany?')
        self.assertEqual(question.text, 'What is the capital of Germany?')

    def test_answer_creation(self):
        answer = Answer.objects.create(question=self.question, text='Berlin', is_correct=True)
        self.assertEqual(answer.text, 'Berlin')
        self.assertTrue(answer.is_correct)

    # def test_quiz_detail_access(self):
    #     response = self.client.get(f'/quizzes/{self.lesson.pk}/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'What is the capital of France?')  # Update with actual expected content

    def test_question_form_validation(self):
        form_data = {'text': 'What is the capital of Spain?', 'course': self.course.id, 'lesson': self.lesson.id}
        form = QuestionForm(data=form_data, user=self.course.instructor)
        self.assertTrue(form.is_valid())

    def test_answer_form_validation(self):
        form_data = {'text': 'Madrid', 'is_correct': True, 'question': self.question.id}
        form = AnswerForm(data=form_data)
        self.assertTrue(form.is_valid())
