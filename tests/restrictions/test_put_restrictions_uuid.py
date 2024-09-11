from uuid import uuid4

import allure
import pytest

from models.error import Error
from utils.restriction_data import RestrictionDataType


class TestPutRestrictionsUuid:
    @allure.epic('Status code')
    @allure.feature('204')
    @allure.story('restrictions')
    def test_should_return_204(self, api_client, restriction_build, new_restriction):
        data = restriction_build(RestrictionDataType.FEDERAL_MSC)
        response = (api_client.as_admin().restrictions().
                    uuid(new_restriction(RestrictionDataType.FEDERAL_MSC).uuid).put(json=data.model_dump()))

        assert response.status_code == 204

    @allure.epic('Updated model')
    @allure.feature('restrictions')
    def test_should_get_updated_model(self, api_client, restriction_build, new_restriction):
        data = restriction_build(RestrictionDataType.FEDERAL_MSC)

        response = (
            api_client.
            as_admin().
            restrictions().
            uuid(new_restriction(RestrictionDataType.FEDERAL_MSC).uuid)
            .get()
        )
        (
            api_client.
            as_admin().
            restrictions().
            uuid(response.json()['uuid']).
            put(json=data.model_dump())
        )
        response_update = (
            api_client.
            as_admin().
            restrictions().
            uuid(response.json()['uuid']).get()
        )

        assert response.text != response_update.text

    @allure.epic('Status code')
    @allure.feature('401')
    @allure.story('restrictions')
    def test_should_return_401(self, api_client, new_restriction, restriction_build):
        data = restriction_build(RestrictionDataType.FEDERAL_MSC)
        response = (api_client.restrictions().uuid(new_restriction(RestrictionDataType.FEDERAL_MSC).uuid).
                    put(json=data.model_dump()))

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('403')
    @allure.story('restrictions')
    def test_should_return_403(self, api_client, restriction_build, new_restriction):
        data = restriction_build(RestrictionDataType.FEDERAL_MSC)
        response = (api_client.as_svs_pilot().restrictions().
                    uuid(new_restriction(RestrictionDataType.FEDERAL_MSC).uuid).put(json=data.model_dump()))

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('404')
    @allure.story('restrictions')
    def test_should_return_404(self, api_client, restriction_build):
        data = restriction_build(RestrictionDataType.FEDERAL_MSC)
        response = api_client.as_admin().restrictions().uuid(uuid4()).put(json=data.model_dump())

        assert response.status_code == 404
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('422')
    @allure.story('restrictions')
    def test_should_return_422(self, api_client, new_restriction):
        response = (api_client.as_admin().restrictions().
                    uuid(new_restriction(RestrictionDataType.FEDERAL_MSC).uuid).put(json={'n': 1}))

        assert response.status_code == 422

    @allure.epic('Status code')
    @allure.feature('500')
    @allure.story('restrictions')
    def test_should_return_500(self, api_client, restriction_build, new_restriction):
        data = restriction_build(RestrictionDataType.FEDERAL_MSC).model_dump()
        data['restriction_type'] = 'ัะรพีัะำีัะ้เดิอระพืิืิืปแอิืิแืทืิทททิทื'
        response = (api_client.as_admin().restrictions().
                    uuid(new_restriction(RestrictionDataType.FEDERAL_MSC).uuid).put(json=data))

        assert response.status_code == 500
        assert Error.model_validate(response.json())

    @allure.epic('Access')
    @allure.feature('default')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_default(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_default().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('pilot')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_pilot(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_pilot().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('browsing_dispatcher')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_browsing_dispatcher(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_browsing_dispatcher().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('dispatcher_gc')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_dispatcher_gc(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_dispatcher_gc().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('atm_dispatcher')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_atm_dispatcher(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_atm_dispatcher_moscow().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('admin')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_admin(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_admin().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 204

    @allure.epic('Access')
    @allure.feature('atm_admin')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_atm_admin(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_atm_admin_moscow().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('aircompany')
    @allure.story('restrictions')
    @pytest.mark.skip("can't create super admin via SPPI UI")
    @pytest.mark.access
    def test_access_super_admin(self):
        pass

    @allure.epic('Access')
    @allure.feature('aircompany')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_aircompany(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_aircompany().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('subject_representative')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.FEDERAL_SPB
    ])
    def test_access_subject_representative(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_subject_representative_moscow().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        if data_param == RestrictionDataType.FEDERAL_MSC:
            assert response.status_code == 204
        else:
            assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('lsg_representative')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.FEDERAL_SPB
    ])
    def test_access_lsg_representative(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_lsg_representative_moscow().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        if data_param == RestrictionDataType.MUNICIPAL_MSC:
            assert response.status_code == 204
        else:
            assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('mod_representative')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_mod_representative(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_mod_representative().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mo')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_mo(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_gosaviaciya_mo().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_fsb')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_fsb(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_gosaviaciya_fsb().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_fso')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_fso(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_gosaviaciya_fso().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mvd')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_mvd(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_gosaviaciya_mvd().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_vv_mvd_rf')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_vv_mvd_rf(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_gosaviaciya_vv_mvd_rf().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mchs')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_mchs(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_gosaviaciya_mchs().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_dosaaf')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_dosaaf(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_gosaviaciya_dosaaf().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_custom')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_custom(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_gosaviaciya_custom().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('experimental_aviation')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_experimental_aviation(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_experimental_aviation().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('aeroinfo')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_aeroinfo(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_aeroinfo_uuuwzdzx().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('svs_pilot')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_svs_pilot(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_svs_pilot().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('spw_manager')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_spw_manager(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_spw_manager().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('mr_submission_manager')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_mr_submission_manager(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_mr_submission_manager().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('shar_pilot')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_shar_pilot(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_shar_pilot().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('aer_pilot')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_aer_pilot(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_aer_pilot().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('bla_pilot')
    @allure.story('restrictions')
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_bla_pilot(self, api_client, restriction_build, new_restriction, data_param):
        data = restriction_build(data_param)
        response = (api_client.as_bla_pilot().restrictions().
                    uuid(new_restriction(data_param).uuid).put(json=data.model_dump()))

        assert response.status_code == 403
