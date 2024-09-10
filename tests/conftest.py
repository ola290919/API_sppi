from typing import List

import pytest
from models.aerial_photos_list import AerialPhotosList, AerialPhoto
from models.federation_entities_list import FederationEntitiesList
from models.federation_entity import FederationEntity
from models.municipal_list import MunicipalList, Municipal
from models.new_federation_entity import NewFederationEntityFactory
from models.new_municipal_entity import NewMunicipalFactory
from models.restriction import Restriction
from models.restrictions_list import RestrictionsList
from pydantic import UUID4
from utils.api_client import ApiClient
from utils.restriction_data import RestrictionData, RestrictionDataType
from utils.uuid_fetcher import UUIDType


@pytest.fixture(scope="function")
def api_client() -> ApiClient:
    return ApiClient()


@pytest.fixture(scope="function")
def uuid_data():
    """
    Фикстура параметризации тестов с [uuid] только субъектов федерации,
    только МСУ или любого
    """

    def _wrapper(data_type: UUIDType):
        return data_type.get_uuid()

    yield _wrapper


@pytest.fixture(scope="class")
def federation_entity() -> FederationEntity:
    api_client = ApiClient()

    federation_entity = api_client.create_federation_entity()

    yield federation_entity

    api_client.delete_federation_entity(federation_entity.uuid)


@pytest.fixture(scope="class")
def federation_entities_with_different_names() -> List[FederationEntity]:
    api_client = ApiClient()

    entities = [
        api_client.create_federation_entity(new_federation_entity=NewFederationEntityFactory.build(name='test1')),
        api_client.create_federation_entity(new_federation_entity=NewFederationEntityFactory.build(name='test2'))
    ]

    yield entities

    for entity in entities:
        api_client.delete_federation_entity(entity.uuid)


@pytest.fixture(scope="class")
def federation_entities_with_registered_in_sppi() -> List[FederationEntity]:
    api_client = ApiClient()

    entities = [
        api_client.create_federation_entity(
            new_federation_entity=NewFederationEntityFactory.build(details__registered_in_sppi=True)),
        api_client.create_federation_entity(
            new_federation_entity=NewFederationEntityFactory.build(details__registered_in_sppi=False))
    ]

    yield entities

    for entity in entities:
        api_client.delete_federation_entity(entity.uuid)


@pytest.fixture(scope="class")
def municipals_with_registered_in_sppi() -> List[Municipal]:
    api_client = ApiClient()

    entities = [
        api_client.create_municipal(
            new_municipal=NewMunicipalFactory.build(details__registered_in_sppi=True)),
        api_client.create_municipal(
            new_municipal=NewMunicipalFactory.build(details__registered_in_sppi=False))
    ]
    yield entities

    for entity in entities:
        api_client.delete_federation_entity(entity.federal_entity.uuid)
        api_client.delete_municipal(entity.uuid)


@pytest.fixture(scope="class")
def municipals_with_different_names(federation_entities_with_different_names) -> List[Municipal]:
    api_client = ApiClient()

    entities = [
        api_client.create_municipal(new_municipal=NewMunicipalFactory.build(
            name='test1',
            federal_entity_uuid=str(federation_entities_with_different_names[0].uuid))),
        api_client.create_municipal(new_municipal=NewMunicipalFactory.build(
            name='test2',
            federal_entity_uuid=str(federation_entities_with_different_names[1].uuid)))
    ]

    yield entities

    for entity in entities:
        api_client.delete_municipal(entity.uuid)


@pytest.fixture(scope="class")
def aerial_photo() -> AerialPhoto:
    api_client = ApiClient()

    aerial_photo = api_client.create_aerial_photo()

    yield aerial_photo

    api_client.delete_aerial_photo(aerial_photo.uuid)


@pytest.fixture(scope="class")
def municipal_entity() -> Municipal:
    api_client = ApiClient()

    municipal_entity = api_client.create_municipal()

    yield municipal_entity

    api_client.delete_municipal(municipal_entity.uuid)


@pytest.fixture(scope="class")
def geometry_uuid(federation_entity) -> UUID4:
    api_client = ApiClient()

    geometry = api_client.create_geometry(object_uuid=federation_entity.uuid)

    yield geometry.uuid

    api_client.delete_geometry(geometry.uuid)


@pytest.fixture(scope="function")
def restriction_build():
    def _wrapper(restriction_data_type: RestrictionDataType):
        return RestrictionData(restriction_data_type).build()

    yield _wrapper


@pytest.fixture(scope="session")
def new_restriction(request):
    api_client = ApiClient()

    class NewRestrictionFixture:
        created_restrictions: List[Restriction] = []

        def wrapper(self, restriction_data_type: RestrictionDataType):
            created_restriction = RestrictionData(restriction_data_type).create()
            self.created_restrictions.append(created_restriction)
            return created_restriction

        def delete_restrictions(self):
            for restriction in self.created_restrictions:
                api_client.as_admin().restrictions().uuid(restriction.uuid).delete()

    fixture = NewRestrictionFixture()

    yield fixture.wrapper

    request.addfinalizer(fixture.delete_restrictions)


@pytest.fixture(scope="class")
def federation_entities_list() -> List[FederationEntity]:
    api_client = ApiClient()

    federation_entities_list = FederationEntitiesList.model_validate(
        api_client.as_admin().federation_entities().get().json()).data

    if not federation_entities_list:
        pytest.skip("Federation entities list is empty")

    if len(federation_entities_list) < 3:
        pytest.skip("Federation entities list contains less than three entities")

    return federation_entities_list


@pytest.fixture(scope="class")
def aerial_photos_list() -> List[AerialPhoto]:
    api_client = ApiClient()

    aerial_photos_list = AerialPhotosList.model_validate(
        api_client.as_admin().aerial_photos().get().json()).data

    if not aerial_photos_list:
        pytest.skip("Aerial Photos list is empty")

    if len(aerial_photos_list) < 3:
        pytest.skip("Aerial Photos list contains less than three entities")

    return aerial_photos_list


@pytest.fixture(scope="class")
def municipals_list() -> List[Municipal]:
    api_client = ApiClient()

    municipals_list = MunicipalList.model_validate(
        api_client.as_admin().municipals().get().json()).data

    if not municipals_list:
        pytest.skip("Municipal list is empty")

    if len(municipals_list) < 3:
        pytest.skip("Municipal list contains less than three entities")

    return municipals_list


@pytest.fixture(scope="class")
def restrictions_list() -> List[Restriction]:
    api_client = ApiClient()

    restrictions_list = RestrictionsList.model_validate(
        api_client.as_admin().restrictions().query(
            {'filter[object_uuid]': UUIDType.SUBJECT.get_uuid()}).get().json()).data

    if not restrictions_list:
        pytest.skip("Restrictions list is empty")

    if len(restrictions_list) < 3:
        pytest.skip("Restrictions list contains less than three entities")

    return restrictions_list
