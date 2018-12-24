# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.conf import settings

class IndexViewTestCase(TestCase):

  def setUp(self):
    self.client = Client()
    self.url = reverse('index')

  def tearDown(self):
    pass

  def test_status_code(self):
    response = self.client.get(self.url)
    self.assertEquals(response.status_code, 200)

  def test_template_used(self):
    response = self.client.get(self.url)
    self.assertTemplateUsed(response, 'index.html')

class ContactViewTestCase(TestCase):

  def setUp(self):
    self.client = Client()
    self.url = reverse('contact')

  def test_view_sucess(self):
    response = self.client.get(self.url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'contact.html')

  def test_form_submit_fail(self):
    data = {'name': '', 'message': '', 'email': ''}
    response = self.client.post(self.url, data)
    self.assertFormError(response, 'form', 'name', 'This field is required.')
    self.assertFormError(response, 'form', 'email', 'This field is required.')
    self.assertFormError(response, 'form', 'message', 'This field is required.')

  def test_form_submit_success(self):
    data = {'name': 'test', 'message': 'test', 'email': 'test@test.com'}
    response = self.client.post(self.url, data)
    self.assertTrue(response.context['success'])
    self.assertEquals(len(mail.outbox), 1)
    self.assertEquals(mail.outbox[0].subject, 'Contato do Django E-Commerce')
