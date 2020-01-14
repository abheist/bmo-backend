from allauth.account.views import confirm_email
from django.conf.urls import url
from django.urls import path, include

from api.views import UserList, UserDetail, ProfileDetail

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^verify-email/(?P<key>[\w@+-:]+)/$', confirm_email, name="account_confirm_email"),
    url(r'^user/$', UserList.as_view(), name="users_list"),
    url(r'^user/(?P<pk>[\w]+)/$', UserDetail.as_view(), name="user_detail"),
    url(r'^profile/(?P<user>[\w]+)/$', ProfileDetail.as_view(), name="profile_detail"),
]
