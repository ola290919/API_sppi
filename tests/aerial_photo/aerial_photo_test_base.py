from typing import List

import pytest
from requests import Response

from models.aerial_photo import AerialPhoto
from utils.api_client import ApiClient


class AerialPhotoTestBase:
    created_entries: List[AerialPhoto] = []

    @pytest.fixture(scope="session", autouse=True)
    def cleanup_entries(self, request):
        api_client = ApiClient()

        yield

        def delete_entries():
            for entity in self.created_entries:
                api_client.as_admin().aerial_photos().uuid(entity.uuid).delete()

        request.addfinalizer(delete_entries)

    def _add_entry_for_deletion(self, entry: AerialPhoto | Response | None = None):
        try:
            if entry:
                if isinstance(entry, Response):
                    entry = AerialPhoto.model_validate(entry.json())

                self.created_entries.append(entry)
        except (Exception,):
            pass
