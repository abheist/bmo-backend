from allauth.account.views import confirm_email
from django.conf.urls import url
from django.urls import path, include

from api.views import UsersList

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^verify-email/(?P<key>[\w@+-:]+)/$', confirm_email, name="account_confirm_email"),
    url(r'^users/$', UsersList.as_view(), name="users_list"),
]
