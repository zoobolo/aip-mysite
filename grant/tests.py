from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
from .views import home


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

# class login(TestCase):
#     def login_view_status_code(self):
#         url = reverse('login')
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 302)

    def test_home_url_resolves_home_view(self):
        view = resolve('/home')
        self.assertEquals(view.func, home)

# Create your tests here.
