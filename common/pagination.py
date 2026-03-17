from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from common.responses import success_response


class CustomPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response(
            success_response(
                data=data,
                message="Data fetched successfully",
                meta={
                    "count": self.page.paginator.count,
                    "page": self.page.number,
                    "page_size": self.page_size,
                    "total_pages": self.page.paginator.num_pages
                }
            )
        )