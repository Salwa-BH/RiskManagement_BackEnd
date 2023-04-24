import django_filters
from .models import Role
from .models import Profile
from .models import Group
from .models import UserAssign
from .models import Permissions
from .models import WebsiteStructure
from .models import DataLog

#----------------------------Data log

class DataLogFilter(django_filters.FilterSet):
    class Meta: 
        model = DataLog
        #fields = ( 'level','timestamp', 'fileName', 'lineNumber','message')
        fields = ('name','headers','status','statusText','message','url','email','timestamp')

#----------------------------ROLE

class RoleFilter(django_filters.FilterSet):
    class Meta:
        model = Role
        fields=('name','description', 'confirmation')

#---------------------------- PROFILE

class ProfileFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields=('name','description',)

#---------------------------- GROUP

class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields=('name','description',)

#---------------------------- USER ASSIGN

class UserAssignFilter(django_filters.FilterSet):
    class Meta:
        model = UserAssign
        fields=('user_id', 'role_id','profile_id','group_id')
#----------------------------WEBSITE STRUCTURE WITH ONE TABLE

class WebsiteStructureFilter(django_filters.FilterSet):
    class Meta:
        model = WebsiteStructure
        fields=('structure','sub_structure',)


#----------------------------PERMISSIONS

class PermissionsFilter(django_filters.FilterSet):
    class Meta:
        model = Permissions
        fields= ('profile_id', 'structure_id','description','read', 'create', 'edit','erase')

