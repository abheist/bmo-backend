from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.models import Profile


class ProfileSerializer(CountryFieldMixin, ModelSerializer):

    class Meta:
        model = Profile
        fields = ['user', 'dob', 'gender', 'address1', 'address2', 'zip_code', 'city', 'country']
