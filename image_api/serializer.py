from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import record

class recordSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(use_url=True)

    class Meta:
        model = record
        fields='__all__'