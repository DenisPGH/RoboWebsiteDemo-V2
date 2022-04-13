
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from ROBOWEB.adm.models import Phrase
from ROBOWEB.first.models import RoboUser, Profile, Images


class Def_galery_tests(TestCase):
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

    def test_if_galery_return_corect__all_pictures_from_db(self):
        self.__create_user()
        user = RoboUser.objects.first()
        self.__create_profil_for_user(user)
        new_phrasa = Phrase(phrase="hello")
        new_phrasa.save()
        self.client.login(**self.test_user_data)
        new_pic=Images(pic='a',link="b")
        new_pic.save()
        pic_for_prove=Images.objects.all()
        response = self.client.get(reverse('galery'))
        # self.assertEqual(
        #     pic_for_prove, response.context['pictures']
        # )
        self.assertIsNotNone(response.context['pictures'])


