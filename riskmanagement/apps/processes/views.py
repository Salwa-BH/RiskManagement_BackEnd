from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework import filters
from rest_framework import viewsets, authentication, permissions, filters, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .forms import PlayerFilter, IOElementFilter, ProcessPlayerFilter,StatusProcessFilter
from .forms import ProcessFilter, ProcessTypeFilter, ProcessIOFilter
from .forms import CompanySiteFilter

from .models import Process, ProcessType, ProcessPlayer,StatusProcess
from .models import Player, IOElement, ProcessIO
from .models import CompanySite

from .serializers import ProcessSerializer, ProcessTypeSerializer
from .serializers import PlayerSerializer, ProcessPlayerSerializer
from .serializers import IOElementSerializer, ProcessIOSerializer,StatusProcessSerializer
from .serializers import CompanySiteSerializer



from .services import ProcessService
from .utils import update_process_tree_types


class DefaultMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""

    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )


class CompanySiteViewSet(DefaultMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating domains."""

    queryset = CompanySite.objects.all()
    serializer_class = CompanySiteSerializer
    filter_class = CompanySiteFilter
    search_fields = ('name',)
    ordering_fields = ('name',)


class ProcessTypeViewSet(DefaultMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating domains."""

    queryset = ProcessType.objects.all()
    serializer_class = ProcessTypeSerializer
    filter_class = ProcessTypeFilter
    search_fields = ('name',)
    ordering_fields = ('name',)

    @action(detail=True, methods=['POST'])
    def add_child(self, request, pk=None):
        serializer = ProcessTypeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            response = serializer.create(validated_data, pk)
            return Response(response)

    # Change a process's type parent
    @action(detail=True, methods=['patch'])
    def change_parent(self, request, pk=True):
        processType = ProcessType.objects.get(pk=pk)

        response = request.data
        data = request.data
        if 'parent' in data:
            newParentPk = data['parent']
            if(newParentPk == 0):
                processType.move(processType.get_root())
                processType.refresh_from_db()
            elif(newParentPk > 0):
                newParent = ProcessType.objects.get(pk=newParentPk)
                processType.move(newParent, 'first-child')
                processType.refresh_from_db()
        return Response(response)

    @action(detail=False, methods=['GET'])
    def get_tree(self, request, pk=None):
        return Response(ProcessType.dump_bulk())


class ProcessViewSet(DefaultMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating processes."""
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    filter_class = ProcessFilter
    search_fields = ('title',)
    ordering_fields = ('title',)

    @action(detail=True, methods=['POST'])
    def add_child(self, request, pk=None):
        serializer = ProcessSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            response = serializer.create(validated_data, pk)
            return Response(response)

    # Change a process's parent
    @action(detail=True, methods=['patch'])
    def change_parent(self, request, pk=True):
        process = Process.objects.get(pk=pk)

        data = request.data
        if 'parent' in data:
            new_parent_pk = data['parent']
            if(new_parent_pk == 0):
                print(process.get_root())
                process.move(process.get_root())
                process.save()
                # process.refresh_from_db()
            elif(new_parent_pk > 0):
                new_parent = Process.objects.get(pk=new_parent_pk)
                process.move(new_parent, 'first-child')
                process = Process.objects.get(pk=pk)
                process.save()
                # process.refresh_from_db()

        return Response(request.data)

    @action(detail=True, methods=['GET'])
    def get_ancestors(self, request, pk=True):
        ancestors = {
            'Process': None,
            'data': []
        }
        process = self.get_object()

        if process:
            ancestors['process'] = process.__str__()
            ancestors['data'] = [acvt.__str__()
                                 for acvt in process.get_ancestors()]
        return Response(ancestors)

    @action(detail=True, methods=['GET'])
    def get_tree(self, request, pk=True):
        process = self.get_object()

        if process:
            tree = [acvt.__str__() for acvt in process.get_tree()]
            return Response(tree)

    @action(detail=False, methods=['GET'])
    def get_bulk(self, request, pk=None):
        return Response(Process.dump_bulk())

    @action(detail=True, methods=['GET'])
    def get_process_tree(self, request, pk=True):
        process = Process.objects.get(pk=pk)
        return Response(Process.dump_bulk(process))

    @action(detail=False, methods=['POST'])
    def merge_processes(self, request):
        serializer = ProcessSerializer()
        serializer.merge(request.data)
        return Response(Process.dump_bulk())

    # Get process's children having the default type
    @action(detail=True, methods=['GET'], name='Get process\'s default type children count')
    def get_process_default_type_children_count(self, request, pk=True):
        count = 0 
        processService = ProcessService()
        count = processService.get_default_type_process_children_count(pk)

        return Response({'count': count})


class PlayerViewSet(DefaultMixin, viewsets.ModelViewSet):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_class = PlayerFilter
    search_fields = ('short_name', 'long_name')
    ordering_fields = ('short_name', 'long_name')

    @action(detail=True, methods=['POST'])
    def add_child(self, request, pk=None):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            response = serializer.create(validated_data, pk)
            return Response(response)

    # Change a process's type parent
    @action(detail=True, methods=['patch'])
    def change_parent(self, request, pk=True):
        player = Player.objects.get(pk=pk)

        response = request.data
        data = request.data
        if 'parent' in data:
            newParentPk = data['parent']
            if(newParentPk == 0):
                player.move(player.get_root(), 'last-sibling')
                player.refresh_from_db()
            elif(newParentPk > 0):
                newParent = Player.objects.get(pk=newParentPk)
                player.move(newParent, 'last-child')
                player.refresh_from_db()
        return Response(response)

    @action(detail=True, methods=['GET'])
    def get_tree(self, request, pk=True):
        process = self.get_object()

        if process:
            tree = [acvt.__str__() for acvt in process.get_tree()]
            return Response(tree)


class ProcessPlayerViewSet(DefaultMixin, viewsets.ModelViewSet):

    queryset = ProcessPlayer.objects.all()
    serializer_class = ProcessPlayerSerializer
    filter_class = ProcessPlayerFilter
    search_fields = ('process', 'player', 'playerRole')
    ordering_fields = ('process', 'player', 'playerRole')


class IOElementViewSet(DefaultMixin, viewsets.ModelViewSet):

    queryset = IOElement.objects.all()
    serializer_class = IOElementSerializer
    # filter_class =
    search_fields = ('name')
    ordering_fields = ('name')


class ProcessIOViewSet(DefaultMixin, viewsets.ModelViewSet):

    queryset = ProcessIO.objects.all()
    serializer_class = ProcessIOSerializer
    filter_class = ProcessIOFilter
    search_fields = ('process', 'io_element')
    ordering_fields = ('process', 'io_element')

class StatusProcessViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = StatusProcess.objects.all()
    serializer_class = StatusProcessSerializer
    filter_class = StatusProcessFilter
    search_fields = ('name',)
    ordering_fields = ('name')