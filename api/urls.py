from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]
