from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from ROBOWEB.adm.models import Phrase
from ROBOWEB.first.models import RoboUser, Profile, Images


class ProfilDetailsView(TestCase):
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

    def test_edit_some_field_store_in_profil_post(self):
        self.__create_user()
        user = RoboUser.objects.first()
        self.__create_profil_for_user(user)
        new_phrasa = Phrase(phrase="hello")
        new_phrasa.save()
        self.client.login(**self.test_user_data)

        profile = Profile.objects.first()
        self.assertEqual("deni", profile.first_name)
        edit_first_name = {'first_name': 'deni',
                           'last_name':'New_name',
                           'access': 'True',
                           'born': '2020-3-4',
                           'picture': 'ddd',
                           'type_user':'random',
                           'user':'user' }

        response = self.client.post(
                    reverse('edit_profil_page',kwargs={'pk': profile.pk}),
                    edit_first_name
                    )
        self.assertEqual(response.status_code, 302)
        profile.refresh_from_db()
        self.assertEqual(False, profile.access)
        self.assertEqual( 'New_name',profile.last_name)
        self.assertIsNotNone(profile.picture)


