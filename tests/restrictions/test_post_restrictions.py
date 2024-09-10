import allure
import pytest

from models.error import Error
from models.restriction import Restriction
from utils.restriction_data import RestrictionDataType
from .resrictions_test_base import RestrictionsTestBase


class TestPostRestriction(RestrictionsTestBase):
    def test_should_return_201(self, api_client, restriction_build):
        new = restriction_build(RestrictionDataType.FEDERAL_SPB)

        response = api_client.as_admin().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 201

    def test_should_return_valid_model(self, api_client, restriction_build):
        new = restriction_build(RestrictionDataType.MUNICIPAL_MSC)

        response = api_client.as_admin().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert Restriction.model_validate(response.json())

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3053/")
    def test_should_return_401(self, api_client, restriction_build):
        new = restriction_build(RestrictionDataType.FEDERAL_SPB)

        response = api_client.restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 401
        assert Error.model_validate(response.json())

    def test_should_return_403(self, api_client, restriction_build):
        new = restriction_build(RestrictionDataType.FEDERAL_SPB)

        response = api_client.as_spw_manager().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403
        assert Error.model_validate(response.json())

    @pytest.mark.skip("don't know what is definition of duplicate")
    def test_should_return_409(self, api_client, restriction_build):
        pass

    def test_should_return_422(self, api_client):
        response = api_client.as_admin().restrictions().post(json={'name': ''})
        self._add_entry_for_deletion(response)

        assert response.status_code == 422
        assert Error.model_validate(response.json())

    def test_should_return_500(self, api_client):
        response = api_client.as_admin().restrictions().post(
            json={'object_uuid': '445ef25f-9c1e-49f4-ad5e-fbe3312b90d4',
                  'name': 'er', 'restriction_type': '𐐔𐐇𐐝𐐀𐐡𐐇𐐓𐐡𐐝𐐓𐐝𐐇𐐗𐐊𐐤𐐔𐐒𐐋𐐗𐐒', 'state': 'closed'})
        self._add_entry_for_deletion(response)

        assert response.status_code == 500
        assert Error.model_validate(response.json())

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_default(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_default().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_pilot(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_pilot().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_browsing_dispatcher(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_browsing_dispatcher().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_dispatcher_gc(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_dispatcher_gc().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_atm_dispatcher(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_atm_dispatcher_moscow().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_admin(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_admin().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 201

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_atm_admin(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_atm_admin_moscow().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.skip("can't create super admin via SPPI UI")
    @pytest.mark.access
    def test_access_super_admin(self):
        pass

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_aircompany(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_aircompany().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.FEDERAL_SPB,
    ])
    def test_access_subject_representative(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = (api_client.as_subject_representative_moscow().restrictions().
                    post(json=new.model_dump()))
        self._add_entry_for_deletion(response)

        if data_param == RestrictionDataType.FEDERAL_MSC:
            assert response.status_code == 201
        else:
            assert response.status_code == 403

    @allure.issue("https://yt.monitorsoft.ru/issue/AT-3050/")
    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC,
        RestrictionDataType.MUNICIPAL_KLIN
    ])
    def test_access_lsg_representative(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = (api_client.as_lsg_representative_moscow().restrictions().
                    post(json=new.model_dump()))
        self._add_entry_for_deletion(response)

        if data_param == RestrictionDataType.MUNICIPAL_MSC:
            assert response.status_code == 201
        else:
            assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_mod_representative(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_mod_representative().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_mo(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_gosaviaciya_mo().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_fsb(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_gosaviaciya_fsb().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_fso(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_gosaviaciya_fso().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_mvd(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_gosaviaciya_mvd().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_vv_mvd_rf(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_gosaviaciya_vv_mvd_rf().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_mchs(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_gosaviaciya_mchs().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_dosaaf(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_gosaviaciya_dosaaf().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_gosaviaciya_custom(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_gosaviaciya_custom().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_experimental_aviation(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_experimental_aviation().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_aeroinfo(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_aeroinfo_uuuwzdzx().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_svs_pilot(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_svs_pilot().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_spw_manager(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_spw_manager().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_mr_submission_manager(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_mr_submission_manager().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_shar_pilot(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_shar_pilot().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_aer_pilot(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_aer_pilot().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403

    @pytest.mark.access
    @pytest.mark.parametrize("data_param", [
        RestrictionDataType.MUNICIPAL_MSC,
        RestrictionDataType.FEDERAL_MSC
    ])
    def test_access_bla_pilot(self, api_client, restriction_build, data_param):
        new = restriction_build(data_param)

        response = api_client.as_bla_pilot().restrictions().post(json=new.model_dump())
        self._add_entry_for_deletion(response)

        assert response.status_code == 403
