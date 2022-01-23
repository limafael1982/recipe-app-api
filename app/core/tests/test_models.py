from django.core.exceptions import ValidationError
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

    def test_incorrect_email_should_raise_an_error(self):
        """ Test if e-mail has the correct format """

        email = 'invalid_email_.'
        password = 'Test@123'
        with self.assertRaises(ValidationError):
            user = get_user_model().objects.create_user(
                email=email,
                password=password
            )
