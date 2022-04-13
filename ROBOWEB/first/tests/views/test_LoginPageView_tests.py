from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse


class LoginPageViewTests(TestCase):
    UserModel = get_user_model()
    def test_register_user_redirect_login_page(self):
        user_data={
            "email":"deni@abv.bg",
            'password':"12345"
        }
        self.UserModel.objects.create_user(**user_data)
        self.client.login()
        response=self.client.get(reverse('first_page'))
        self.assertTemplateUsed(response,'first_page.html')
        # self.assertEqual(
        #     user_data['email']
        # )


    def test_non_register_user_raise_error(self):
        pass
        # user_data = {
        #     "email": "deni@abv.bg",
        #     'password': "12345"
        # }
        # #self.UserModel.objects.create_user(**user_data)
        # with self.assertRaises(Exception) as context:
        #     self.client.login()
        # self.assertIsNone(context.exception)
