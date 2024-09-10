from typing import List

from models.paginated_list import PaginatedList
from models.restriction import Restriction


class RestrictionsList(PaginatedList):
    data: List[Restriction]
