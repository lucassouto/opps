#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model

from opps.channels.models import Channel
from opps.channels.forms import ChannelAdminForm


class ChannelFormTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(username=u'test', password='test')
        self.site = Site.objects.filter(name=u'example.com').get()
        self.parent = Channel.objects.create(name=u'Home', slug=u'home',
                                             description=u'home page',
                                             site=self.site, user=self.user)

    def test_init(self):
        """
        Test successful init without data
        """
        form = ChannelAdminForm(instance=self.parent)
        self.assertTrue(isinstance(form.instance, Channel))
        self.assertEqual(form.instance.pk, self.parent.pk)

