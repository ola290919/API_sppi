import allure
import pytest
from models.aerial_photos_list import AerialPhotosList, AerialPhotosListGrid
from models.entity_short_list import EntityShortList
from models.error import Error

from .aerial_photo_test_base import AerialPhotoTestBase


class TestGetAerialPhotos(AerialPhotoTestBase):
    def test_should_get_200(self, api_client):
        response = api_client.as_admin().aerial_photos().get()

        assert response.status_code == 200

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3053/")
    def test_should_return_401(self, api_client):
        response = api_client.aerial_photos().get()

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    def test_should_return_403(self, api_client):
        response = api_client.as_dispatcher_gc().aerial_photos().get()

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    def test_should_return_422(self, api_client):
        response = (api_client.as_admin().aerial_photos().
                    query({'detalization': '𐐡𐐝𐐓𐐝𐐇𐐗𐐊𐐤𐐔𐐒𐐋𐐗𐐒'}).get())

        assert response.status_code == 422
        assert Error.model_validate(response.json())

    @pytest.mark.skip("don't know how get 500 error")
    def test_should_return_500(self, api_client):
        pass

    def test_should_has_valid_models(self, api_client):
        response = api_client.as_admin().aerial_photos().get()

        assert AerialPhotosList.model_validate(response.json())

    def test_should_has_valid_models_with_detalization_self(self, api_client):
        response = api_client.as_admin().aerial_photos().query({'detalization': 'self'}).get()

        assert AerialPhotosList.model_validate(response.json())
        # pass

    def test_should_has_valid_models_with_detalization_detail(self, api_client):
        response = api_client.as_admin().aerial_photos().query({'detalization': 'detail'}).get()

        assert AerialPhotosList.model_validate(response.json())

    def test_should_has_valid_models_with_detalization_grid(self, api_client):
        response = api_client.as_admin().aerial_photos().query({'detalization': 'grid'}).get()

        assert AerialPhotosListGrid.model_validate(response.json())

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3059/")
    def test_should_has_valid_models_with_detalization_short(self, api_client):
        response = api_client.as_admin().aerial_photos().query({'detalization': 'short'}).get()

        assert EntityShortList.model_validate(response.json())

    def test_should_has_valid_models_with_detalization_full(self, api_client):
        response = api_client.as_admin().aerial_photos().query({'detalization': 'full'}).get()

        assert AerialPhotosList.model_validate(response.json())

    def test_should_filter_by_uuid(self, api_client, aerial_photos_list):
        uuid = aerial_photos_list[0].uuid

        response = AerialPhotosList.model_validate(
            api_client.as_admin().aerial_photos().query({'filter[uuid]': uuid}).get().json())

        assert len(response.data) == 1
        assert response.data[0].uuid == uuid

    @pytest.mark.not_stable
    def test_should_filter_by_uuid_list(self, api_client, aerial_photos_list):
        uuid_list = [aerial_photos_list[i].uuid for i in range(3)]

        response = AerialPhotosList.model_validate(
            api_client.as_admin().aerial_photos().query({'filter[uuid]': uuid_list}).get().json())
        assert len(response.data) == 3

        for i in range(3):
            assert response.data[i].uuid == aerial_photos_list[i].uuid

    def test_should_limit(self, api_client, aerial_photos_list):
        response = AerialPhotosList.model_validate(
            api_client.as_admin().aerial_photos().limit(1).get().json())

        assert len(response.data) == 1
        assert len(response.data) < len(aerial_photos_list)

    @pytest.mark.not_stable
    def test_should_offset(self, api_client, aerial_photos_list):
        response = AerialPhotosList.model_validate(
            api_client.as_admin().aerial_photos().limit(1).offset(1).get().json())

        assert response.data[0] == aerial_photos_list[1]

    @pytest.mark.skip("don't have docs what fields included in search")
    def test_should_search(self):
        pass

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3058/")
    def test_should_filter_by_name(self, api_client, aerial_photo):
        name = aerial_photo.name
        filtered_list = AerialPhotosList.model_validate(
            api_client.as_admin().aerial_photos().query({'filter[name]': [name]}).get().json()).data

        assert len(filtered_list) == 1
        assert filtered_list[0].name == name

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3048/")
    def test_should_filter_by_name_list(self, api_client):
        names_list = []
        for _ in range(2):
            obj = api_client.create_aerial_photo()
            names_list.append(obj.name)
            self._add_entry_for_deletion(obj)

        filtered_list = AerialPhotosList.model_validate(api_client.as_admin().aerial_photos().
                                                        query({'filter[name]': names_list}).
                                                        get().json()).data
        assert len(filtered_list) == 2
        assert [entity.name for entity in filtered_list] == names_list

    def test_should_sort_by_name_asc(self, api_client):
        uuids_list = []
        for _ in range(3):
            response = api_client.create_aerial_photo()
            uuids_list.append(response.uuid)
            self._add_entry_for_deletion(response)

        unsorted_list = AerialPhotosList.model_validate(api_client.as_admin().aerial_photos().
                                                        query({'filter[uuid]': uuids_list}).
                                                        get().json()).data
        sorted_list_asc = AerialPhotosList.model_validate(api_client.as_admin().aerial_photos().
                                                          query({'filter[uuid]': uuids_list,
                                                                 'sort[name]': 'asc'}).
                                                          get().json()).data

        assert (sorted([entity.name for entity in unsorted_list]) == [entity.name for entity in sorted_list_asc])

    def test_should_sort_by_name_desc(self, api_client):
        uuids_list = []
        for _ in range(3):
            response = api_client.create_aerial_photo()
            uuids_list.append(response.uuid)
            self._add_entry_for_deletion(response)

        unsorted_list = AerialPhotosList.model_validate(api_client.as_admin().aerial_photos().
                                                        query({'filter[uuid]': uuids_list}).
                                                        get().json()).data
        sorted_list_desc = AerialPhotosList.model_validate(api_client.as_admin().aerial_photos().
                                                           query({'filter[uuid]': uuids_list,
                                                                  'sort[name]': 'desc'}).
                                                           get().json()).data

        assert (sorted([entity.name for entity in unsorted_list], reverse=True) ==
                [entity.name for entity in sorted_list_desc])

    @pytest.mark.access
    def test_access_default(self, api_client):
        response = api_client.as_default().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_pilot(self, api_client):
        response = api_client.as_pilot().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_browsing_dispatcher(self, api_client):
        response = api_client.as_browsing_dispatcher().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_dispatcher_gc(self, api_client):
        response = api_client.as_dispatcher_gc().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_atm_dispatcher(self, api_client):
        response = api_client.as_atm_dispatcher_moscow().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_admin(self, api_client):
        response = api_client.as_admin().aerial_photos().get()

        assert response.status_code == 200

    @pytest.mark.access
    def test_access_atm_admin(self, api_client):
        response = api_client.as_atm_admin_moscow().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.skip("can't create super admin via SPPI UI")
    @pytest.mark.access
    def test_access_super_admin(self, api_client):
        pass

    @pytest.mark.access
    def test_access_aircompany(self, api_client):
        response = api_client.as_aircompany().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_subject_representative(self, api_client):
        response = api_client.as_subject_representative_moscow().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_lsg_representative(self, api_client):
        response = api_client.as_lsg_representative_moscow().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_mod_representative(self, api_client):
        response = api_client.as_mod_representative().aerial_photos().get()

        assert response.status_code == 200

    @pytest.mark.access
    def test_access_gosaviaciya_mo(self, api_client):
        response = api_client.as_gosaviaciya_mo().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_fsb(self, api_client):
        response = api_client.as_gosaviaciya_fsb().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_fso(self, api_client):
        response = api_client.as_gosaviaciya_fso().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_mvd(self, api_client):
        response = api_client.as_gosaviaciya_mvd().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_vv_mvd_rf(self, api_client):
        response = api_client.as_gosaviaciya_vv_mvd_rf().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_mchs(self, api_client):
        response = api_client.as_gosaviaciya_mchs().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_dosaaf(self, api_client):
        response = api_client.as_gosaviaciya_dosaaf().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_custom(self, api_client):
        response = api_client.as_gosaviaciya_custom().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_experimental_aviation(self, api_client):
        response = api_client.as_experimental_aviation().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_aeroinfo(self, api_client):
        response = api_client.as_aeroinfo_uuuwzdzx().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_svs_pilot(self, api_client):
        response = api_client.as_svs_pilot().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_spw_manager(self, api_client):
        response = api_client.as_spw_manager().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_mr_submission_manager(self, api_client):
        response = api_client.as_mr_submission_manager().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_shar_pilot(self, api_client):
        response = api_client.as_shar_pilot().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_aer_pilot(self, api_client):
        response = api_client.as_aer_pilot().aerial_photos().get()

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_bla_pilot(self, api_client):
        response = api_client.as_bla_pilot().aerial_photos().get()

        assert response.status_code == 403
