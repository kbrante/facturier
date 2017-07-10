from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/edit$', ProfileUpdate.as_view(), name="profile-update"),
    url(r'^(?P<slug>[\w-]+)$', ProfileDetailView.as_view(), name="profile-detail"),
    url(r'^(?P<slug>[\w-]+)/archives/$', DevisListView.as_view(), name="devis-list"),
    url(r'^(?P<slug>[\w-]+)/create/$', DevisCreateView.as_view(), name="devis-create"),
    url(r'^(?P<slug>[\w-]+)/archives/(?P<pk>\d+)/$', DevisDetailView.as_view(), name="devis-detail"),
    url(r'^(?P<pk>\d+)/update/$', UpdateStatus, name="update-status"),
    url(r'^(?P<pk>\d+)/archived/$', ArchiveDevis, name="archived-status"),
]
