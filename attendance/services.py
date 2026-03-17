from .models import Attendance
from employee.models import Employee
from common.exceptions import ValidationException, NotFoundException


def mark_attendance(data):
    employee_id = data.get("employee_id")
    date = data.get("date")

    employee = Employee.objects.filter(employee_id=employee_id).first()

    if not employee:
        raise NotFoundException("Employee not found")

    if Attendance.objects.filter(employee=employee, date=date).exists():
        raise ValidationException("Attendance already marked for this date")

    return Attendance.objects.create(
        employee=employee,
        date=date,
        status=data.get("status")
    )