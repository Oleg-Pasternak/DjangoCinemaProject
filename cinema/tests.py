from django.test import TestCase
from account.models import Profile
from django.contrib.auth.models import User


class TestProfile(TestCase):
    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(username='jacob',
                                             email='test@example.com',
                                             password='top_secret')
        self.first_name = "Jacob"
        self.last_name = "Smeeth"

    def test_profile_creation(self):
        object = Profile.objects.create(user=self.user,
                                        first_name=self.first_name,
                                        last_name=self.last_name)
        # check if object was created (if exists)
        self.assertTrue(object)
