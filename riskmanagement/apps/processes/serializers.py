from rest_framework import serializers
from .models import Process, ProcessType, ProcessPlayer ,StatusProcess
from .models import Player, IOElement, ProcessIO
from .models import CompanySite


class CompanySiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySite
        fields = ('id', 'name', 'is_default')


class ProcessTypeSerializer(serializers.ModelSerializer):
    """Class serializer for the Activity model"""

    children = serializers.SerializerMethodField('get_children')
    depth = serializers.SerializerMethodField('get_depth')

    class Meta:
        model = ProcessType
        fields = ('id', 'name', 'is_default', 'children', "depth")

    def create(self, validated_data, pk=None):
        if pk is None:
            return ProcessType.add_root(**validated_data)
        else:
            if validated_data:
                parent = ProcessType.objects.get(pk=pk)
                parent.add_child(
                    **validated_data)
                return {**validated_data}

    def get_children(self, obj):
        return [
            {'id': processType.id,
             'name': processType.name}
            for processType in obj.get_children()
        ]

    def get_depth(self, obj):
        return obj.depth


class ProcessSerializer(serializers.ModelSerializer):
    """Class serializer for the Activity model"""

    # bulk = serializers.SerializerMethodField('get_bulk')
    parents = serializers.SerializerMethodField('get_parents')
    children = serializers.SerializerMethodField('get_children')
    depth = serializers.SerializerMethodField("get_depth")
    company_site_info = serializers.SerializerMethodField(
        "get_company_site_info")

    class Meta:
        model = Process
        fields = ('id', 'title', 'description', 'aim', 'process_type', 'company_site', 'status',
                  'start_date', 'end_date', 'company_site_info', 'depth', 'parents', 'children',
                  'financial_level_1','financial_level_2','financial_level_3','financial_level_4','financial_level_5' )

    def create(self, validated_data, pk=None):
        if pk is None:
            return Process.add_root(**validated_data)
        else:
            if validated_data:
                process_type = validated_data.pop('process_type')
                company_site = validated_data.pop('company_site')
                parent_process = Process.objects.get(pk=pk)
                parent_process.add_child(
                    **validated_data, process_type=process_type, company_site=company_site)
                return {**validated_data,
                        'type': process_type.pk,
                        'company_site': company_site.pk}

    def merge(self, data):
        errors = []
        if 'firstProcess' not in data:
            errors.append("First Process Id Not Received")
        if 'secondProcess' not in data:
            errors.append("Second Process Id Not Received")
        if 'newProcessName' not in data:
            errors.append("New Merged Process Name Not Received")

        if len(errors) > 0:
            raise serializers.ValidationError(str(errors))

        try:
            firstProcess = Process.objects.get(pk=data['firstProcess'])
            secondProcess = Process.objects.get(pk=data['secondProcess'])
            newName = data["newProcessName"]

            if firstProcess.get_depth() == secondProcess.get_depth():
                if secondProcess.get_children_count() > 0:
                    for process in secondProcess.get_children():
                        process.move(firstProcess, "last-child")
                    secondProcess.delete()
                else:
                    secondProcess.delete()
                if newName != "":
                    firstProcess.title = newName
                    firstProcess.save()

            else:
                raise serializers.ValidationError(
                    "The processes aren't from the same level")

        except Process.DoesNotExist:
            raise serializers.ValidationError("Process does not exist!")

    def get_parents(self, obj):
        return [
            {
                'id': process.id,
                'title': process.title
            }
            for process in obj.get_ancestors()
        ]

    def get_children(self, obj):
        return [
            {
                'id': process.id,
                'title': process.title,
                'status': process.status,
                'process_type': process.process_type.id,
                'depth': process.depth
            }
            for process in obj.get_children()
        ]

    def get_depth(self, obj):
        return obj.depth

    def get_company_site_info(self, obj):
        return {
            "id": obj.company_site.id,
            "name": obj.company_site.name
        }


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('id', 'short_name', 'long_name',
                  'nature', 'start_date', 'end_date')

    def create(self, validated_data, pk=None):
        if pk is None:
            return Player.add_root(**validated_data)
        else:
            if validated_data:
                parent = Player.objects.get(pk=pk)
                parent.add_child(
                    **validated_data)
                return {**validated_data}


class ProcessPlayerSerializer(serializers.ModelSerializer):
    playerDetails = serializers.SerializerMethodField('get_player_details')

    class Meta:
        model = ProcessPlayer
        fields = ('id', 'process', 'player', 'playerRole', 'playerDetails')

    def get_player_details(self, obj):
        playerObject = {
            'name': obj.player.long_name,
            'short_name': obj.player.short_name
        }
        return playerObject


class IOElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = IOElement
        fields = '__all__'


class ProcessIOSerializer(serializers.ModelSerializer):

    ioDetails = serializers.SerializerMethodField('get_io_details')

    class Meta:
        model = ProcessIO
        fields = ('id', 'process', 'io_element', 'io_type', 'ioDetails')

    def get_io_details(self, obj):
        return {
            'name': obj.io_element.name
        }
class  StatusProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusProcess
        fields = ('id', 'name')