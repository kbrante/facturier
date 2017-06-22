# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Profile
from django.views.generic.edit import UpdateView


class ProfileDetailView(DetailView):
    model = Profile
    slug_field = "user__username"

class ProfileUpdate(UpdateView):
    model = Profile
    slug_field = "user__username"
    fields = ['address', 'zip_Code', 'city', 'website', 'contact_Email', 'avatar']
    
    def get_success_url(self):
        return reverse('profile-detail', kwargs={'slug' : self.object.user.username})
