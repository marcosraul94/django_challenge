from http import HTTPStatus
from django.http import JsonResponse
from django.views.generic import View
from works_single_view.models import MusicalWork
from works_single_view.utils import load_musical_works


class MusicalWorkDetailView(View):
    model = MusicalWork
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        iswc: str = kwargs['iswc']

        data = load_musical_works()

        try:
            musical_work: MusicalWork = MusicalWork.objects.get(iswc=iswc)
            data = {"data": musical_work.to_json()}
            return JsonResponse(data, safe=False, status=HTTPStatus.OK)

        except MusicalWork.DoesNotExist:
            data = {'message': f'Entity not found with iswc = \'{iswc}\''}
            return JsonResponse(data, status=HTTPStatus.NOT_FOUND)
