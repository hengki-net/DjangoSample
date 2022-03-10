from rest_framework import serializers
from api.sample import sample_models


class sample_Serializer(serializers.ModelSerializer):
    class Meta:
        model = sample_models.sample_Model
        fields = ['PON', 'IN_DATE']
