# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Profile
from django.views.generic.edit import UpdateView
# Create your views here.


class ProfileDetailView(DetailView):
    model = Profile
    slug_field = "user__username"

class ProfileUpdate(UpdateView):
    model = Profile
    slug_field = "user__username"
    fields = ['address', 'zip_Code', 'city', 'website', 'contact_Email', 'avatar', 'skills', 'interests']
