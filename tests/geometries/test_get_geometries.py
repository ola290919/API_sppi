import allure
import pytest

from models.error import Error
from models.geometries_list import GeometriesList
from utils.uuid_fetcher import UUIDType


class TestGetGeometries:
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_should_get_200(self, api_client, uuid_data, data_param):
        response = api_client.as_admin().geometries().query({'uuid': uuid_data(data_param)}).get()

        assert response.status_code == 200

    def test_should_return_valid_model(self, api_client, uuid_data):
        # TODO need to get a valid uuid with full geometry to check its model
        response = api_client.as_admin().geometries().query({'uuid': uuid_data(UUIDType.SUBJECT)}).get()

        assert GeometriesList.model_validate(response.json())

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3053/")
    def test_should_return_401(self, api_client, uuid_data):
        response = api_client.geometries().query({'uuid': uuid_data(UUIDType.SUBJECT)}).get()

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    def test_should_return_403(self, api_client, uuid_data):
        response = api_client.as_gosaviaciya_mo().geometries().query({'uuid': uuid_data(UUIDType.SUBJECT)}).get()

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    @pytest.mark.skip("don't know how to get 422 error")
    def test_should_return_422(self, api_client):
        pass

    @pytest.mark.skip("don't know how to get 500 error")
    def test_should_return_500(self):
        pass

    @pytest.mark.skip("need an uuid with more that one geometry")
    def test_should_limit(self):
        pass

    @pytest.mark.skip("need an uuid with more that one geometry")
    def test_should_offset(self):
        pass

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_default(self, api_client, uuid_data, data_param):
        response = (api_client.as_default().geometries().query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_pilot(self, api_client, uuid_data, data_param):
        response = (api_client.as_pilot().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        if data_param == UUIDType.PHOTO:
            assert response.status_code == 403
        else:
            assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_browsing_dispatcher(self, api_client, uuid_data, data_param):
        response = (api_client.as_browsing_dispatcher().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_dispatcher_gc(self, api_client, uuid_data, data_param):
        response = (api_client.as_dispatcher_gc().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_atm_dispatcher(self, api_client, uuid_data, data_param):
        response = (api_client.as_atm_dispatcher_moscow().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_admin(self, api_client, uuid_data, data_param):
        response = api_client.as_admin().geometries().query({'uuid': uuid_data(data_param)}).get()

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_atm_admin(self, api_client, uuid_data, data_param):
        response = (api_client.as_atm_admin_moscow().geometries().
                    query({'uuid': uuid_data(data_param)}).get())
        assert response.status_code == 403

    @pytest.mark.skip("can't create super admin via SPPI UI")
    @pytest.mark.access
    def test_access_super_admin(self):
        pass

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_aircompany(self, api_client, uuid_data, data_param):
        response = (api_client.as_aircompany().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        if data_param == UUIDType.PHOTO:
            assert response.status_code == 403
        else:
            assert response.status_code == 200

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3063/")
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.LSG_KLIN,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG_KLIN
    ])
    def test_access_subject_representative(self, api_client, uuid_data, data_param):
        response = (api_client.as_subject_representative_moscow().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        if data_param == UUIDType.RESTRICTION_SUBJECT or UUIDType.FEDERAL:
            assert response.status_code == 200
        else:
            assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_lsg_representative(self, api_client, uuid_data, data_param):
        response = (api_client.as_lsg_representative_moscow().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        if data_param == UUIDType.PHOTO:
            assert response.status_code == 403
        else:
            assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_mod_representative(self, api_client, uuid_data, data_param):
        response = (api_client.as_mod_representative().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        if data_param == UUIDType.PHOTO:
            assert response.status_code == 200
        else:
            assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_gosaviaciya_mo(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_mo().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_gosaviaciya_fsb(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_fsb().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_gosaviaciya_fso(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_fso().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_gosaviaciya_mvd(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_mvd().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_gosaviaciya_vv_mvd_rf(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_vv_mvd_rf().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_gosaviaciya_mchs(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_mchs().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_gosaviaciya_dosaaf(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_dosaaf().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_gosaviaciya_custom(self, api_client, uuid_data, data_param):
        response = (api_client.as_gosaviaciya_custom().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_experimental_aviation(self, api_client, uuid_data, data_param):
        response = (api_client.as_experimental_aviation().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_aeroinfo(self, api_client, uuid_data, data_param):
        response = (api_client.as_aeroinfo_uuuwzdzx().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_svs_pilot(self, api_client, uuid_data, data_param):
        response = (api_client.as_svs_pilot().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        if data_param == UUIDType.PHOTO:
            assert response.status_code == 403
        else:
            assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_spw_manager(self, api_client, uuid_data, data_param):
        response = (api_client.as_spw_manager().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        if data_param == UUIDType.PHOTO:
            assert response.status_code == 403
        else:
            assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_mr_submission_manager(self, api_client, uuid_data, data_param):
        response = (api_client.as_mr_submission_manager().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_shar_pilot(self, api_client, uuid_data, data_param):
        response = (api_client.as_shar_pilot().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        if data_param == UUIDType.PHOTO:
            assert response.status_code == 403
        else:
            assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_aer_pilot(self, api_client, uuid_data, data_param):
        response = (api_client.as_aer_pilot().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        if data_param == UUIDType.PHOTO:
            assert response.status_code == 403
        else:
            assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_access_bla_pilot(self, api_client, uuid_data, data_param):
        response = (api_client.as_bla_pilot().geometries().
                    query({'uuid': uuid_data(data_param)}).get())

        if data_param == UUIDType.PHOTO:
            assert response.status_code == 403
        else:
            assert response.status_code == 200
