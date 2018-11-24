from rest_framework.serializers import ModelSerializer

from .models import GasesCollected


class ValuesSerializer(ModelSerializer):

    class Meta:
        model = GasesCollected
        fields = '__all__'


'''
class ValuesFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valores
        fields = ('temperature', 'humidity', 'co' , 'co2', 'mp25', 'id')
'''
