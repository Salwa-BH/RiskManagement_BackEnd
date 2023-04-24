
from .models import Process, ProcessType


class ProcessService(object):
    def get_default_type_process_children_count(self, process_id):
        process_type = ProcessType.objects.get(is_default=True)
        process = Process.objects.get(pk=process_id)
        count = 0

        # for child in process.get_descendants():
        #     if (child.process_type.pk == process_type.pk):
        #         count += 1
        return count
