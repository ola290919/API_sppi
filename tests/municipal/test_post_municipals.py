import allure
import pytest
from faker import Faker

from models.error import Error
from models.municipal import Municipal
from models.new_municipal_entity import NewMunicipal, NewMunicipalFactory
from .municipal_test_base import MunicipalsTestBase


class TestPostMunicipals(MunicipalsTestBase):
    def test_should_return_201(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = api_client.as_admin().municipals().post(json=new_municipal_entity.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 201

    def test_should_return_valid_model(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = api_client.as_admin().municipals().post(json=new_municipal_entity.model_dump())
        self._add_entry_for_deletion(response)

        assert Municipal.model_validate(response.json())

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3053/")
    def test_should_return_401(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = api_client.municipals().post(json=new_municipal_entity.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    def test_should_return_403(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_atm_dispatcher_moscow().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    @pytest.mark.skip("don't know what is definition of duplicate")
    def test_should_return_409(self, api_client):
        pass

    def test_should_return_422(self, api_client):
        response = api_client.as_admin().municipals().post(json={'name': '語學研究所'})

        self._add_entry_for_deletion(response)

        assert response.status_code == 422
        assert Error.model_validate(response.json())

    def test_should_return_500(self, api_client):
        response = api_client.as_admin().municipals().post(
            json={'name': f'{Faker().text(max_nb_chars=10000)}',
                  'federal_entity_uuid': '558641de-0de5-4b24-a28d-5e658d28f97a',
                  'details': {'registered_in_sppi': True}})
        self._add_entry_for_deletion(response)

        assert response.status_code == 500
        assert Error.model_validate(response.json())

    @pytest.mark.access
    def test_access_default(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = api_client.as_default().municipals().post(json=new_municipal_entity.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_pilot(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = api_client.as_pilot().municipals().post(json=new_municipal_entity.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_browsing_dispatcher(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_browsing_dispatcher().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_dispatcher_gc(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_dispatcher_gc().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_atm_dispatcher(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_atm_dispatcher_moscow().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_admin(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = api_client.as_admin().municipals().post(json=new_municipal_entity.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 201

    @pytest.mark.access
    def test_access_atm_admin(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_atm_admin_moscow().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.skip("can't create super admin via SPPI UI")
    @pytest.mark.access
    def test_access_super_admin(self, api_client):
        pass

    @pytest.mark.access
    def test_access_aircompany(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_aircompany().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_subject_representative(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_subject_representative_moscow().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_lsg_representative(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_lsg_representative_moscow().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_mod_representative(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_mod_representative().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_mo(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_gosaviaciya_mo().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_fsb(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_gosaviaciya_fsb().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_fso(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_gosaviaciya_fso().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_mvd(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_gosaviaciya_mvd().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_vv_mvd_rf(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_gosaviaciya_vv_mvd_rf().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_mchs(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_gosaviaciya_mchs().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_dosaaf(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_gosaviaciya_dosaaf().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_custom(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_gosaviaciya_custom().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_experimental_aviation(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_experimental_aviation().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_aeroinfo(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_aeroinfo_uuuwzdzx().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_svs_pilot(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_svs_pilot().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_spw_manager(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_spw_manager().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_mr_submission_manager(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_mr_submission_manager().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_shar_pilot(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_shar_pilot().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_aer_pilot(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_aer_pilot().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_bla_pilot(self, api_client):
        new_municipal_entity: NewMunicipal = NewMunicipalFactory.build()

        response = (api_client.as_bla_pilot().municipals().
                    post(json=new_municipal_entity.model_dump()))
        self._add_entry_for_deletion(response)

        assert response.status_code == 403
