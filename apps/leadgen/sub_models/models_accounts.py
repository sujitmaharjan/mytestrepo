# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from model_utils.models import TimeStampedModel
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from .models_spiders import Spider

@python_2_unicode_compatible
class CharField(TimeStampedModel):
    class Meta:
        app_label = "leadgen"

    # First Name and Last Name do not cover name patterns
    # around the globe.
    value = models.CharField(_("Value"), blank=False, max_length=255)
    source_url = models.CharField(_("Source Url"), blank=False, max_length=255)
    
    def __str__(self):
        return self.value

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

@python_2_unicode_compatible
class IntegerField(TimeStampedModel):
    class Meta:
        app_label = "leadgen"
    # First Name and Last Name do not cover name patterns
    # around the globe.
    value = models.IntegerField(_("Value"), blank=False)
    source_url = models.TextField(_("url"), blank=False, max_length=255)
    
    def __str__(self):
        return self.value

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
@python_2_unicode_compatible
class DefaultAccount(models.Model):
    class Meta:
        abstract = True
    spider = models.ForeignKey(Spider)
    name = models.ForeignKey(CharField, null=False, related_name="account_name")
    description = models.ForeignKey(CharField, null=True, related_name="account_description")
    website = models.ForeignKey(CharField, null=True, related_name="account_website")
    linkedin_url =models.ForeignKey(CharField, null=True, related_name="account_linkedin_url")
    street = models.ForeignKey(CharField, null=True, related_name="account_street")
    city = models.ForeignKey(CharField, null=True, related_name="account_city")
    zip_code = models.ForeignKey(CharField, null=True, related_name="account_zip_code")
    state = models.ForeignKey(CharField, null=True, related_name="account_state")
    province = models.ForeignKey(CharField, null=True, related_name="account_province")
    country = models.ForeignKey(CharField, null=True, related_name="account_country")
    membership_size = models.ForeignKey(CharField, null=True, related_name="account_membership_size")
    income =models.ForeignKey(CharField, null=True, related_name="account_income")
    expenditure = models.ForeignKey(CharField, null=True, related_name="account_expenditure")
    assets = models.ForeignKey(CharField, null=True, related_name="account_assets")
    liabilities = models.ForeignKey(CharField, null=True, related_name="account_liabilities")

@python_2_unicode_compatible
class EdTech(models.Model):
    class Meta:
        abstract = True
    grades = models.ForeignKey(CharField, null=True, related_name="account_grades")
    platforms = models.ForeignKey(CharField, null=True, related_name="account_platforms")
    price = models.ForeignKey(CharField, null=True, related_name="account_price")
    subjects = models.ForeignKey(CharField, null=True, related_name="account_subjects")
    rating = models.ForeignKey(CharField, null=True, related_name="account_rating")
    purpose = models.ForeignKey(CharField, null=True, related_name="account_purpose")
    skills = models.ForeignKey(CharField, null=True, related_name="account_skills")


class MultiCulture(models.Model):
    class Meta:
        abstract = True

    ethnicity = models.ForeignKey(CharField, null=True, related_name="account_ethinicity")
    
class SportsAssociation(models.Model):
    class Meta:
        abstract = True

    target_age_group = models.ForeignKey(CharField, null=True, related_name="account_target_age_group")
    related_associations = models.ForeignKey(CharField, null=True, related_name="account_related_associations")
    

@python_2_unicode_compatible
class Account(TimeStampedModel,DefaultAccount, EdTech, MultiCulture, SportsAssociation):
    class Meta:
        app_label = "leadgen"
    # First Name and Last Name do not cover name patterns
    # around the globe.
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
