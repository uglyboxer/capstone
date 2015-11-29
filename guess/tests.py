from django.core.urlresolvers import resolve
from django.test import TestCase, Client
from django.http import HttpRequest
from django.template.loader import render_to_string

from guess.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):

        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_post_request_resolves_to_results(self):
        c = Client()
        response = c.post('/data/', {'info': '2'})
        self.assertEqual(response.status_code, 302)
