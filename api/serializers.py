from rest_framework import serializers

from api.models import ZwardyFarmers

class ZwardyFarmersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZwardyFarmers
        fields = ('date_created', 'is_active', 'form_id', 'first_name', 'surname')

