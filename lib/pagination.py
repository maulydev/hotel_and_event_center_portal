from rest_framework.pagination import LimitOffsetPagination

class Pagination(LimitOffsetPagination):
    default_limit = 25  # Number of items to display by default if `limit` is not provided in the query params
    limit_query_param = 'limit'  # Query parameter to specify the limit of items per page
    offset_query_param = 'offset'  # Query parameter to specify the offset
    max_limit = 50  # Maximum number of items that can be requested per page
