import os
from uuid import uuid4

import allure
import pytest

from models.error import Error
from models.municipal import Municipal
from models.patch_details import PatchDetails, PatchDetailsFactory


class TestPatchMunicipalUuidDetails:
    @allure.epic('Status code')
    @allure.feature('204')
    @allure.story('municipals')
    def test_should_return_204(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = api_client.as_admin().municipals().uuid(municipal_entity.uuid).details().patch(
            json=patch_details.model_dump())

        assert response.status_code == 204

    @allure.epic('Updated model')
    @allure.feature('municipals')
    def test_should_get_updated_model(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()
        api_client.as_admin().municipals().uuid(municipal_entity.uuid).details().patch(
            json=patch_details.model_dump())

        response = api_client.as_admin().municipals().uuid(municipal_entity.uuid).get()
        updated_entity = Municipal.model_validate(response.json())

        assert PatchDetails(**updated_entity.details.model_dump()) == patch_details

    @allure.epic('Status code')
    @allure.feature('401')
    @allure.story('municipals')
    def test_should_return_401(self, api_client, municipal_entity):
        response = api_client.municipals().uuid(municipal_entity.uuid).details().patch()

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('403')
    @allure.story('municipals')
    def test_should_return_403(self, api_client, municipal_entity):
        response = api_client.as_mod_representative().municipals().uuid(
            municipal_entity.uuid).details().patch()

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('404')
    @allure.story('municipals')
    def test_should_return_404(self, api_client):
        response = api_client.as_admin().municipals().uuid(uuid4()).details().patch()

        assert response.status_code == 404
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('422')
    @allure.story('municipals')
    def test_should_return_422(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()
        wrong_patch_details = patch_details.model_dump()
        wrong_patch_details['registered_in_sppi'] = '･✿ヾ╲(｡◕‿◕｡)╱✿･'
        response = api_client.as_admin().municipals().uuid(municipal_entity.uuid).details().patch(
            json=wrong_patch_details)

        assert response.status_code == 422
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('500')
    @allure.story('municipals')
    @pytest.mark.skip("don't know how to get 500 error")
    def test_should_return_500(self):
        pass

    @allure.epic('Access')
    @allure.feature('default')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_default(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = api_client.as_default().municipals().uuid(municipal_entity.uuid).details().patch(
            json=patch_details.model_dump())

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('pilot')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_pilot(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = api_client.as_pilot().municipals().uuid(municipal_entity.uuid).details().patch(
            json=patch_details.model_dump())

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('browsing_dispatcher')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_browsing_dispatcher(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_browsing_dispatcher().municipals().uuid(municipal_entity.uuid).
                    details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('dispatcher_gc')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_dispatcher_gc(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_dispatcher_gc().municipals().uuid(municipal_entity.uuid).
                    details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('atm_dispatcher')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_atm_dispatcher(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_atm_dispatcher_moscow().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('admin')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_admin(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_admin().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 204

    @allure.epic('Access')
    @allure.feature('atm_admin')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_atm_admin(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_atm_admin_moscow().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('super_admin')
    @allure.story('municipals')
    @pytest.mark.skip("can't create super admin via SPPI UI")
    @pytest.mark.access
    def test_access_super_admin(self, api_client):
        pass

    @allure.epic('Access')
    @allure.feature('aircompany')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_aircompany(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_aircompany().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('subject_representative')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_subject_representative(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_subject_representative_moscow().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('lsg_representative')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_lsg_representative(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_lsg_representative_moscow().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('lsg_representative_own')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_lsg_representative_own(self, api_client):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_lsg_representative_moscow().municipals().
                    uuid(os.getenv('SPPI_LSG_REPRESENTATIVE_MOSCOW_UUID')).
                    details().patch(json=patch_details.model_dump()))

        assert response.status_code == 204

    @allure.epic('Access')
    @allure.feature('mod_representative')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_mod_representative(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_mod_representative().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mo')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_mo(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_gosaviaciya_mo().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_fsb')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_fsb(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_gosaviaciya_fsb().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_fso')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_fso(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_gosaviaciya_fso().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mvd')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_mvd(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_gosaviaciya_mvd().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_vv_mvd_rf')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_vv_mvd_rf(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_gosaviaciya_vv_mvd_rf().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mchs')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_mchs(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_gosaviaciya_mchs().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_dosaaf')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_dosaaf(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_gosaviaciya_dosaaf().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_custom')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_custom(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_gosaviaciya_custom().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('experimental_aviation')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_experimental_aviation(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_experimental_aviation().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('aeroinfo')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_aeroinfo(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_aeroinfo_uuuwzdzx().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('svs_pilot')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_svs_pilot(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_svs_pilot().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('spw_manager')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_spw_manager(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_spw_manager().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('mr_submission_manager')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_mr_submission_manager(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_mr_submission_manager().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('shar_pilot')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_shar_pilot(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_shar_pilot().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('aer_pilot')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_aer_pilot(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_aer_pilot().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('bla_pilot')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_bla_pilot(self, api_client, municipal_entity):
        patch_details: PatchDetails = PatchDetailsFactory.build()

        response = (api_client.as_bla_pilot().municipals().
                    uuid(municipal_entity.uuid).details().patch(json=patch_details.model_dump()))

        assert response.status_code == 403
