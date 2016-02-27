# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from leadgen_viewer.users.models import User
from model_utils.models import TimeStampedModel
from .models_verticals import Vertical
@python_2_unicode_compatible
class Spider(TimeStampedModel):
    '''Data model for the spider'''
    class Meta:
        app_label = "leadgen"

    name = models.CharField(_("Name"), blank=False, max_length=255)
    description = models.TextField(_("Description"), blank=True, max_length=255)
    url = models.CharField(_("Base URL of the spider"), blank=False, null=False, max_length=255)
    vertical = models.ForeignKey(Vertical,null=False,related_name="spiders")
    suggested_by = models.ForeignKey(User, null=False,related_name="suggested_spiders")
    approved_by = models.ForeignKey(User,null=True,blank=True,related_name="approved_spiders")
    assigned_to = models.ForeignKey(User,null=True,blank=True,related_name="assigned_spiders")
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
