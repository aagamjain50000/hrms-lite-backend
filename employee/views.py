from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import EmployeeSerializer
from .selectors import get_all_employees, get_employee_with_attendance_count
from .services import create_employee, delete_employee

from common.responses import success_response
from common.pagination import CustomPagination


class EmployeeViewSet(viewsets.ViewSet, CustomPagination):

    def list(self, request):
        employees = get_all_employees()

        page = self.paginate_queryset(employees, request)
        if page is not None:
            serializer = EmployeeSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EmployeeSerializer(employees, many=True)
        return Response(
            success_response(
                data=serializer.data,
                message="Data fetched successfully",
                meta={"count": len(serializer.data)}
            )
        )

    @action(detail=False, methods=["get"], url_path="attendance-summary")
    def attendance_summary(self, request):
        """
        Returns employees with their total present days.
        """
        employees = get_employee_with_attendance_count()

        page = self.paginate_queryset(employees, request)
        if page is not None:
            serializer = EmployeeSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EmployeeSerializer(employees, many=True)
        return Response(
            success_response(
                data=serializer.data,
                message="Data fetched successfully",
                meta={"count": len(serializer.data)}
            )
        )

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee = create_employee(serializer.validated_data)

        return Response(
            success_response(
                EmployeeSerializer(employee).data,
                "Employee created successfully"
            ),
            status=status.HTTP_201_CREATED
        )

    def destroy(self, request, pk=None):
        delete_employee(pk)

        return Response(
            success_response(message="Employee deleted successfully"),
            status=status.HTTP_200_OK
        )