import django_filters
from .models import Process, ProcessType, Player, ProcessPlayer ,StatusProcess
from .models import IOElement, ProcessIO
from .models import CompanySite


class CompanySiteFilter(django_filters.FilterSet):

    class Meta:
        model = CompanySite
        fields = ('is_default',)


class ProcessFilter(django_filters.FilterSet):

    class Meta:
        model = Process
        fields = ('title', 'description', 'process_type',
                  'depth', 'company_site')


class ProcessTypeFilter(django_filters.FilterSet):

    class Meta:
        model = ProcessType
        fields = ('name', 'is_default',)


class PlayerFilter(django_filters.FilterSet):

    class Meta:
        model = Player
        fields = ('short_name', 'long_name',)


class ProcessPlayerFilter(django_filters.FilterSet):
    class Meta:
        model = ProcessPlayer
        fields = ['process', 'playerRole', 'player']


class IOElementFilter(django_filters.FilterSet):

    class Meta:
        model = IOElement
        fields = ('name', 'description')


class ProcessIOFilter(django_filters.FilterSet):
    class Meta:
        model = ProcessIO
        fields = ['process']

class StatusProcessFilter(django_filters.FilterSet):

    class Meta:
        model = StatusProcess
        fields = ('id',)
