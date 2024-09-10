from typing import List

from models.aerial_photo import AerialPhoto, AerialPhotoGrid
from models.paginated_list import PaginatedList


class AerialPhotosList(PaginatedList):
    data: List[AerialPhoto]


class AerialPhotosListGrid(PaginatedList):
    data: List[AerialPhotoGrid]
