from rest_framework import serializers
from .models import Patients, Record, PatientRecord, Practitioner
from django.utils import timezone


class PatientRegistrationSerializer(serializers.ModelSerializer):
    practitioners = serializers.ListField(
        child=serializers.IntegerField(), required=False
    )

    class Meta:
        model = Patients
        fields = [
            "id",
            "username",
            "email",
            "age",
            "password",
            "riskLevel",
            "birthday",
            "practitioners",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        practitioner_ids = validated_data.pop("practitioners", [])
        practitioners = []
        for practitioner_id in practitioner_ids:
            try:
                practitioner = Practitioner.objects.get(practitioner_id=practitioner_id)
            except Practitioner.DoesNotExist:
                raise serializers.ValidationError(
                    f"Practitioner with id {practitioner_id} does not exist"
                )
            practitioners.append(practitioner)

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
        user = Patients.objects.create_user(**user_data)
        for record in records:
            user_record = PatientRecord(user=user, record=record)
            user_record.save()
        for practitioner in practitioners:
            practitioner.patients.add(user)
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


class PatientRecordSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    record = serializers.StringRelatedField()

    class Meta:
        model = PatientRecord
        fields = ["id", "user", "record"]


class RecordUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ["name", "description", "illness"]


class PatientSerializer(serializers.ModelSerializer):
    user_records = PatientRecordSerializer(many=True, read_only=True)

    class Meta:
        model = Patients
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


class PatientDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ["username"]


class PractitionerDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practitioner
        fields = ["username"]


class PractitionerSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(many=True)

    class Meta:
        model = Practitioner
        fields = ["id", "practitioner_id", "username", "email", "patients"]


class PractitionerRegistrationSerializer(serializers.ModelSerializer):
    patients = serializers.ListField(child=serializers.IntegerField(), required=False)

    class Meta:
        model = Practitioner
        fields = [
            "practitioner_id",
            "username",
            "email",
            "password",
            "patients",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        patient_ids = validated_data.pop("patients", [])
        patients = []
        for patient_id in patient_ids:
            try:
                patient = Patients.objects.get(id=patient_id)
            except Patients.DoesNotExist:
                raise serializers.ValidationError(
                    f"Patient with id {patient_id} does not exist"
                )
            patients.append(patient)

        practitioner = Practitioner.objects.create_user(**validated_data)
        for patient in patients:
            practitioner.patients.add(patient)
        return practitioner
