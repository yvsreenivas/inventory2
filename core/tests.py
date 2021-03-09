from django.test import TestCase
from django.contrib.auth.models import User


class ModelTest(TestCase):

    @classmethod
    def setUpClass(cls):

        super(ModelTest, cls).setUpClass()

        user = User(username='tom', password='tom')
        user.save()

    def test_user_models(self):
        user = User.objects.get(username='tom')
        print('Added user data : ')
        print(user)
        print('')
        self.assertEqual(user.username, 'tom')
