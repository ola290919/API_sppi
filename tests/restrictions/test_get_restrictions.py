import allure
import pytest

from models.error import Error
from models.restrictions_list import RestrictionsList
from utils.uuid_fetcher import UUIDType


class TestGetRestrictions:
    @allure.feature('Проверка статус кода ответа')
    def test_should_get_200(self, api_client, uuid_data):
        response = (api_client.as_admin().restrictions().
                    query({'filter[object_uuid]': uuid_data(UUIDType.SUBJECT)}).get())

        assert response.status_code == 200

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3053/")
    def test_should_return_401(self, api_client, uuid_data):
        response = (api_client.restrictions().
                    query({'filter[object_uuid]': uuid_data(UUIDType.SUBJECT)}).get())

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    def test_should_return_403(self, api_client, uuid_data):
        response = (api_client.as_subject_representative_moscow().restrictions().
                    query({'filter[object_uuid]': uuid_data(UUIDType.LSG)}).get())

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    def test_should_return_422(self, api_client):
        response = (api_client.as_admin().restrictions().
                    query({'filter[object_uuid]': '･✿ヾ╲(｡◕‿◕｡)╱✿･'}).get())

        assert response.status_code == 422
        assert Error.model_validate(response.json())

    @pytest.mark.skip("don't know how get 500 error")
    def test_should_return_500(self, api_client):
        pass

    def test_should_has_valid_models(self, api_client, uuid_data):
        response = (api_client.as_admin().restrictions().
                    query({'filter[object_uuid]': uuid_data(UUIDType.SUBJECT)}).get())

        assert RestrictionsList.model_validate(response.json())

    def test_should_limit(self, api_client, uuid_data, restrictions_list):
        response = RestrictionsList.model_validate(
            api_client.as_admin().restrictions().limit(1).
            query({'filter[object_uuid]': uuid_data(UUIDType.SUBJECT)}).get().json())

        assert len(response.data) == 1
        assert len(response.data) < len(restrictions_list)

    @pytest.mark.not_stable
    def test_should_offset(self, api_client, uuid_data, restrictions_list):
        response = RestrictionsList.model_validate(
            api_client.as_admin().restrictions().limit(1).offset(1).
            query({'filter[object_uuid]': uuid_data(UUIDType.SUBJECT)}).get().json())

        assert response.data[0] == restrictions_list[1]

    @pytest.mark.skip("don't have docs what fields included in search")
    def test_should_search(self):
        pass

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_default(self, api_client, uuid_data, data_param):
        response = (api_client.as_default().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_pilot(self, api_client, uuid_data, data_param):
        response = (api_client.as_pilot().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_browsing_dispatcher(self, api_client, uuid_data, data_param):
        response = (api_client.as_browsing_dispatcher().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_dispatcher_gc(self, api_client, uuid_data, data_param):
        response = (api_client.as_dispatcher_gc().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_atm_dispatcher(self, api_client, uuid_data, data_param):
        response = (api_client.as_atm_dispatcher_moscow().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_admin(self, api_client, uuid_data, data_param):
        response = (api_client.as_pilot().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_atm_admin(self, api_client, uuid_data, data_param):
        response = (api_client.as_atm_admin_moscow().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.skip("can't create super admin via SPPI UI")
    @pytest.mark.access
    def test_access_super_admin(self, api_client):
        pass

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_aircompany(self, api_client, uuid_data, data_param):
        response = (api_client.as_aircompany().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY,
        UUIDType.SUBJECT
    ])
    def test_access_subject_representative(self, api_client, uuid_data, data_param):
        response = (api_client.as_subject_representative_moscow().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())
        if data_param in (UUIDType.SUBJECT, UUIDType.FEDERAL):
            assert response.status_code == 200
        else:
            assert response.status_code == 403

        if data_param == UUIDType.SUBJECT:
            assert uuid_data(data_param) in response.text

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY,
        UUIDType.LSG
    ])
    def test_access_lsg_representative(self, api_client, uuid_data, data_param):
        response = (api_client.as_lsg_representative_moscow().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 200

        if data_param == UUIDType.LSG:
            assert uuid_data(data_param) in response.text

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_mod_representative(self, api_client, uuid_data, data_param):
        response = (api_client.as_mod_representative().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_gosaviaciya_mo(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_mo().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_gosaviaciya_fsb(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_fsb().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_gosaviaciya_fso(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_fso().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_gosaviaciya_mvd(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_mvd().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_gosaviaciya_vv_mvd_rf(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_vv_mvd_rf().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_gosaviaciya_mchs(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_mchs().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_gosaviaciya_dosaaf(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_dosaaf().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_gosaviaciya_custom(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_custom().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_experimental_aviation(self, api_client, uuid_data, data_param):
        response = (api_client.as_experimental_aviation().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_aeroinfo(self, api_client, uuid_data, data_param):
        response = (api_client.as_aeroinfo_uuuwzdzx().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_svs_pilot(self, api_client, uuid_data, data_param):
        response = (api_client.as_svs_pilot().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_spw_manager(self, api_client, uuid_data, data_param):
        response = (api_client.as_spw_manager().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_mr_submission_manager(self, api_client, uuid_data, data_param):
        response = (api_client.as_mr_submission_manager().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_shar_pilot(self, api_client, uuid_data, data_param):
        response = (api_client.as_shar_pilot().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_aer_pilot(self, api_client, uuid_data, data_param):
        response = (api_client.as_aer_pilot().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.ANY
    ])
    def test_access_bla_pilot(self, api_client, uuid_data, data_param):
        response = (api_client.as_bla_pilot().restrictions().
                    query({'filter[object_uuid]': uuid_data(data_param)}).get())

        assert response.status_code == 200
