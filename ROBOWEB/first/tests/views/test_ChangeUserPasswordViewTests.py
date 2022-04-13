from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from ROBOWEB.adm.models import Phrase
from ROBOWEB.first.models import RoboUser, Profile, Images


class ChangeUserPasswordView(TestCase):
    UserModel = get_user_model()
    test_user_data = {
        "email": "deni@abv.bg",
        'password': "12345"
    }

    def __create_user(self):
        self.UserModel.objects.create_user(**self.test_user_data)

    def __create_profil_for_user(self, user):
        profile_data = {
            'first_name': "deni",
            'last_name': "Petrov",
            'user': user
        }
        new_profile = Profile.objects.create(
            first_name=profile_data['first_name'],
            last_name=profile_data['last_name'],
            user=profile_data['user'],
        )
        new_profile.save()

    def test_change_password__return_new_passs(self):
        self.__create_user()
        user = RoboUser.objects.first()
        old_pass=user.password
        self.__create_profil_for_user(user)
        new_phrasa = Phrase(phrase="hello")
        new_phrasa.save()
        self.client.login(**self.test_user_data)

        edit_first_name = {
            'old_password': '12345',
            'new_password1': '123',
            'new_password2': '123',
                          }

        response = self.client.post(
            reverse('change_password_page'),
            edit_first_name
        )
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertTrue(user.check_password('123'))
        self.assertNotEqual(old_pass, user.password)


