import random

import allure
import pytest

from models.error import Error
from models.municipal_list import MunicipalList, MunicipalListGrid, MunicipalListDetail, MunicipalListSelf
from models.entity_short_list import EntityShortList
from .municipal_test_base import MunicipalsTestBase


class TestGetMunicipals(MunicipalsTestBase):
    @allure.epic('Status code')
    @allure.feature('200')
    @allure.story('municipals')
    def test_should_get_200(self, api_client):
        response = api_client.as_admin().municipals().get()

        assert response.status_code == 200

    @allure.epic('Status code')
    @allure.feature('401')
    @allure.story('municipals')
    def test_should_return_401(self, api_client):
        response = api_client.municipals().get()

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('403')
    @allure.story('municipals')
    def test_should_return_403(self, api_client):
        response = api_client.as_atm_dispatcher_moscow().municipals().get()

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('422')
    @allure.story('municipals')
    def test_should_return_422(self, api_client):
        response = api_client.as_admin().municipals().query({'detalization': '社會科學院語學研究所'}).get()

        assert response.status_code == 422
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('500')
    @allure.story('municipals')
    @pytest.mark.skip("don't know how get 500 error")
    def test_should_return_500(self, api_client):
        pass

    @allure.epic('Valid model')
    @allure.feature('without detalization')
    @allure.story('municipals')
    def test_should_has_valid_models(self, api_client):
        response = api_client.as_admin().municipals().get()

        assert MunicipalList.model_validate(response.json())

    @allure.epic('Valid model')
    @allure.feature('with detalization')
    @allure.story('municipals')
    def test_should_has_valid_models_with_detalization_self(self, api_client):
        response = api_client.as_admin().municipals().query({'detalization': 'self'}).get()

        assert MunicipalListSelf.model_validate(response.json())

    @allure.epic('Valid model')
    @allure.feature('with detalization')
    @allure.story('municipals')
    def test_should_has_valid_models_with_detalization_detail(self, api_client):
        response = api_client.as_admin().municipals().query({'detalization': 'detail'}).get()

        assert MunicipalListDetail.model_validate(response.json())

    @allure.epic('Valid model')
    @allure.feature('with detalization')
    @allure.story('municipals')
    def test_should_has_valid_models_with_detalization_grid(self, api_client):
        response = api_client.as_admin().municipals().query({'detalization': 'grid'}).get()

        assert MunicipalListGrid.model_validate(response.json())

    @allure.epic('Valid model')
    @allure.feature('with detalization')
    @allure.story('municipals')
    def test_should_has_valid_models_with_detalization_short(self, api_client):
        response = api_client.as_admin().municipals().query({'detalization': 'short'}).get()

        assert EntityShortList.model_validate(response.json())

    @allure.epic('Valid model')
    @allure.feature('with detalization')
    @allure.story('municipals')
    def test_should_has_valid_models_with_detalization_full(self, api_client):
        response = api_client.as_admin().municipals().query({'detalization': 'full'}).get()

        assert MunicipalList.model_validate(response.json())

    @allure.epic('Parameters')
    @allure.feature('filter_by_uuid')
    @allure.story('municipals')
    def test_should_filter_by_uuid(self, api_client, municipals_list):
        uuid = municipals_list[0].uuid

        response = MunicipalList.model_validate(
            api_client.as_admin().municipals().query({'filter[uuid]': uuid}).get().json())

        assert len(response.data) == 1
        assert response.data[0].uuid == uuid

    @allure.epic('Parameters')
    @allure.feature('filter_by_uuid')
    @allure.story('municipals')
    def test_should_filter_by_uuid_list(self, api_client, municipals_list):
        uuid_list = [municipals_list[i].uuid for i in range(2)]

        response = MunicipalList.model_validate(
            api_client.as_admin().municipals().query({'filter[uuid]': uuid_list}).get().json())

        assert len(response.data) == 2

        for i in range(2):
            assert response.data[i].uuid == municipals_list[i].uuid

    @allure.epic('Parameters')
    @allure.feature('limit')
    @allure.story('municipals')
    def test_should_limit(self, api_client, municipals_list):
        response = MunicipalList.model_validate(
            api_client.as_admin().municipals().limit(1).get().json())

        assert len(response.data) == 1
        assert len(response.data) < len(municipals_list)

    @allure.epic('Parameters')
    @allure.feature('offset')
    @allure.story('municipals')
    @pytest.mark.not_stable
    def test_should_offset(self, api_client, municipals_list):
        response = MunicipalList.model_validate(
            api_client.as_admin().municipals().limit(1).offset(1).get().json())

        assert response.data[0] == municipals_list[1]

    @allure.epic('Parameters')
    @allure.feature('search')
    @allure.story('municipals')
    @pytest.mark.skip("don't have docs what fields included in search")
    def test_should_search(self):
        pass

    @allure.epic('Parameters')
    @allure.feature('filter_by_registered_in_sppi')
    @allure.story('municipals')
    def test_should_filter_by_registered_in_sppi_true(self, api_client, municipals_with_registered_in_sppi):
        response = MunicipalList.model_validate(
            api_client.as_admin().municipals().
            query({'filter[registered_in_sppi]': True}).get().json())

        assert response.data[0].details.registered_in_sppi is True

    @allure.epic('Parameters')
    @allure.feature('filter_by_registered_in_sppi')
    @allure.story('municipals')
    def test_should_filter_by_registered_in_sppi_false(self, api_client, municipals_with_registered_in_sppi):
        response = MunicipalList.model_validate(
            api_client.as_admin().municipals().
            query({'filter[registered_in_sppi]': False}).get().json())

        assert response.data[0].details.registered_in_sppi is False

    @allure.epic('Parameters')
    @allure.feature('sort_by_registered_in_sppi')
    @allure.story('municipals')
    def test_should_sort_by_registered_in_sppi_asc(self, api_client, municipals_with_registered_in_sppi):
        response = MunicipalList.model_validate(
            api_client.as_admin().municipals().
            query({'sort[registered_in_sppi]': 'asc'}).get().json())

        assert response.data[0].details.registered_in_sppi is False

    @allure.epic('Parameters')
    @allure.feature('sort_by_registered_in_sppi')
    @allure.story('municipals')
    def test_should_sort_by_registered_in_sppi_desc(self, api_client, municipals_with_registered_in_sppi):
        response = MunicipalList.model_validate(
            api_client.as_admin().municipals().
            query({'sort[registered_in_sppi]': 'desc'}).get().json())

        assert response.data[0].details.registered_in_sppi is True

    @allure.epic('Parameters')
    @allure.feature('filter_by_federal_entity_name')
    @allure.story('municipals')
    def test_should_filter_by_federal_entity_name(self, api_client, municipals_list):
        federal_entity_name = random.choice([municipal.federal_entity.name for municipal in municipals_list])

        filtered_list = MunicipalList.model_validate(
            api_client.as_admin().municipals().query(
                {'filter[federal_entity_name]': federal_entity_name}).get().json()).data

        assert len(filtered_list) >= 1
        assert all(municipal.federal_entity.name == federal_entity_name for municipal in filtered_list)

    @allure.epic('Parameters')
    @allure.feature('filter_by_federal_entity_name')
    @allure.story('municipals')
    def test_should_filter_by_federal_entity_name_list(self, api_client, municipals_list):
        # TODO список может содержать два одинаковых значения
        names_list = random.choices([municipal.federal_entity.name for municipal in municipals_list], k=2)

        filtered_list = MunicipalList.model_validate(
            api_client.as_admin().municipals().
            query({'filter[federal_entity_name]': names_list}).get().json()).data

        assert len(filtered_list) >= 2
        assert all(municipal.federal_entity.name in names_list for municipal in filtered_list)

    @allure.epic('Parameters')
    @allure.feature('filter_by_name')
    @allure.story('municipals')
    def test_should_filter_by_name(self, api_client, municipals_list):
        name = random.choice([municipal.name for municipal in municipals_list])
        filtered_list = MunicipalList.model_validate(
            api_client.as_admin().municipals().query({'filter[name]': name}).get().json()).data

        assert len(filtered_list) >= 1
        assert all(municipal.name == name for municipal in filtered_list)

    @allure.epic('Parameters')
    @allure.feature('filter_by_name')
    @allure.story('municipals')
    def test_should_filter_by_name_list(self, api_client, municipals_list):
        # TODO список может содержать два одинаковых значения
        names_list = random.choices([entity.name for entity in municipals_list], k=2)

        filtered_list = MunicipalList.model_validate(api_client.as_admin().municipals().
                                                     query({'filter[name]': names_list}).
                                                     get().json()).data
        assert len(filtered_list) >= 2
        assert all(entity.name in names_list for entity in filtered_list)

    @allure.epic('Parameters')
    @allure.feature('sort_by_federal_entity_name')
    @allure.story('municipals')
    def test_should_sort_by_federal_entity_name_asc(self, api_client, municipals_with_different_names):
        response = MunicipalList.model_validate(
            api_client.as_admin().municipals().query({'sort[federal_entity_name]': 'asc'}).get().json())

        for i in range(len(response.data) - 1):
            if response.data[i].name != response.data[i + 1].name:
                assert response.data[i].name < response.data[i + 1].name
                break

    @allure.epic('Parameters')
    @allure.feature('sort_by_federal_entity_name')
    @allure.story('municipals')
    def test_should_sort_by_federal_entity_name_asc_desc(self, api_client, municipals_with_different_names):
        response = MunicipalList.model_validate(
            api_client.as_admin().municipals().query({'sort[federal_entity_name]': 'desc'}).get().json())

        for i in range(len(response.data) - 1):
            if response.data[i].name != response.data[i + 1].name:
                assert response.data[i].name > response.data[i + 1].name
                break

    @allure.epic('Parameters')
    @allure.feature('sort_by_name')
    @allure.story('municipals')
    def test_should_sort_by_name_asc(self, api_client, municipals_with_different_names):
        response = MunicipalList.model_validate(
            api_client.as_admin().municipals().query({'sort[name]': 'asc'}).get().json())

        for i in range(len(response.data) - 1):
            if response.data[i].name != response.data[i + 1].name:
                assert response.data[i].name < response.data[i + 1].name
                break

    @allure.epic('Parameters')
    @allure.feature('sort_by_name')
    @allure.story('municipals')
    def test_should_sort_by_name_desc(self, api_client, municipals_with_different_names):
        response = MunicipalList.model_validate(
            api_client.as_admin().municipals().query({'sort[name]': 'desc'}).get().json())

        for i in range(len(response.data) - 1):
            if response.data[i].name != response.data[i + 1].name:
                assert response.data[i].name > response.data[i + 1].name
                break

    @allure.epic('Access')
    @allure.feature('default')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_default(self, api_client):
        response = api_client.as_default().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('pilot')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_pilot(self, api_client):
        response = api_client.as_pilot().municipals().get()

        assert response.status_code == 200

    @allure.epic('Access')
    @allure.feature('browsing_dispatcher')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_browsing_dispatcher(self, api_client):
        response = api_client.as_browsing_dispatcher().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('dispatcher_gc')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_dispatcher_gc(self, api_client):
        response = api_client.as_dispatcher_gc().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('atm_dispatcher')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_atm_dispatcher(self, api_client):
        response = api_client.as_atm_dispatcher_moscow().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('admin')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_admin(self, api_client):
        response = api_client.as_admin().municipals().get()

        assert response.status_code == 200

    @allure.epic('Access')
    @allure.feature('atm_admin')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_atm_admin(self, api_client):
        response = api_client.as_atm_admin_moscow().municipals().get()

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
    def test_access_aircompany(self, api_client):
        response = api_client.as_aircompany().municipals().get()

        assert response.status_code == 200

    @allure.epic('Access')
    @allure.feature('subject_representative')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_subject_representative(self, api_client):
        response = api_client.as_subject_representative_moscow().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('lsg_representative')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_lsg_representative(self, api_client):
        response = api_client.as_lsg_representative_moscow().municipals().get()

        assert response.status_code == 200

    @allure.epic('Access')
    @allure.feature('mod_representative')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_mod_representative(self, api_client):
        response = api_client.as_mod_representative().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mo')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_mo(self, api_client):
        response = api_client.as_gosaviaciya_mo().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_fsb')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_fsb(self, api_client):
        response = api_client.as_gosaviaciya_fsb().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_fso')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_fso(self, api_client):
        response = api_client.as_gosaviaciya_fso().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mvd')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_mvd(self, api_client):
        response = api_client.as_gosaviaciya_mvd().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_vv_mvd_rf')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_vv_mvd_rf(self, api_client):
        response = api_client.as_gosaviaciya_vv_mvd_rf().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mchs')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_mchs(self, api_client):
        response = api_client.as_gosaviaciya_mchs().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_dosaaf')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_dosaaf(self, api_client):
        response = api_client.as_gosaviaciya_dosaaf().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_custom')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_gosaviaciya_custom(self, api_client):
        response = api_client.as_gosaviaciya_custom().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('experimental_aviation')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_experimental_aviation(self, api_client):
        response = api_client.as_experimental_aviation().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('aeroinfo')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_aeroinfo(self, api_client):
        response = api_client.as_aeroinfo_uuuwzdzx().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('svs_pilot')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_svs_pilot(self, api_client):
        response = api_client.as_svs_pilot().municipals().get()

        assert response.status_code == 200

    @allure.epic('Access')
    @allure.feature('spw_manager')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_spw_manager(self, api_client):
        response = api_client.as_spw_manager().municipals().get()

        assert response.status_code == 200

    @allure.epic('Access')
    @allure.feature('mr_submission_manager')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_mr_submission_manager(self, api_client):
        response = api_client.as_mr_submission_manager().municipals().get()

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('shar_pilot')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_shar_pilot(self, api_client):
        response = api_client.as_shar_pilot().municipals().get()

        assert response.status_code == 200

    @allure.epic('Access')
    @allure.feature('aer_pilot')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_aer_pilot(self, api_client):
        response = api_client.as_aer_pilot().municipals().get()

        assert response.status_code == 200

    @allure.epic('Access')
    @allure.feature('bla_pilot')
    @allure.story('municipals')
    @pytest.mark.access
    def test_access_bla_pilot(self, api_client):
        response = api_client.as_bla_pilot().municipals().get()

        assert response.status_code == 200
