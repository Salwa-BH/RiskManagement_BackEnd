from django.db import models
from django.conf import settings 
from treebeard.mp_tree import MP_Node

class DataLog(models.Model):
    # level = models.DecimalField(max_digits=1, decimal_places=0, null=False)
    # timestamp = models.CharField(max_length=300, blank=True, null=True)
    # fileName = models.CharField(max_length=300, blank=True, null=True)
    # lineNumber = models.CharField(max_length=300, blank=True, null=True)
    # message = models.CharField(max_length=3000, blank=True, null=True)

    name = models.CharField(max_length=300, blank=True, null=True)
    headers = models.CharField(max_length=3000, blank=True, null=True)
    status = models.DecimalField(max_digits=3, decimal_places=0, null=False)
    statusText = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=3000, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.message




#----------------------------Role

class Role(MP_Node):
    name = models.CharField(max_length=100,blank=False,null=False, unique=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.name

#----------------------------Profile

class Profile(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False, unique=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

#----------------------------Group

class Group(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False, unique=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

#----------------------------Assign users to group,role, profile

class UserAssign(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=False,null=False)
    role_id = models.ForeignKey(Role,on_delete=models.CASCADE,blank=True,null=True)
    profile_id = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    group_id = models.ForeignKey(Group,on_delete=models.CASCADE,blank=True,null=True)

#----------------------------Website Structure with only one table 

class WebsiteStructure(models.Model):
    TYPE_CHOICES = (
        ("Dashboard","Dashboard"),
        ("Process", "Process"),
        ("Risk", "Risk"),
        ("Setting", "Setting"),
    )

    structure = models.CharField(max_length=50, choices=TYPE_CHOICES, blank=False, null=False)
    sub_structure = models.CharField(max_length=50,blank=False,null=False)
    def __str__(self):
        return self.structure+" - " + self.sub_structure

#----------------------------Permissions

class Permissions(models.Model):
    profile_id = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=False,null=False)
    structure_id = models.ForeignKey(WebsiteStructure,on_delete=models.CASCADE,blank=False,null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    read = models.BooleanField(default=False)
    create = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
    erase = models.BooleanField(default=False)  
    
