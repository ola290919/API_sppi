from uuid import uuid4

import allure
import pytest
from faker import Faker

from models.aerial_photo import AerialPhoto
from models.error import Error
from models.new_aerial_photo import NewAerialPhoto, NewAerialPhotoFactory


class TestPutAerialPhotosUuid:
    def test_should_return_204(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_admin().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 204

    def test_should_get_updated_model(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        api_client.as_admin().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        response = api_client.as_admin().aerial_photos().uuid(aerial_photo.uuid).get()
        updated_entity = AerialPhoto.model_validate(response.json())

        assert updated_entity != new_aerial_photo

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3053/")
    def test_should_return_401(self, api_client, aerial_photo):
        response = api_client.aerial_photos().uuid(aerial_photo.uuid).put()

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    def test_should_return_403(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_gosaviaciya_fsb().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    def test_should_return_404(self, api_client):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_admin().aerial_photos().uuid(uuid4()).put(json=new_aerial_photo.model_dump())

        assert response.status_code == 404
        assert Error.model_validate(response.json())

    def test_should_return_422(self, api_client, aerial_photo):
        response = api_client.as_admin().aerial_photos().uuid(aerial_photo.uuid).put(json={'n': 1})

        assert response.status_code == 422

    def test_should_return_500(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build(name=Faker().text(max_nb_chars=10000))

        response = api_client.as_admin().aerial_photos().uuid(aerial_photo.uuid).put(json=new_aerial_photo.model_dump())

        assert response.status_code == 500
        assert Error.model_validate(response.json())

    @pytest.mark.access
    def test_access_default(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_default().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_pilot(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_pilot().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_browsing_dispatcher(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_browsing_dispatcher().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_dispatcher_gc(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_dispatcher_gc().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_atm_dispatcher(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = (api_client.as_atm_dispatcher_moscow().aerial_photos().
                    uuid(aerial_photo.uuid).put(json=new_aerial_photo.model_dump()))

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_admin(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_admin().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 204

    @pytest.mark.access
    def test_access_atm_admin(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_atm_admin_moscow().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.skip("can't create super admin via SPPI UI")
    @pytest.mark.access
    def test_access_super_admin(self, api_client):
        pass

    @pytest.mark.access
    def test_access_aircompany(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_aircompany().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_subject_representative(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = (api_client.as_subject_representative_moscow().aerial_photos().
                    uuid(aerial_photo.uuid).put(json=new_aerial_photo.model_dump()))

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_lsg_representative(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = (api_client.as_lsg_representative_moscow().aerial_photos().
                    uuid(aerial_photo.uuid).put(json=new_aerial_photo.model_dump()))

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_mod_representative(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_mod_representative().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 204

    @pytest.mark.access
    def test_access_gosaviaciya_mo(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_gosaviaciya_mo().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_fsb(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_gosaviaciya_fsb().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_fso(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_gosaviaciya_fso().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_mvd(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_gosaviaciya_mvd().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_vv_mvd_rf(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = (api_client.as_gosaviaciya_vv_mvd_rf().aerial_photos().
                    uuid(aerial_photo.uuid).put(json=new_aerial_photo.model_dump()))

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_mchs(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_gosaviaciya_mchs().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_dosaaf(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_gosaviaciya_dosaaf().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_gosaviaciya_custom(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_gosaviaciya_custom().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_experimental_aviation(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = (api_client.as_experimental_aviation().aerial_photos().
                    uuid(aerial_photo.uuid).put(json=new_aerial_photo.model_dump()))

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_aeroinfo(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_aeroinfo_uuuwzdzx().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_svs_pilot(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_svs_pilot().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_spw_manager(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_spw_manager().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_mr_submission_manager(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = (api_client.as_mr_submission_manager().aerial_photos().
                    uuid(aerial_photo.uuid).put(json=new_aerial_photo.model_dump()))

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_shar_pilot(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_shar_pilot().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_aer_pilot(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_aer_pilot().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403

    @pytest.mark.access
    def test_access_bla_pilot(self, api_client, aerial_photo):
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = api_client.as_bla_pilot().aerial_photos().uuid(aerial_photo.uuid).put(
            json=new_aerial_photo.model_dump())

        assert response.status_code == 403
