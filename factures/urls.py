from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/edit$', ProfileUpdate.as_view(), name="profile-update"),
    url(r'^(?P<slug>[\w-]+)$', ProfileDetailView.as_view(), name="profile-detail"),
    url(r'^(?P<slug>[\w-]+)/archives/$', DevisListView.as_view(), name="devis-list"),
]
