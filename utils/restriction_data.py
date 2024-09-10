import os
from enum import Enum

from models.new_restriction import NewRestrictionFactory, NewRestriction
from models.restriction import Restriction
from utils.api_client import ApiClient


class RestrictionDataType(Enum):
    FEDERAL_MSC = 1
    FEDERAL_SPB = 2
    MUNICIPAL_MSC = 3
    MUNICIPAL_KLIN = 4


class RestrictionData:
    def __init__(self, restriction_type: RestrictionDataType):
        self.restriction_type = restriction_type
        self.api_client = ApiClient()

    def build(self) -> NewRestriction:
        data_method = {
            RestrictionDataType.FEDERAL_MSC: NewRestrictionFactory.build(
                object_uuid=os.getenv('SPPI_SUBJECT_REPRESENTATIVE_MOSCOW_UUID')),
            RestrictionDataType.FEDERAL_SPB: NewRestrictionFactory.build(
                object_uuid=os.getenv('SPPI_SUBJECT_REPRESENTATIVE_SPB_UUID')),
            RestrictionDataType.MUNICIPAL_MSC: NewRestrictionFactory.build(
                object_uuid=os.getenv('SPPI_LSG_REPRESENTATIVE_MOSCOW_UUID')),
            RestrictionDataType.MUNICIPAL_KLIN: NewRestrictionFactory.build(
                object_uuid=os.getenv('SPPI_LSG_REPRESENTATIVE_KLIN_UUID'))
        }[self.restriction_type]

        return data_method

    def create(self) -> Restriction:
        new_restriction = self.build()

        response = self.api_client.as_admin().restrictions().post(json=new_restriction.model_dump())
        restriction = Restriction.model_validate(response.json())

        return restriction
