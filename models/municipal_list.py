from typing import List

from models.municipal import Municipal, MunicipalSelf, MunicipalGrid, MunicipalDetail
from models.paginated_list import PaginatedList


class MunicipalList(PaginatedList):
    data: List[Municipal]


class MunicipalListSelf(PaginatedList):
    data: List[MunicipalSelf]


class MunicipalListGrid(PaginatedList):
    data: List[MunicipalGrid]


class MunicipalListDetail(PaginatedList):
    data: List[MunicipalDetail]
