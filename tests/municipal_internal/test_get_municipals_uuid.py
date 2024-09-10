import pytest

from models.municipal import Municipal
from utils.uuid_fetcher import UUIDType


class TestGetMunicipalsUuid:
    def test_should_return_200(self, api_client, uuid_data):
        response = api_client.internal().municipals().uuid(uuid_data(UUIDType.MUNICIPAL)).get()

        assert response.status_code == 200

    def test_should_return_valid_model(self, api_client, uuid_data):
        response = api_client.internal().municipals().uuid(uuid_data(UUIDType.MUNICIPAL)).get()

        assert Municipal.model_validate(response.json())

    def test_should_return_404(self, api_client, uuid_data):
        response = api_client.internal().municipals().uuid(uuid_data(UUIDType.FEDERAL)).get()

        assert response.status_code == 404

    def test_should_return_422(self, api_client):
        response = api_client.internal().municipals().uuid(1).get()

        assert response.status_code == 422

    @pytest.mark.skip("don't know how to get 500 error")
    def test_should_return_500(self, api_client):
        pass
