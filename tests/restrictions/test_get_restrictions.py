import allure
import pytest

from models.error import Error
from models.restrictions_list import RestrictionsList
from utils.uuid_fetcher import UUIDType


class TestGetRestrictions:
    @allure.epic('Status code')
    @allure.feature('200')
    @allure.story('restrictions')
    def test_should_get_200(self, api_client, uuid_data):
        response = (api_client.as_admin().restrictions().
                    query({'filter[object_uuid]': uuid_data(UUIDType.SUBJECT)}).get())

        assert response.status_code == 200

    @allure.epic('Status code')
    @allure.feature('401')
    @allure.story('restrictions')
    def test_should_return_401(self, api_client, uuid_data):
        response = (api_client.restrictions().
                    query({'filter[object_uuid]': uuid_data(UUIDType.SUBJECT)}).get())

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('403')
    @allure.story('restrictions')
    def test_should_return_403(self, api_client, uuid_data):
        response = (api_client.as_subject_representative_moscow().restrictions().
                    query({'filter[object_uuid]': uuid_data(UUIDType.LSG)}).get())

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('403')
    @allure.story('restrictions')
    def test_should_return_422(self, api_client):
        response = (api_client.as_admin().restrictions().
                    query({'filter[object_uuid]': '･✿ヾ╲(｡◕‿◕｡)╱✿･'}).get())

        assert response.status_code == 422
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('500')
    @allure.story('restrictions')
    @pytest.mark.skip("don't know how get 500 error")
    def test_should_return_500(self, api_client):
        pass

    @allure.epic('Valid model')
    @allure.feature('without detalization')
    @allure.story('restrictions')
    def test_should_has_valid_models(self, api_client, uuid_data):
        response = (api_client.as_admin().restrictions().
                    query({'filter[object_uuid]': uuid_data(UUIDType.SUBJECT)}).get())

        assert RestrictionsList.model_validate(response.json())

    @allure.epic('Parameters')
    @allure.feature('limit')
    @allure.story('restrictions')
    def test_should_limit(self, api_client, uuid_data, restrictions_list):
        response = RestrictionsList.model_validate(
            api_client.as_admin().restrictions().limit(1).
            query({'filter[object_uuid]': uuid_data(UUIDType.SUBJECT)}).get().json())

        assert len(response.data) == 1
        assert len(response.data) < len(restrictions_list)

    @allure.epic('Parameters')
    @allure.feature('offset')
    @allure.story('restrictions')
    @pytest.mark.not_stable
    def test_should_offset(self, api_client, uuid_data, restrictions_list):
        response = RestrictionsList.model_validate(
            api_client.as_admin().restrictions().limit(1).offset(1).
            query({'filter[object_uuid]': uuid_data(UUIDType.SUBJECT)}).get().json())

        assert response.data[0] == restrictions_list[1]

    @allure.epic('Parameters')
    @allure.feature('search')
    @allure.story('restrictions')
    @pytest.mark.skip("don't have docs what fields included in search")
    def test_should_search(self):
        pass

    @allure.epic('Access')
    @allure.feature('default')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('pilot')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('browsing_dispatcher')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('dispatcher_gc')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('atm_dispatcher')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('admin')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('atm_admin')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('super_admin')
    @allure.story('restrictions')
    @pytest.mark.skip("can't create super admin via SPPI UI")
    @pytest.mark.access
    def test_access_super_admin(self, api_client):
        pass

    @allure.epic('Access')
    @allure.feature('aircompany')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('subject_representative')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('lsg_representative')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('mod_representative')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mo')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_fsb')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_fso')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mvd')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_vv_mvd_rf')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mchs')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_dosaaf')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_custom')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('experimental_aviation')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('aeroinfo')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('svs_pilot')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('spw_manager')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('mr_submission_manager')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('shar_pilot')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('aer_pilot')
    @allure.story('restrictions')
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

    @allure.epic('Access')
    @allure.feature('bla_pilot')
    @allure.story('restrictions')
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
