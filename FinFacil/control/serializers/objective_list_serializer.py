from rest_framework import serializers

from ..models.objective_list import ObjectiveList, ObjectiveListItens

class ObjectiveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectiveList
        fields = '__all__'
    
class ObjectiveListItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectiveListItens
        fields = '__all__'
