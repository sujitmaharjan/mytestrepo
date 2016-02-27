# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

@python_2_unicode_compatible
class Contact(TimeStampedModel):
    class Meta:
        app_label = "leadgen"

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Spider Name"), blank=True, max_length=255)
    description = models.TextField(_("Spider Name"), blank=True, max_length=255)
    url = models.CharField(_("Main URL of the spider"), blank=False, max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
