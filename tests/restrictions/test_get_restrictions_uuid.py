from uuid import uuid4

import allure
import pytest

from models.error import Error
from models.restriction import Restriction
from utils.restriction_data import RestrictionDataType


class TestGetRestrictionsUuid:
    def test_should_return_200(self, api_client, new_restriction):
        response_subject = (api_client.as_admin().restrictions().
                            uuid(new_restriction(RestrictionDataType.FEDERAL_MSC).uuid).get())

        assert response_subject.status_code == 200

    def test_should_return_valid_model(self, api_client, new_restriction):
        restriction = new_restriction(RestrictionDataType.FEDERAL_MSC)
        response = api_client.as_admin().restrictions().uuid(restriction.uuid).get()

        response_entity = Restriction.model_validate(response.json())

        assert response_entity == restriction

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3053/")
    def test_should_return_401(self, api_client, new_restriction):
        response = (api_client.restrictions().
                    uuid(new_restriction(RestrictionDataType.FEDERAL_MSC).uuid).get())

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    def test_should_return_403(self, api_client, new_restriction):
        response = (api_client.as_atm_admin_moscow().restrictions().
                    uuid(new_restriction(RestrictionDataType.FEDERAL_MSC).uuid).get())

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3051/")
    def test_should_return_404(self, api_client):
        response = api_client.as_admin().restrictions().uuid(uuid4()).get()

        assert response.status_code == 404
        assert Error.model_validate(response.json())

    def test_should_return_422(self, api_client):
        response = api_client.as_admin().aerial_photos().get('/wrong-uuid')

        assert response.status_code == 422
        assert Error.model_validate(response.json())

    def test_should_return_500(self, api_client):
        response = api_client.as_admin().restrictions().uuid(uuid4()).get()

        assert response.status_code == 500
        assert Error.model_validate(response.json())

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_default(self, api_client, new_restriction, data_param):
        response = (api_client.as_default().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_pilot(self, api_client, new_restriction, data_param):
        response = (api_client.as_pilot().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_browsing_dispatcher(self, api_client, new_restriction, data_param):
        response = (api_client.as_browsing_dispatcher().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_dispatcher_gc(self, api_client, new_restriction, data_param):
        response = (api_client.as_dispatcher_gc().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_atm_dispatcher(self, api_client, new_restriction, data_param):
        response = (api_client.as_atm_dispatcher_moscow().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_admin(self, api_client, new_restriction, data_param):
        response = api_client.as_admin().restrictions().uuid(new_restriction(data_param).uuid).get()

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_atm_admin(self, api_client, new_restriction, data_param):
        response = (api_client.as_atm_admin_moscow().restrictions().
                    uuid(new_restriction(data_param).uuid).get())
        assert response.status_code == 403

    @pytest.mark.skip("can't create super admin via SPPI UI")
    @pytest.mark.access
    def test_access_super_admin(self):
        pass

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_aircompany(self, api_client, new_restriction, data_param):
        response = (api_client.as_aircompany().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_subject_representative(self, api_client, new_restriction, data_param):
        response = (api_client.as_subject_representative_moscow().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        if data_param == RestrictionDataType.FEDERAL_MSC:
            assert response.status_code == 200
        else:
            assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_lsg_representative(self, api_client, new_restriction, data_param):
        response = (api_client.as_lsg_representative_moscow().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_mod_representative(self, api_client, new_restriction, data_param):
        response = (api_client.as_mod_representative().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_gosaviaciya_mo(self, api_client, new_restriction, data_param):
        response = (api_client.as_gosaviaciya_mo().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_gosaviaciya_fsb(self, api_client, new_restriction, data_param):
        response = (api_client.as_gosaviaciya_fsb().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_gosaviaciya_fso(self, api_client, new_restriction, data_param):
        response = (api_client.as_gosaviaciya_fso().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_gosaviaciya_mvd(self, api_client, new_restriction, data_param):
        response = (api_client.as_gosaviaciya_mvd().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_gosaviaciya_vv_mvd_rf(self, api_client, new_restriction, data_param):
        response = (api_client.as_gosaviaciya_vv_mvd_rf().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_gosaviaciya_mchs(self, api_client, new_restriction, data_param):
        response = (api_client.as_gosaviaciya_mchs().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_gosaviaciya_dosaaf(self, api_client, new_restriction, data_param):
        response = (api_client.as_gosaviaciya_dosaaf().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_gosaviaciya_custom(self, api_client, new_restriction, data_param):
        response = (api_client.as_gosaviaciya_custom().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_experimental_aviation(self, api_client, new_restriction, data_param):
        response = (api_client.as_experimental_aviation().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_aeroinfo(self, api_client, new_restriction, data_param):
        response = (api_client.as_aeroinfo_uuuwzdzx().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_svs_pilot(self, api_client, new_restriction, data_param):
        response = (api_client.as_svs_pilot().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_spw_manager(self, api_client, new_restriction, data_param):
        response = (api_client.as_spw_manager().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_mr_submission_manager(self, api_client, new_restriction, data_param):
        response = (api_client.as_mr_submission_manager().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_shar_pilot(self, api_client, new_restriction, data_param):
        response = (api_client.as_shar_pilot().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_aer_pilot(self, api_client, new_restriction, data_param):
        response = (api_client.as_aer_pilot().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 200

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_MSC
    ])
    def test_access_bla_pilot(self, api_client, new_restriction, data_param):
        response = (api_client.as_bla_pilot().restrictions().
                    uuid(new_restriction(data_param).uuid).get())

        assert response.status_code == 200
