from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from courses.models import Course, Lesson
from users.models import User, UserRoles


class CourseTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='tester@test1.com',
            role=UserRoles.MODERATOR,
            is_active=True,
            is_superuser=True,
            is_staff=True
        )
        self.user.set_password('qwerty')
        self.user.save()
        response = self.client.post('/users/token/', {"email": "tester@test1.com", "password": "qwerty"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_course_create(self):
        """Course creation test"""
        data = {
            'title': 'test_course_create',
            'description': 'test_course_create_description',
        }
        response = self.client.post('/courses/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            'id': 1,
            'lessons': [],
            'lessons_number': 0,
            'title': 'test_course_create',
            'preview': None,
            'description': 'test_course_create_description',
            'owner': None
        })

    def test_course_list(self):
        Course.objects.create(
            title='test_course_list',
            description='test_course_list_description',
        )
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.all().count(), 1)
        self.assertEqual(response.json(),
                         {'count': 1,
                          'next': None,
                          'previous': None,
                          'results': [
                              {'id': 4,
                               'lessons': [],
                               'lessons_number': 0,
                               'title': 'test_course_list',
                               'preview': None,
                               'description': 'test_course_list_description',
                               'owner': None}]}
                         )

    def test_course_get(self):
        Course.objects.create(
            title='test_course_detail',
            description='test_course_list_detail_description',
        )
        response = self.client.get('/courses/3/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'id': 3,
            'lessons': [],
            'lessons_number': 0,
            'title': 'test_course_detail',
            'preview': None,
            'description': 'test_course_list_detail_description',
            'owner': None
        })

    def test_course_delete(self):
        Course.objects.create(
            title='test_course_delete',
            description='test_course_list_delete_description',
        )
        response = self.client.delete('/courses/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='tester@test1.com',
            role=UserRoles.MEMBER,
            is_active=True,
            is_superuser=False,
            is_staff=False
        )
        self.user.set_password('qwerty')
        self.user.save()
        response = self.client.post('/users/token/', {"email": "tester@test1.com", "password": "qwerty"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.course = Course.objects.create(
            title='test_course_for_lesson',
            description='test_course_for_lesson_description',
        )
        self.lesson = Lesson.objects.create(
            course=self.course,
            title='test_lesson',
            description='test_lesson_description',
            owner=self.user
        )

    def test_lesson_list(self):
        response = self.client.get('/lessons/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'count': 1,
                          'next': None,
                          'previous': None,
                          'results': [
                              {'title': 'test_lesson',
                               'course': 'test_course_for_lesson',
                               'owner': 'tester@test1.com'}
                          ]})

    def test_lesson_get(self):
        response_get = self.client.get('/lesson/3/')
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)

    def test_lesson_update(self):
        response_patch = self.client.patch('/lesson/5/update/', {"title": "test_lesson_patch"})
        self.assertEqual(response_patch.status_code, status.HTTP_200_OK)
        print(response_patch.json())
        self.assertEqual(response_patch.json(),
                         {'id': 5, 'title': 'test_lesson_patch', 'description': 'test_lesson_description',
                          'preview': None, 'video_url': None, 'course': 4, 'owner': 4})
        response_put = self.client.patch('/lesson/5/update/', {"title": "test_lesson_put"})
        self.assertEqual(response_put.status_code, status.HTTP_200_OK)
        print(response_put.json())
        self.assertEqual(response_put.json(),
                         {'id': 5, 'title': 'test_lesson_put', 'description': 'test_lesson_description',
                          'preview': None, 'video_url': None, 'course': 4, 'owner': 4})

    def test_lesson_create(self):
        data = {
            'course': self.course.id,
            'title': 'test_lesson_create',
            'description': 'test_lesson_create_description',
            'owner': self.user.id
        }
        response = self.client.post('/lesson/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_bad = self.client.post('/lesson/create/', {
            'course': self.course.id,
            'title': 'test_lesson_create',
            'description': 'test_lesson_create_description',
            'video_url': 'mail.ru',
            'owner': self.user.id
        })
        self.assertEqual(response_bad.status_code, status.HTTP_400_BAD_REQUEST)
