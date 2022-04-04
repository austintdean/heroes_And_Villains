from rest_framework import serializers
from .models import super_type

class super_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = super_type
        fields =['type']