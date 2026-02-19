from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from quickstart.serializers import GroupSerializer, UserSerializer

# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    #API endpoint that allow user to be viewed or edited.
    
    queryset = User.objects.all() #Date_Joined
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewset(viewsets.ModelViewSet):
    #API endpoint that allow groups to be viewed or edited.
    
    queryset = Group.objects.all()   #Date_Joined
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]    