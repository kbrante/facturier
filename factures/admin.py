# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from parler.admin import TranslatableStackedInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class ProfileInline(TranslatableStackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class ServiceInline(admin.TabularInline):
    model = Service
    verbose_name = "Services"
    can_delete = True
class ProposalAdmin(admin.ModelAdmin):
    inlines = (ServiceInline,)
admin.site.register(Profile)
admin.site.register(Status)
admin.site.register(Proposal,ProposalAdmin)
