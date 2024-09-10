from typing import List

import pytest
from requests import Response

from models.municipal import Municipal
from utils.api_client import ApiClient


class MunicipalsTestBase:
    created_entries: List[Municipal] = []

    @pytest.fixture(scope="session", autouse=True)
    def cleanup_entries(self, request):
        api_client = ApiClient()

        yield

        def delete_entries():
            for entry in self.created_entries:
                api_client.as_admin().municipals().uuid(entry.uuid).delete()

        request.addfinalizer(delete_entries)

    def _add_entry_for_deletion(self, entry: Municipal | Response | None = None):
        try:
            if entry:
                if isinstance(entry, Response):
                    entry = Municipal.model_validate(entry.json())

                self.created_entries.append(entry)
        except (Exception,):
            pass
