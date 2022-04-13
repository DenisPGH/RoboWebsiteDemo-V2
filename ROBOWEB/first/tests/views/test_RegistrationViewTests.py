from django.test import TestCase
from django.urls import reverse

from ROBOWEB.first.models import Profile, RoboUser


class RegistrationViewTests(TestCase):
    pass

    # def test_success_registration(self):
    #     new_profil_data = {
    #                         'password1':'12345',
    #                         'password2':'12345',
    #                         'email':'deni@abv.bg',
    #                         'first_name': 'deni',
    #                        'last_name': 'New_name',
    #                        # 'access': 'True',
    #                        'born': '2020-3-4',
    #                        # 'picture': 'ddd',
    #                        # 'type_user': 'random',
    #                        'user': 'user'}
    #
    #     response=self.client.post(reverse('register_page'),data=new_profil_data)
    #     profile=Profile.objects.first()
    #     user=RoboUser.objects.first()
    #     self.assertEqual(1,len(RoboUser.objects.all()))
    #     self.assertEqual(1,len(Profile.objects.all()))
    #     self.assertEqual(new_profil_data['first_name'],profile.first_name)
    #     self.assertEqual(new_profil_data['email'],user.email)