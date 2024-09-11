import allure
import pytest

from models.error import Error
from models.geometries_list import GeometriesList
from utils.uuid_fetcher import UUIDType


class TestGetGeometries:

    @allure.epic('Status code')
    @allure.feature('200')
    @allure.story('geometries')
    def test_should_get_200(self, api_client, uuid_data, data_param):
        response = api_client.as_admin().geometries().query({'uuid': uuid_data(UUIDType.SUBJECT)}).get()

        assert response.status_code == 200

    @allure.epic('Valid model')
    @allure.feature('without detalization')
    @allure.story('geometries')
    def test_should_return_valid_model(self, api_client, uuid_data):
        # TODO need to get a valid uuid with full geometry to check its model
        response = api_client.as_admin().geometries().query({'uuid': uuid_data(UUIDType.SUBJECT)}).get()

        assert GeometriesList.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('401')
    @allure.story('geometries')
    def test_should_return_401(self, api_client, uuid_data):
        response = api_client.geometries().query({'uuid': uuid_data(UUIDType.SUBJECT)}).get()

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('403')
    @allure.story('geometries')
    def test_should_return_403(self, api_client, uuid_data):
        response = api_client.as_gosaviaciya_mo().geometries().query({'uuid': uuid_data(UUIDType.SUBJECT)}).get()

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('422')
    @allure.story('geometries')
    @pytest.mark.skip("don't know how to get 422 error")
    def test_should_return_422(self, api_client):
        pass

    @allure.epic('Status code')
    @allure.feature('500')
    @allure.story('geometries')
    @pytest.mark.skip("don't know how to get 500 error")
    def test_should_return_500(self):
        pass

    @allure.epic('Parameters')
    @allure.feature('different_uuid')
    @allure.story('geometries')
    @pytest.mark.parametrize("data_param", [
        UUIDType.FEDERAL,
        UUIDType.MUNICIPAL,
        UUIDType.PHOTO,
        UUIDType.RESTRICTION_SUBJECT,
        UUIDType.RESTRICTION_LSG
    ])
    def test_should_take_different_uuid(self, api_client, uuid_data, data_param):
        response = api_client.as_admin().geometries().query({'uuid': uuid_data(data_param)}).get()

        assert response.status_code == 200

    @allure.epic('Parameters')
    @allure.feature('limit')
    @allure.story('geometries')
    @pytest.mark.skip("need an uuid with more that one geometry")
    def test_should_limit(self):
        pass

    @allure.epic('Parameters')
    @allure.feature('offset')
    @allure.story('geometries')
    @pytest.mark.skip("need an uuid with more that one geometry")
    def test_should_offset(self):
        pass

    @allure.epic('Access')
    @allure.feature('default')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('pilot')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('browsing_dispatcher')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('dispatcher_gc')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('atm_dispatcher')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('admin')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('atm_admin')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('super_admin')
    @allure.story('geometries')
    @pytest.mark.skip("can't create super admin via SPPI UI")
    @pytest.mark.access
    def test_access_super_admin(self):
        pass

    @allure.epic('Access')
    @allure.feature('aircompany')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('subject_representative')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('lsg_representative')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('mod_representative')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mo')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_fsb')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_fso')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mvd')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_vv_mvd_rf')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mchs')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_dosaaf')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('gosaviaciya_custom')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('experimental_aviation')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('aeroinfo')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('svs_pilot')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('spw_manager')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('mr_submission_manager')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('shar_pilot')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('aer_pilot')
    @allure.story('geometries')
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

    @allure.epic('Access')
    @allure.feature('bla_pilot')
    @allure.story('geometries')
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
