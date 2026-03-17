from .models import Employee
from django.db.models import Count, Q


def get_all_employees():
    return Employee.objects.all().order_by('-created_at')


def get_employee_by_id(pk):
    return Employee.objects.filter(pk=pk).first()


def get_employee_by_employee_id(employee_id):
    return Employee.objects.filter(employee_id=employee_id).first()

def get_employee_with_attendance_count():

    return Employee.objects.annotate(
        present_days=Count(
            'attendances',
            filter=Q(attendances__status='PRESENT')
        )
    )