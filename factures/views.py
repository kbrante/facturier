# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import *
# from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView


class ProfileDetailView(DetailView):
    model = Profile
    slug_field = "user__username"

class ProfileUpdate(UpdateView):
    model = Profile
    slug_field = "user__username"
    fields = "__all__"

    def get_success_url(self):
        return reverse('profile-detail', kwargs={'slug' : self.object.user.username})

# @login_required
class DevisListView(ListView):
    model = Proposition
    context_object_name = "devis"
    template_name = "factures/devis_list.html"
