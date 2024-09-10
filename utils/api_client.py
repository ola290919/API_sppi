import os
from datetime import datetime, timedelta

from models.aerial_photo import AerialPhoto
from models.federation_entity import FederationEntity
from models.municipal import Municipal
from models.new_aerial_photo import NewAerialPhoto, NewAerialPhotoFactory
from models.new_federation_entity import NewFederationEntityFactory, NewFederationEntity
from models.new_municipal_entity import (NewMunicipal, NewMunicipalFactory)
from utils.base_client import BaseClient
from utils.sppi_api_client import SppiClient


class ApiClient(BaseClient):
    sppi_client: SppiClient

    def __init__(self):
        super().__init__(os.getenv('BASE_URL', 'http://app.sppi.dev.plan/drone-area-registry'))
        self.sppi_client = SppiClient()

    def as_admin(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_ADMIN_USER'), os.getenv('SPPI_ADMIN_PASSWORD'))
        self.bearer(token)

        return self

    def as_default(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_DEFAULT_USER'), os.getenv('SPPI_DEFAULT_PASSWORD'))
        self.bearer(token)

        return self

    def as_pilot(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_PILOT_USER'), os.getenv('SPPI_PILOT_PASSWORD'))
        self.bearer(token)

        return self

    def as_browsing_dispatcher(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_BROWSING_DISPATCHER_USER'),
                                                  os.getenv('SPPI_BROWSING_DISPATCHER_PASSWORD'))
        self.bearer(token)

        return self

    def as_dispatcher_gc(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_DISPATCHER_GC_USER'),
                                                  os.getenv('SPPI_DISPATCHER_GC_PASSWORD'))
        self.bearer(token)

        return self

    def as_atm_dispatcher_moscow(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_ATM_DISPATCHER_MOSCOW_USER'),
                                                  os.getenv('SPPI_ATM_DISPATCHER_MOSCOW_PASSWORD'))
        self.bearer(token)

        return self

    def as_atm_admin_moscow(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_ATM_ADMIN_MOSCOW_USER'),
                                                  os.getenv('SPPI_ATM_ADMIN_MOSCOW_PASSWORD'))
        self.bearer(token)

        return self

    def as_aircompany(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_AIRCOMPANY_USER'),
                                                  os.getenv('SPPI_AIRCOMPANY_PASSWORD'))
        self.bearer(token)

        return self

    def as_subject_representative_moscow(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_SUBJECT_REPRESENTATIVE_MOSCOW_USER'),
                                                  os.getenv('SPPI_SUBJECT_REPRESENTATIVE_MOSCOW_PASSWORD'))
        self.bearer(token)

        return self

    def as_lsg_representative_moscow(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_LSG_REPRESENTATIVE_MOSCOW_USER'),
                                                  os.getenv('SPPI_LSG_REPRESENTATIVE_MOSCOW_PASSWORD'))
        self.bearer(token)

        return self

    def as_mod_representative(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_MOD_REPRESENTATIVE_USER'),
                                                  os.getenv('SPPI_MOD_REPRESENTATIVE_PASSWORD'))
        self.bearer(token)

        return self

    def as_gosaviaciya_mo(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_GOSAVIACIYA_MO_USER'),
                                                  os.getenv('SPPI_GOSAVIACIYA_MO_PASSWORD'))
        self.bearer(token)

        return self

    def as_gosaviaciya_fsb(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_GOSAVIACIYA_FSB_USER'),
                                                  os.getenv('SPPI_GOSAVIACIYA_FSB_PASSWORD'))
        self.bearer(token)

        return self

    def as_gosaviaciya_fso(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_GOSAVIACIYA_FSO_USER'),
                                                  os.getenv('SPPI_GOSAVIACIYA_FSO_PASSWORD'))
        self.bearer(token)

        return self

    def as_gosaviaciya_mvd(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_GOSAVIACIYA_MVD_USER'),
                                                  os.getenv('SPPI_GOSAVIACIYA_MVD_PASSWORD'))
        self.bearer(token)

        return self

    def as_gosaviaciya_vv_mvd_rf(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_GOSAVIACIYA_VV_MVD_RF_USER'),
                                                  os.getenv('SPPI_GOSAVIACIYA_VV_MVD_RF_PASSWORD'))
        self.bearer(token)

        return self

    def as_gosaviaciya_mchs(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_GOSAVIACIYA_MCHS_USER'),
                                                  os.getenv('SPPI_GOSAVIACIYA_MCHS_PASSWORD'))
        self.bearer(token)

        return self

    def as_gosaviaciya_dosaaf(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_GOSAVIACIYA_DOSAAF_USER'),
                                                  os.getenv('SPPI_GOSAVIACIYA_DOSAAF_PASSWORD'))
        self.bearer(token)

        return self

    def as_gosaviaciya_custom(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_GOSAVIACIYA_CUSTOM_USER'),
                                                  os.getenv('SPPI_GOSAVIACIYA_CUSTOM_PASSWORD'))
        self.bearer(token)

        return self

    def as_experimental_aviation(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_EXPERIMENTAL_AVIATION_USER'),
                                                  os.getenv('SPPI_EXPERIMENTAL_AVIATION_PASSWORD'))
        self.bearer(token)

        return self

    def as_aeroinfo_uuuwzdzx(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_AEROINFO_UUUWZDZX_USER'),
                                                  os.getenv('SPPI_AEROINFO_UUUWZDZX_PASSWORD'))
        self.bearer(token)

        return self

    def as_svs_pilot(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_SVS_PILOT_USER'),
                                                  os.getenv('SPPI_SVS_PILOT_PASSWORD'))
        self.bearer(token)

        return self

    def as_spw_manager(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_SPW_MANAGER_USER'),
                                                  os.getenv('SPPI_SPW_MANAGER_PASSWORD'))
        self.bearer(token)

        return self

    def as_mr_submission_manager(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_MR_SUBMISSION_MANAGER_USER'),
                                                  os.getenv('SPPI_MR_SUBMISSION_MANAGER_PASSWORD'))
        self.bearer(token)

        return self

    def as_shar_pilot(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_SHAR_PILOT_USER'),
                                                  os.getenv('SPPI_SHAR_PILOT_PASSWORD'))
        self.bearer(token)

        return self

    def as_aer_pilot(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_AER_PILOT_USER'),
                                                  os.getenv('SPPI_AER_PILOT_PASSWORD'))
        self.bearer(token)

        return self

    def as_bla_pilot(self):
        token = self.sppi_client.get_access_token(os.getenv('SPPI_BLA_PILOT_USER'),
                                                  os.getenv('SPPI_BLA_PILOT_PASSWORD'))
        self.bearer(token)

        return self

    def status(self):
        self._url = '/'

        return self

    def federation_entities(self):
        if self._url == '/internal':
            self._url += '/federation-entities'
        else:
            self._url = '/federation-entities'

        return self

    def uuid(self, uuid: str):
        self._url += f'/{uuid}'

        return self

    def details(self):
        self._url += '/details'

        return self

    def municipals(self):
        if self._url == '/internal':
            self._url += '/municipals'
        else:
            self._url = '/municipals'

        return self

    def aerial_photos(self):
        self._url = '/aerial-photos'

        return self

    def restrictions(self):
        if self._url == '/internal':
            self._url += '/restrictions'
        else:
            self._url = '/restrictions'

        return self

    def geometries(self):
        if self._url == '/internal':
            self._url += '/geometries'
        else:
            self._url = '/geometries'

        return self

    def internal(self):
        self._url = '/internal'

        return self

    def drone_areas(self):
        self._url += '/drone-areas'

        return self

    def geometry(self):
        self._url += '/geometry'

        return self

    def metadata(self):
        self._url += '/metadata'

        return self

    def updates(self):
        self._url += '/updates'

        return self

    def since_date_time(self, delta: timedelta = timedelta(weeks=1)):
        self._query.update({'since_date_time': int((datetime.now() - delta).timestamp())})

        return self

    def create_federation_entity(self, new_federation_entity: NewFederationEntity | None = None) -> FederationEntity:
        if new_federation_entity is None:
            new_federation_entity: NewFederationEntity = NewFederationEntityFactory.build()

        response = self.as_admin().federation_entities().post(json=new_federation_entity.model_dump())
        federation_entity = FederationEntity.model_validate(response.json())

        return federation_entity

    def delete_federation_entity(self, uuid: str) -> bool:
        response = self.as_admin().federation_entities().uuid(uuid).delete()

        return response.status_code == 204

    def create_aerial_photo(self) -> AerialPhoto:
        new_aerial_photo: NewAerialPhoto = NewAerialPhotoFactory.build()

        response = self.as_admin().aerial_photos().post(json=new_aerial_photo.model_dump())
        aerial_photo = AerialPhoto.model_validate(response.json())

        return aerial_photo

    def delete_aerial_photo(self, uuid: str) -> bool:
        response = self.as_admin().aerial_photos().uuid(uuid).delete()

        return response.status_code == 204

    def create_municipal(self, new_municipal: NewMunicipal | None = None) -> Municipal:
        if new_municipal is None:
            new_municipal: NewMunicipal = NewMunicipalFactory.build()

        response = self.as_admin().municipals().post(json=new_municipal.model_dump())
        municipal_entity = Municipal.model_validate(response.json())

        return municipal_entity

    def delete_municipal(self, uuid: str) -> bool:
        response = self.as_admin().municipals().uuid(uuid).delete()

        return response.status_code == 204

    def delete_restriction(self, uuid: str) -> bool:
        response = self.as_admin().restrictions().uuid(uuid).delete()

        return response.status_code == 204
