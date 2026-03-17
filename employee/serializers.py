from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    present_days = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Employee
        fields = "__all__"

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required")
        return value