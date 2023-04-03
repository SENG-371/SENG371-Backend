from rest_framework import serializers
from .models import CustomUser, Record, UserRecord
from django.utils import timezone


class UserRegistrationSerializer(serializers.ModelSerializer):
    records = serializers.ListField(child=serializers.IntegerField(), required=False)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "age",
            "password",
            "riskLevel",
            "birthday",
            "records",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        record_ids = validated_data.pop("records", [])
        records = []
        for record_id in record_ids:
            try:
                record = Record.objects.get(id=record_id)
            except Record.DoesNotExist:
                record_data = {
                    "name": f"Record {record_id}",
                    "description": "",
                    "created_at": timezone.now(),
                    "updated_at": timezone.now(),
                }
                record = Record.objects.create(**record_data)
            records.append(record)

        user_data = validated_data
        user = CustomUser.objects.create_user(**user_data)
        for record in records:
            user_record = UserRecord(user=user, record=record)
            user_record.save()
        return user


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ["id", "name", "description", "illness", "created_at", "updated_at"]

    def create(self, validated_data):
        record, created = Record.objects.update_or_create(
            name=validated_data["name"],
            defaults={
                "description": validated_data.get("description", ""),
                "illness": validated_data.get("illness", ""),
            },
        )
        return record


class UserRecordSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    record = serializers.StringRelatedField()

    class Meta:
        model = UserRecord
        fields = ["id", "user", "record"]


class RecordUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ["name", "description", "illness"]


class UserSerializer(serializers.ModelSerializer):
    user_records = UserRecordSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "age",
            "birthday",
            "riskLevel",
            "user_records",
        ]

    def get_records(self, obj):
        user_records = obj.user_records.all()
        return RecordSerializer(user_records.values("record"), many=True).data


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username"]
