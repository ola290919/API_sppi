from typing import List

from models.entity_short import EntityShort
from models.paginated_list import PaginatedList


class EntityShortList(PaginatedList):
    data: List[EntityShort]
