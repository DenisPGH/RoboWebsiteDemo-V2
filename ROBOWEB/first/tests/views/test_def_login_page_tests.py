from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from ROBOWEB.adm.models import Phrase
from ROBOWEB.first.models import RoboUser, Profile


class Def_login_page_tests(TestCase):
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



    def test_login_page__correct_context_value(self):
        self.__create_user()
        user=RoboUser.objects.first()
        self.__create_profil_for_user(user)
        new_phrasa=Phrase(phrase="hello")
        new_phrasa.save()
        self.client.login(**self.test_user_data)

        profile = Profile.objects.first()
        self.assertEqual(profile.pk, user.id)
        response = self.client.get(reverse('login_page'))
        self.assertTemplateUsed(response,'login_page.html')
        self.assertEqual(
            profile,response.context['current_user']
        )
        self.assertEqual(
            'hello', response.context['to_write']
        )

    def test_correct_take_post_form_shoud__store_in_DB_(self):
        self.__create_user()
        user = RoboUser.objects.first()
        self.__create_profil_for_user(user)
        new_phrasa = Phrase(phrase="hello")
        new_phrasa.save()
        new_phrasa_2 = Phrase(phrase="hello")
        new_phrasa_2.save()
        self.client.login(**self.test_user_data)

        add_phrasa_data={'phrase':"Denis"}
        self.client.post(reverse('login_page'),data=add_phrasa_data)
        first_phrasa_in_db=Phrase.objects.order_by('-id').first()
        self.assertEqual(add_phrasa_data['phrase'],first_phrasa_in_db.phrase)

    def test_access_status_logged_person(self):
        self.__create_user()
        user = RoboUser.objects.first()
        self.__create_profil_for_user(user)
        new_phrasa = Phrase(phrase="hello")
        new_phrasa.save()
        new_phrasa_2 = Phrase(phrase="hello")
        new_phrasa_2.save()
        self.client.login(**self.test_user_data)
        profile = Profile.objects.first()
        self.assertEqual(False, profile.access)





