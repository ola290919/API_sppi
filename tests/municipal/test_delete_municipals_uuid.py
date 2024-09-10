from uuid import uuid4

import allure
import pytest

from models.error import Error
from .municipal_test_base import MunicipalsTestBase


class TestDeleteMunicipalsUuid(MunicipalsTestBase):
    def test_should_return_204(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_admin().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 204

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3053/")
    def test_should_return_401(self, api_client, municipal_entity):
        response = api_client.municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    def test_should_return_403(self, api_client, municipal_entity):
        response = (api_client.as_atm_admin_moscow().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    def test_should_return_404(self, api_client):
        response = api_client.as_admin().municipals().uuid(uuid4()).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 404
        assert Error.model_validate(response.json())

    def test_should_return_422(self, api_client):
        response = api_client.as_admin().municipals().uuid(1).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 422
        assert Error.model_validate(response.json())

    @pytest.mark.skip("don't know how to get 500 error")
    def test_should_return_500(self):
        pass

    @pytest.mark.access
    def test_access_default(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_default().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_pilot(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_pilot().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_browsing_dispatcher(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = (api_client.as_browsing_dispatcher().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_dispatcher_gc(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_dispatcher_gc().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_atm_dispatcher(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = (api_client.as_atm_dispatcher_moscow().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_admin(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_admin().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 204

    @pytest.mark.access
    def test_access_atm_admin(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = (api_client.as_atm_admin_moscow().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.skip("can't create super admin via SPPI UI")
    @pytest.mark.access
    def test_access_super_admin(self, api_client):
        pass

    @pytest.mark.access
    def test_access_aircompany(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_aircompany().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_subject_representative(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = (api_client.as_subject_representative_moscow().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_lsg_representative(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = (api_client.as_lsg_representative_moscow().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_mod_representative(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = (api_client.as_mod_representative().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_mo(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_gosaviaciya_mo().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_fsb(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_gosaviaciya_fsb().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_fso(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_gosaviaciya_fso().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_mvd(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_gosaviaciya_mvd().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_vv_mvd_rf(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = (api_client.as_gosaviaciya_vv_mvd_rf().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_mchs(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = (api_client.as_gosaviaciya_mchs().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_dosaaf(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = (api_client.as_gosaviaciya_dosaaf().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_custom(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = (api_client.as_gosaviaciya_custom().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_experimental_aviation(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = (api_client.as_experimental_aviation().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_aeroinfo(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = (api_client.as_aeroinfo_uuuwzdzx().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_svs_pilot(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_svs_pilot().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_spw_manager(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_spw_manager().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_mr_submission_manager(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = (api_client.as_mr_submission_manager().municipals().
                    uuid(municipal_entity.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_shar_pilot(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_shar_pilot().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_aer_pilot(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_aer_pilot().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_bla_pilot(self, api_client):
        municipal_entity = api_client.create_municipal()

        response = api_client.as_bla_pilot().municipals().uuid(municipal_entity.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403
