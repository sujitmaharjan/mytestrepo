# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from model_utils.models import TimeStampedModel
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class Vertical(TimeStampedModel):
    class Meta:
        app_label = "leadgen"

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name"), blank=True, max_length=255)
    description = models.TextField(_("Description"), blank=True, max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
