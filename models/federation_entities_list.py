from typing import List

from models.federation_entity import FederationEntity, FederationEntitySelf, FederationEntityGrid
from models.paginated_list import PaginatedList


class FederationEntitiesList(PaginatedList):
    data: List[FederationEntity]


class FederationEntitiesListSelf(PaginatedList):
    data: List[FederationEntitySelf]


class FederationEntitiesListGrid(PaginatedList):
    data: List[FederationEntityGrid]
