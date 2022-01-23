from django.contrib.auth.password_validation import password_changed
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_user_create_user_with_email_with_success(self):
        """Tests if a user can be created successfuly"""

        email = 'teEt@hotmaiL.com'
        password = 'Test@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))