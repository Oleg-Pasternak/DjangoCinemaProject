from django.test import TestCase
from account.models import Profile
from django.contrib.auth.models import User


class TestProfile(TestCase):
    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(username='jacob',
                                             image='home/web/Downloads/poster-rick-and-morty.jpg',
                                             password='top_secret')
        self.first_name = "Jacob"
        self.last_name = "Smeeth"
        self.image = 'home/web/Downloads/poster-rick-and-morty.jpg'

    def test_profile_creation(self):
        object = Profile.objects.create(user=self.user,
                                        first_name=self.first_name,
                                        last_name=self.last_name,
                                        image=self.image)
        # check if object was created (if exists)
        self.assertTrue(object)
