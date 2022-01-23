from django.test import Client
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@ads.com',
            password='P@ssword123!'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='eu@ads.com',
            password='t123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """ Test if user are listed on the user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
