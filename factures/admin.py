# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class ServiceInline(admin.TabularInline):
    model = Service
    verbose_name = "Services"
    can_delete = True
class ProposalAdmin(admin.ModelAdmin):
    inlines = (ServiceInline,)
admin.site.register(Profile)
admin.site.register(Status)
admin.site.register(Proposal,ProposalAdmin)
