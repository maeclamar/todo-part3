from django.urls import resolve
from django.test import TestCase
from blogs.views import index, detail, signup

from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.
class UrlResolveTest(TestCase):
    def test_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_url_resolves_to_detail_view(self):
        found = resolve('/detail/3/')
        self.assertEqual(found.func, detail)

    def test_url_resolves_to_signup_view(self):
        found = resolve('/signup/')


class HtmlTest(TestCase):
    def test_index_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        expected_html = render_to_string('blogs/index.html', {'blogs': []})
        self.assertEqual(response.content.decode(), expected_html)
