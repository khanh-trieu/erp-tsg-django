from rest_framework.pagination import LimitOffsetPagination, CursorPagination, PageNumberPagination


class MyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'page'
    # ordering = '-id'



