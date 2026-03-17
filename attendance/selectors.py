from .models import Attendance


def get_all_attendance():
    return Attendance.objects.select_related('employee').all().order_by('-date')


def get_attendance_by_employee(employee_id):
    return Attendance.objects.select_related('employee').filter(
        employee__employee_id=employee_id
    ).order_by('-date')


def filter_attendance(employee_id=None, date=None):
    queryset = Attendance.objects.select_related('employee').all()

    if employee_id:
        queryset = queryset.filter(employee__employee_id=employee_id)

    if date:
        queryset = queryset.filter(date=date)

    return queryset.order_by('-date')