from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from accounts.models import User, Profile
from api.serializers.ProfileSerializer import ProfileSerializer
from api.serializers.UserSerializer import UserSerializer


class UserList(ListCreateAPIView):
    def get_queryset(self):
        # todo: list should go acc. to user type
        return User.objects.all()

    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileDetail(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user'
