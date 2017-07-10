# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, redirect
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import *
# from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from .form import *


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

    def get_queryset(self):
        qs = Proposition.objects.filter(dealer = self.request.user)
        return qs

class DevisCreateView(CreateView):
    model = Proposition
    fields = "__all__"
    template_name = "factures/devis_create.html"

    def get_context_data(self):
        context = CreateView.get_context_data(self)
        context["sous_form"] = form_ligne()
        return context

    def get_success_url(self):
        return reverse('devis-list', kwargs={'slug': self.request.user.username})

class DevisDetailView(DetailView):
    model = Proposition
    pk_field = "id"
    context_object_name = "propositions"
    template_name = "factures/devis_detail.html"

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self)
        context["detail_lignes"] = Ligne.objects.filter(proposal = self.object)
        return context

def UpdateStatus(request, pk):
    proposition = Proposition.objects.get(id=pk)
    pending = Status.objects.get(id=5)
    waiting = Status.objects.get(id=2)
    paid = Status.objects.get(id=3)
    if proposition.status == pending:
        proposition.status = waiting
    elif proposition.status == waiting:
        proposition.status = paid

    proposition.save()
    return redirect('devis-detail',slug = request.user.username, pk=pk)

def ArchiveDevis(request, pk):
    proposition = Proposition.objects.get(id=pk)
    pending = Status.objects.get(id=5)
    aborted = Status.objects.get(id=4)
    archived = Status.objects.get(id=1)

    if proposition.status == pending:
        proposition.status = aborted
    elif proposition.status == aborted:
        proposition.status = archived

    proposition.save()
    return redirect('devis-detail', slug= request.user.username, pk=pk)
