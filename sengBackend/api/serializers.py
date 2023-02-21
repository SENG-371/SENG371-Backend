from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.Serializer):
    illness = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Record.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.illness = validated_data.get("illness", instance.illness)
        instance.description = validated_data.get("description", instance.description)
