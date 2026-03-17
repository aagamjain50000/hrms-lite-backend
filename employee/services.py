from .models import Employee
from common.exceptions import ValidationException, NotFoundException


def create_employee(data):
    if Employee.objects.filter(employee_id=data.get("employee_id")).exists():
        raise ValidationException("Employee ID already exists")

    if Employee.objects.filter(email=data.get("email")).exists():
        raise ValidationException("Email already exists")

    return Employee.objects.create(**data)


def delete_employee(pk):
    employee = Employee.objects.filter(pk=pk).first()

    if not employee:
        raise NotFoundException("Employee not found")

    employee.delete()
    return True