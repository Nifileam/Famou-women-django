from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from famouswomen.models import FamousWomen


class GetPagesTestCase(TestCase):
    fixtures = ['famouswomen_famouswomen.json', 'famouswomen_category.json', 'famouswomen_tagpost.json']

    def test_homepage(self):
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'famouswomen/index.html')
        self.assertEqual(response.context_data['title'], 'Famous Women')

    def test_redirect_addpage(self):
        path = reverse('add_page')
        redirect_url = reverse('users:login') + f'?next={path}'
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, redirect_url)

    def test_data_mainpage(self):
        w = FamousWomen.published.all().select_related('cat')
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(list(response.context['posts']), list(w[:3]))

    def test_paginate_mainpage(self):
        path = reverse('home')
        page = 2
        paginate_by = 3
        response = self.client.get(path + f'?page={page}')
        w = FamousWomen.published.all().select_related('cat')
        self.assertEqual(list(response.context['posts']), list(w[(page - 1) * paginate_by:page * paginate_by]))

    def test_content_post(self):
        w = FamousWomen.published.get(pk=1)
        path = reverse('show_post', args=[w.slug])
        response = self.client.get(path)
        self.assertEqual(w.content, response.context['info'].content)