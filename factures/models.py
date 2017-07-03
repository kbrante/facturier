# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from parler.models import TranslatableModel, TranslatedFields

class Profile(TranslatableModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("user"))
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("adresse"))
    zip_Code = models.CharField(max_length=5, null=True, blank=True, verbose_name=_("code postal"))
    city = models.CharField(max_length=75, null=True, blank=True, verbose_name=_("ville"))
    website = models.CharField(max_length=150, null=True, blank=True, verbose_name=_("site web"))
    contact_Email = models.EmailField(max_length=150, null=True, blank=True, verbose_name=_("email contact"))
    avatar = models.ImageField(null=True, blank=True, verbose_name=_("avatar"))
    translation = TranslatedFields(
        bio = models.TextField( max_length=1000, verbose_name=_("Bio"))
    )
    def __unicode__(self):
        return self.user.username

class Client(models.Model):
    clientname = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("nom client"))
    clientaddress = models.CharField(max_length=100,null=True, blank=True, verbose_name=_("adresse client"))
    clientzipcode = models.CharField(max_length=5,null=True, blank=True, verbose_name=_("code postal client"))

    def __unicode__(self):
        return self.clientname


class Status(models.Model):
    status = models.CharField(max_length=100)

    def __unicode__(self):
        return self.status

    class Meta:
        verbose_name_plural=_("statuses")

class Proposition(models.Model):
    dealer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    proposition = models.CharField(max_length=150, blank=True, null=True)

    def __unicode__(self):
        return self.proposition+" "+str(self.id)



class Ligne(models.Model):
    service_name = models.CharField(max_length=200)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.SmallIntegerField()
    proposal = models.ForeignKey(Proposition, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.service_name
