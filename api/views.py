# Create your views here.
from rest_framework.generics import ListCreateAPIView

from accounts.models import User
from api.serializers.UserSerializer import UserSerializer


class UsersList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
