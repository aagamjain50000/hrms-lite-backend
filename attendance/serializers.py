from rest_framework import serializers
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(write_only=True)
    employee_name = serializers.CharField(source="employee.full_name", read_only=True)

    class Meta:
        model = Attendance
        fields = ["id", "employee_id", "employee_name", "date", "status"]

    def validate_status(self, value):
        if value not in ["PRESENT", "ABSENT"]:
            raise serializers.ValidationError("Invalid status")
        return value