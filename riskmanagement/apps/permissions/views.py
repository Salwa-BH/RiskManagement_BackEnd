from django.shortcuts import render
from rest_framework import serializers
from rest_framework import filters
from rest_framework import viewsets

from .forms import RoleFilter
from .forms import ProfileFilter
from .forms import GroupFilter, UserAssignFilter
#from .forms import StructureWebsiteFilter, SubStructureFilter
from .forms import WebsiteStructureFilter
from .forms import PermissionsFilter

from .serializers import RoleSerializer
from .serializers import ProfileSerializer
from .serializers import GroupSerializer, UserAssignSerializer
#from .serializers import StructureWebsiteSerializer, SubStructureSerializer
from .serializers import WebsiteStructureSerializer
from .serializers import PermissionsSerializer

from .models import Role
from .models import Profile
from .models import Group
from .models import UserAssign
#from .models import StructureWebsite, SubStructure
from .models import Permissions
from .models import WebsiteStructure

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import action
from django.core import serializers
from rest_framework import filters

from rest_framework import viewsets, authentication, permissions, filters, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import DataLog
from .forms import DataLogFilter
from .serializers import DataLogSerializer

#---------------------------- Data Log 

class DataLogViewSet(viewsets.ModelViewSet):
    queryset = DataLog.objects.all()
    serializer_class = DataLogSerializer
    filter_class = DataLogFilter
    #search_fields =  ( 'level','timestamp', 'fileName', 'lineNumber','message')
    search_fields =  ('name','headers','status','statusText','message','url','email','timestamp')

#----------------------------Role 

class RoleViewSet(viewsets.ModelViewSet):

    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_class = RoleFilter
    search_fields = ('name','description')
    ordering_fields = ('name')

    @action(detail=True, methods=['POST'])
    def add_child(self, request, pk=None):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            response = serializer.create(validated_data, pk)
            return Response(response)

    # Change a process's type parent
    @action(detail=True, methods=['patch'])
    def change_parent(self, request, pk=True):
        role = Role.objects.get(pk=pk)

        response = request.data
        data = request.data
        if 'parent' in data:
            newParentPk = data['parent']
            if(newParentPk == 0):
                role.move(role.get_root())
                role.refresh_from_db()
            elif(newParentPk > 0):
                newParent = Role.objects.get(pk=newParentPk)
                role.move(newParent, 'first-child')
                role.refresh_from_db()
        return Response(response)

    @action(detail=False, methods=['GET'])
    def get_tree(self, request, pk=None):
        return Response(Role.dump_bulk())



#----------------------------Profile

class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_class = ProfileFilter
    search_fields = ('name','description',)
    ordering_fields = ('name')

#----------------------------Group 

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_class = GroupFilter
    search_fields = ('name','description',)
    ordering_fields = ('name')

#----------------------------User Assign

class UserAssignViewSet(viewsets.ModelViewSet):
    
    queryset = UserAssign.objects.all()
    serializer_class = UserAssignSerializer
    filter_class = UserAssignFilter
    search_fields = ('user_id','role_id','profile_id','group_id')
    ordering_fields = ('user_id')

#---------------------------- Webstructure

class WebsiteStructureViewSet(viewsets.ModelViewSet):

    queryset = WebsiteStructure.objects.all()
    serializer_class = WebsiteStructureSerializer
    filter_class = WebsiteStructureFilter
    search_fields = ('structure','sub_structure','description',)
    ordering_fields = ('structure','sub_structure')

#----------------------------Permissions

class PermissionsViewSet(viewsets.ModelViewSet):

    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer
    filter_class = PermissionsFilter
    search_fields = ('profile_id', 'structure_id','read', 'create', 'edit','erase')
    ordering_fields = ('profile_id', 'structure_id','read', 'create', 'edit','erase')