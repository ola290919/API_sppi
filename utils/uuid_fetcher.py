import datetime
import os
import random
from enum import Enum

import pytest
from utils.api_client import ApiClient


class UUIDFetcher:
    # Class attributes to store UUID lists, shared across all instances
    _federal_uuid_list = None
    _municipal_uuid_list = None
    _aerial_photo_uuid_list = None
    _restriction_subject_uuid_list = None
    _restriction_lsg_uuid_list = None
    _restriction_lsg_klin_uuid_list = None

    def __init__(self):
        # Initialize the API client
        self.api_client = ApiClient()

    def federal_uuid_list(self):
        # Populate federal UUID list if not already done
        if UUIDFetcher._federal_uuid_list is None:
            UUIDFetcher._federal_uuid_list = self._fetch_federal_uuids()
            if not UUIDFetcher._federal_uuid_list:
                pytest.skip('empty federation entities list')

        return UUIDFetcher._federal_uuid_list

    def federal_uuid_random(self):
        return random.choice(self.federal_uuid_list())

    def municipal_uuid_list(self):
        # Populate municipal UUID list if not already done
        if UUIDFetcher._municipal_uuid_list is None:
            UUIDFetcher._municipal_uuid_list = self._fetch_municipal_uuids()
            if not UUIDFetcher._municipal_uuid_list:
                pytest.skip('empty municipal entities list')

        return UUIDFetcher._municipal_uuid_list

    def municipal_uuid_random(self):
        return random.choice(self.municipal_uuid_list())

    def any_uuid_list(self):
        # Combine federal and municipal UUID lists
        combined_uuid_list = [self.federal_uuid_list(), self.municipal_uuid_list()]
        if not combined_uuid_list:
            pytest.skip('empty entities list')

        return combined_uuid_list

    def any_uuid_random(self):
        return [self.federal_uuid_random(), self.municipal_uuid_random()]

    def aerial_photo_uuid_list(self):
        # Populate aerial_photo UUID list if not already done
        if UUIDFetcher._aerial_photo_uuid_list is None:
            UUIDFetcher._aerial_photo_uuid_list = self._fetch_aerial_photo_uuids()
            if not UUIDFetcher._aerial_photo_uuid_list:
                pytest.skip('empty aerial_photo entities list')

        return UUIDFetcher._aerial_photo_uuid_list

    def aerial_photo_uuid_random(self):
        return random.choice(self.aerial_photo_uuid_list())

    def restriction_subject_uuid_list(self):
        # Populate restriction_subject UUID list if not already done
        if UUIDFetcher._restriction_subject_uuid_list is None:
            UUIDFetcher._restriction_subject_uuid_list = self._fetch_restriction_object_uuids(self.subject_uuid())
            if not UUIDFetcher._restriction_subject_uuid_list:
                pytest.skip('empty restriction_subject entities list')

        return UUIDFetcher._restriction_subject_uuid_list

    def restriction_subject_uuid_random(self):
        return random.choice(self.restriction_subject_uuid_list())

    def restriction_lsg_uuid_list(self):
        # Populate restriction_lsg UUID list if not already done
        if UUIDFetcher._restriction_lsg_uuid_list is None:
            UUIDFetcher._restriction_lsg_uuid_list = self._fetch_restriction_object_uuids(self.lsg_uuid())
            if not UUIDFetcher._restriction_lsg_uuid_list:
                pytest.skip('empty restriction_lsg entities list')

        return UUIDFetcher._restriction_lsg_uuid_list

    def restriction_lsg_uuid_random(self):
        return random.choice(self.restriction_lsg_uuid_list())

    def restriction_lsg_klin_uuid_list(self):
        # Populate restriction_lsg_klin UUID list if not already done
        if UUIDFetcher._restriction_lsg_klin_uuid_list is None:
            UUIDFetcher._restriction_lsg_klin_uuid_list = self._fetch_restriction_object_uuids(self.lsg_klin_uuid())
            if not UUIDFetcher._restriction_lsg_klin_uuid_list:
                pytest.skip('empty restriction_lsg_klin entities list')

        return UUIDFetcher._restriction_lsg_klin_uuid_list

    def restriction_lsg_klin_uuid_random(self):
        return random.choice(self.restriction_lsg_uuid_list())

    @staticmethod
    def subject_uuid():
        # Retrieve subject UUID from environment variable
        uuid = os.getenv("SPPI_SUBJECT_REPRESENTATIVE_MOSCOW_UUID")
        if uuid is None:
            pytest.skip('SPPI_SUBJECT_REPRESENTATIVE_MOSCOW_UUID not set')

        return uuid

    @staticmethod
    def lsg_uuid():
        # Retrieve LSG UUID from environment variable
        uuid = os.getenv("SPPI_LSG_REPRESENTATIVE_MOSCOW_UUID")
        if uuid is None:
            pytest.skip('SPPI_LSG_REPRESENTATIVE_MOSCOW_UUID not set')

        return uuid

    @staticmethod
    def lsg_klin_uuid():
        # Retrieve LSG UUID from environment variable
        uuid = os.getenv("SPPI_LSG_REPRESENTATIVE_KLIN_UUID")
        if uuid is None:
            pytest.skip('SPPI_LSG_REPRESENTATIVE_KLIN_UUID not set')

        return uuid

    @staticmethod
    def object_with_geometry_uuid():
        # Retrieve object with geometry UUID from environment variable
        uuid = os.getenv("SPPI_OBJECT_WITH_GEOMETRY_1_UUID")
        if uuid is None:
            pytest.skip('SPPI_OBJECT_WITH_GEOMETRY_1_UUID not set')

        return uuid

    def _fetch_federal_uuids(self):
        # Fetch and return the list of federal UUIDs
        federal_entities = self.api_client.as_admin().federation_entities().get().json()['data']
        return [entity['uuid'] for entity in federal_entities]

    def _fetch_municipal_uuids(self):
        # Fetch and return the list of municipal UUIDs
        municipal_entities = self.api_client.as_admin().municipals().get().json()['data']
        return [entity['uuid'] for entity in municipal_entities]

    def _fetch_aerial_photo_uuids(self):
        # Fetch and return the list of aerial_photo UUIDs
        aerial_photos = self.api_client.as_admin().aerial_photos().get().json()['data']
        return [entity['uuid'] for entity in aerial_photos]

    def _fetch_restriction_object_uuids(self, object_uuid):
        # Fetch and return the list of restriction_subject UUIDs
        restrictions = \
            self.api_client.as_admin().restrictions().query({'filter[object_uuid]': object_uuid}).get().json()[
                'data']
        return [entity['uuid'] for entity in restrictions if
                entity['to_date'] > int(datetime.datetime.now().timestamp())]

    @classmethod
    def reset_shared_data(cls):
        """Reset the shared UUID lists."""
        cls._federal_uuid_list = None
        cls._municipal_uuid_list = None
        cls._aerial_photo_uuid_list = None
        cls._restriction_subject_uuid_list = None
        cls._restriction_lsg_uuid_list = None
        cls._restriction_lsg_klin_uuid_list = None


fetcher = UUIDFetcher()


class UUIDType(Enum):
    FEDERAL_LIST = 1
    MUNICIPAL_LIST = 2
    ANY_LIST = 3
    SUBJECT = 4
    LSG = 5
    FEDERAL = 6
    MUNICIPAL = 7
    ANY = 8
    OBJECT_WITH_GEOMETRY = 9
    PHOTO = 10
    RESTRICTION_SUBJECT = 11
    RESTRICTION_LSG = 12
    LSG_KLIN = 13
    RESTRICTION_LSG_KLIN = 14

    def get_uuid(self):
        methods = {
            self.FEDERAL_LIST: fetcher.federal_uuid_list,
            self.MUNICIPAL_LIST: fetcher.municipal_uuid_list,
            self.ANY_LIST: fetcher.any_uuid_list,
            self.SUBJECT: fetcher.subject_uuid,
            self.LSG: fetcher.lsg_uuid,
            self.FEDERAL: fetcher.federal_uuid_random,
            self.MUNICIPAL: fetcher.municipal_uuid_random,
            self.ANY: fetcher.any_uuid_random,
            self.OBJECT_WITH_GEOMETRY: fetcher.object_with_geometry_uuid,
            self.PHOTO: fetcher.aerial_photo_uuid_random,
            self.RESTRICTION_SUBJECT: fetcher.restriction_subject_uuid_random,
            self.RESTRICTION_LSG: fetcher.restriction_lsg_uuid_random,
            self.LSG_KLIN: fetcher.lsg_klin_uuid,
            self.RESTRICTION_LSG_KLIN: fetcher.restriction_lsg_klin_uuid_random
        }

        return methods[self]()
