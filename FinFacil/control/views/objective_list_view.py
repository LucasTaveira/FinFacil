from rest_framework import viewsets

from ..models.objective_list import ObjectiveList, ObjectiveListItens
from ..serializers.objective_list_serializer import (
    ObjectiveListSerializer, 
    ObjectiveListItensSerializer
)

class ObjectiveListView(viewsets.ModelViewSet):
    queryset = ObjectiveList.objects.all()
    serializer_class = ObjectiveListSerializer

class ObjectiveListItensView(viewsets.ModelViewSet):
    queryset = ObjectiveListItens.objects.all()
    serializer_class = ObjectiveListItensSerializer
