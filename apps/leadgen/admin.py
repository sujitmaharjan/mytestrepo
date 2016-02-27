# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from .models import Spider
from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken
from .models import *
class SpiderAdmin(admin.ModelAdmin):
    list_display = ('name','description','vertical','url','suggested_by','approved_by',)

    list_filter = ('vertical','suggested_by','approved_by')
    search_fields = ['name','description','url']



class VerticalAdmin(admin.ModelAdmin):
    list_display = ('name','description',)
    search_fields = ['name','description']


admin.site.register(Vertical,VerticalAdmin)
admin.site.register(Spider,SpiderAdmin)
admin.site.register(Account)
admin.site.register(Contact)
admin.site.register(CharField)
admin.site.register(IntegerField)
# from django.contrib import admin
# admin.site.unregister(SocialApp)
# admin.site.unregister(SocialAccount)
# admin.site.unregister(SocialToken)