from typing import List

import pytest

from models.restriction import Restriction
from utils.api_client import ApiClient


class RestrictionsTestBase:
    created_entries: List[Restriction] = []

    @pytest.fixture(scope="session", autouse=True)
    def cleanup_entities(self, request):
        api_client = ApiClient()

        yield

        def delete_entries():
            for entry in self.created_entries:
                api_client.as_admin().restrictions().uuid(entry.uuid).delete()

        request.addfinalizer(delete_entries)

    def _add_entry_for_deletion(self, response=None):
        try:
            if response:
                entry = Restriction.model_validate(response.json())
                if entry:
                    self.created_entries.append(entry)
        except (Exception,):
            pass
