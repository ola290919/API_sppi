from uuid import uuid4

import allure
import pytest

from models.error import Error
from .aerial_photo_test_base import AerialPhotoTestBase


class TestDeleteAerialPhotosUuidTest(AerialPhotoTestBase):
    @allure.epic('Status code')
    @allure.feature('200')
    @allure.story('aerial-photo')
    def test_should_return_204(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = api_client.as_admin().aerial_photos().uuid(aerial_photo.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 204

    @allure.epic('Status code')
    @allure.feature('401')
    @allure.story('aerial-photo')
    def test_should_return_401(self, api_client, aerial_photo):
        response = api_client.aerial_photos().uuid(aerial_photo.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('403')
    @allure.story('aerial-photo')
    def test_should_return_403(self, api_client, aerial_photo):
        response = api_client.as_atm_admin_moscow().aerial_photos().uuid(aerial_photo.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('404')
    @allure.story('aerial-photo')
    def test_should_return_404(self, api_client):
        response = api_client.as_admin().aerial_photos().uuid(uuid4()).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 404
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('422')
    @allure.story('aerial-photo')
    def test_should_return_422(self, api_client):
        response = api_client.as_admin().aerial_photos().uuid(1).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 422
        assert Error.model_validate(response.json())

    @allure.epic('Status code')
    @allure.feature('500')
    @allure.story('aerial-photo')
    @pytest.mark.skip("don't know how to get 500 error")
    def test_should_return_500(self):
        pass

    @allure.epic('Access')
    @allure.feature('default')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_default(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = api_client.as_default().aerial_photos().uuid(aerial_photo.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('pilot')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_pilot(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = api_client.as_pilot().aerial_photos().uuid(aerial_photo.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('browsing_dispatcher')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_browsing_dispatcher(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_browsing_dispatcher().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('dispatcher_gc')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_dispatcher_gc(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = api_client.as_dispatcher_gc().aerial_photos().uuid(aerial_photo.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('atm_dispatcher')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_atm_dispatcher(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_atm_dispatcher_moscow().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('admin')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_admin(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = api_client.as_admin().aerial_photos().uuid(aerial_photo.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 204

    @allure.epic('Access')
    @allure.feature('atm_admin')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_atm_admin(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_atm_admin_moscow().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('super_admin')
    @allure.story('aerial-photo')
    @pytest.mark.skip("can't create super admin via SPPI UI")
    @pytest.mark.access
    def test_access_super_admin(self, api_client):
        pass

    @allure.epic('Access')
    @allure.feature('aircompany')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_aircompany(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = api_client.as_aircompany().aerial_photos().uuid(aerial_photo.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('subject_representative')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_subject_representative(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_subject_representative_moscow().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('lsg_representative')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_lsg_representative(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_lsg_representative_moscow().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('mod_representative')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_mod_representative(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_mod_representative().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 204

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mo')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_gosaviaciya_mo(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_gosaviaciya_mo().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_fsb')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_gosaviaciya_fsb(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_gosaviaciya_fsb().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_fso')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_gosaviaciya_fso(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_gosaviaciya_fso().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mvd')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_gosaviaciya_mvd(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_gosaviaciya_mvd().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_vv_mvd_rf')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_gosaviaciya_vv_mvd_rf(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_gosaviaciya_vv_mvd_rf().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_mchs')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_gosaviaciya_mchs(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_gosaviaciya_mchs().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_dosaaf')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_gosaviaciya_dosaaf(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_gosaviaciya_dosaaf().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('gosaviaciya_custom')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_gosaviaciya_custom(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_gosaviaciya_custom().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('experimental_aviation')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_experimental_aviation(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_experimental_aviation().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('aeroinfo')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_aeroinfo(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_aeroinfo_uuuwzdzx().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('svs_pilot')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_svs_pilot(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = api_client.as_svs_pilot().aerial_photos().uuid(aerial_photo.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('spw_manager')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_spw_manager(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = api_client.as_spw_manager().aerial_photos().uuid(aerial_photo.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('mr_submission_manager')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_mr_submission_manager(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = (api_client.as_mr_submission_manager().aerial_photos().
                    uuid(aerial_photo.uuid).delete())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('shar_pilot')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_shar_pilot(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = api_client.as_shar_pilot().aerial_photos().uuid(aerial_photo.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('aer_pilot')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_aer_pilot(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = api_client.as_aer_pilot().aerial_photos().uuid(aerial_photo.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @allure.epic('Access')
    @allure.feature('bla_pilot')
    @allure.story('aerial-photo')
    @pytest.mark.access
    def test_access_bla_pilot(self, api_client):
        aerial_photo = api_client.create_aerial_photo()

        response = api_client.as_bla_pilot().aerial_photos().uuid(aerial_photo.uuid).delete()
        self._add_entry_for_deletion(response)

        assert response.status_code == 403
