from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import AttendanceSerializer
from .services import mark_attendance
from .selectors import filter_attendance

from common.responses import success_response
from common.pagination import CustomPagination


class AttendanceViewSet(viewsets.ViewSet, CustomPagination):

    def list(self, request):
        employee_id = request.query_params.get("employee_id")
        date = request.query_params.get("date")

        attendance = filter_attendance(employee_id, date)

        page = self.paginate_queryset(attendance, request)
        if page is not None:
            serializer = AttendanceSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AttendanceSerializer(attendance, many=True)
        return Response(
            success_response(
                data=serializer.data,
                message="Data fetched successfully",
                meta={"count": len(serializer.data)}
            )
        )

    def create(self, request):
        serializer = AttendanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        attendance = mark_attendance(serializer.validated_data)

        return Response(
            success_response(
                AttendanceSerializer(attendance).data,
                "Attendance marked successfully"
            ),
            status=status.HTTP_201_CREATED
        )