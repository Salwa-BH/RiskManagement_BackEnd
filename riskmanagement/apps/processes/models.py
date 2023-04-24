from django.db import models
from django.utils.translation import ugettext as _
from treebeard.mp_tree import MP_Node



class CompanySite(models.Model):

    name = models.CharField(max_length=300, blank=False, null=False)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProcessType(MP_Node):

    name = models.CharField(max_length=100, blank=False, null=False)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Process(MP_Node):

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=2000, blank=True, null=True)
    aim = models.TextField(max_length=2000, blank=True, null=True)
    status = models.TextField(
        max_length=30, blank=False, null=False, default="Empty")
    process_type = models.ForeignKey(
        ProcessType, on_delete=models.CASCADE, blank=False, null=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    financial_level_1=models.IntegerField(blank=True, null=True)
    financial_level_2=models.IntegerField(blank=True, null=True)
    financial_level_3=models.IntegerField(blank=True, null=True)
    financial_level_4=models.IntegerField(blank=True, null=True)
    financial_level_5=models.IntegerField(blank=True, null=True)
    company_site = models.ForeignKey(
        CompanySite, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        msg = self.title
        if self.description:
            msg += _(': %s' % self.description)
        return msg


class Player(MP_Node):

    short_name = models.CharField(max_length=30, blank=False, null=False)
    long_name = models.CharField(max_length=100, blank=False, null=False)
    nature = models.CharField(max_length=30, blank=False,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        msg = self.short_name + ' ' + self.long_name
        return msg


class ProcessPlayer(models.Model):

    process = models.ForeignKey(Process, on_delete=models.CASCADE,
                                blank=False, null=False)
    player = models.ForeignKey(Player, on_delete=models.CASCADE,
                               blank=False, null=False)
    playerRole = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        msg = f"{self.process.title} : {self.player} : {self.playerRole}"
        return msg


class IOElement(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        msg = self.name
        if self.description:
            msg += _(': %s' % self.description)
        return msg


class ProcessIO(models.Model):

    process = models.ForeignKey(Process, on_delete=models.CASCADE,
                                blank=False, null=False)
    io_element = models.ForeignKey(IOElement, on_delete=models.CASCADE,
                                   blank=False, null=False)
    io_type = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        msg = f"{self.process.title} : {self.io_element} : {self.io_type}"
        return msg


class StatusProcess(models.Model):
   name=models.CharField(max_length=1000, blank=True, null=False)