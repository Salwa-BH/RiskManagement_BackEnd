from rest_framework import serializers
from .models import Role 
from .models import Profile
from .models import Group
from .models import UserAssign
from .models import Permissions
from .models import WebsiteStructure
from .models import DataLog

#----------------------------Data log

class DataLogSerializer(serializers.ModelSerializer):
    class Meta: 
        model = DataLog
        #fields = ( 'level','timestamp', 'fileName', 'lineNumber','message')
        fields = ('name','headers','status','statusText','message','url','email','timestamp')

#---------------------------- Role

# class RoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Role
#         fields = ('id', 'name','description',)

class RoleSerializer(serializers.ModelSerializer):
    """Class serializer for the Activity model"""

    parents = serializers.SerializerMethodField('get_parents')
    children = serializers.SerializerMethodField('get_children')
    depth = serializers.SerializerMethodField('get_depth')

    class Meta:
        model = Role
        fields = ('id', 'name','description', 'confirmation', 'parents','children', "depth")

    def create(self, validated_data, pk=None):
        if pk is None:
            return Role.add_root(**validated_data)
        else:
            if validated_data:
                parent = Role.objects.get(pk=pk)
                parent.add_child(
                    **validated_data)
                return {**validated_data}

    def get_children(self, obj):
        return [
            {'id': role.id,
             'name': role.name}
            for role in obj.get_children()
        ]
    def get_parents(self, obj):
        return [
            {
                'id': role.id,
                'name': role.name
            }
            for role in obj.get_ancestors()
        ]

    def get_depth(self, obj):
        return obj.depth


#---------------------------- Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name','description',)


#---------------------------- Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name','description',)

#---------------------------- UserAssign 

class UserAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAssign
        fields = ('id', 'user_id', 'role_id','profile_id','group_id')

#---------------------------- Webstructure

class WebsiteStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteStructure
        fields = ('id', 'structure','sub_structure')

#---------------------------- Permissions 

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = ('id','profile_id', 'structure_id','description','read', 'create', 'edit','erase')