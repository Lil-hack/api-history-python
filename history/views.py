from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets, status
from rest_framework.decorators import detail_route, action
from rest_framework.response import Response

from history.models import History

from history.serializers import HistorySerializer


class HistoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    permission_classes = (

     )


    def list(self, request,*args, **kwargs):
        # find all categories first

        # then, filter the categories itself.
        queryset = History.objects.filter(pk__in='uuid').distinct()

        serializer = HistorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




    def perform_create(self, serializer):
        serializer.save()



