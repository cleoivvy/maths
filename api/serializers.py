from rest_framework import serializers
from .models import NumberProperties

class NumberPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberProperties
        fields = '__all__'
