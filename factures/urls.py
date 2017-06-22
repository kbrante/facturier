from django.conf.urls import url
from .views import ProfileDetailView,ProfileUpdate

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/edit$', ProfileUpdate.as_view(), name="profile-update"),
    url(r'^(?P<slug>[\w-]+)', ProfileDetailView.as_view(), name="profile-detail"),
]
