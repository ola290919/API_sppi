from models.default_model import DefaultModel


class PaginatedList(DefaultModel):
    total: int
    limit: int
    offset: int
