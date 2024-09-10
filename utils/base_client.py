import os

import requests


class BaseClient:
    session: requests.Session
    _base_url: str
    _url: str
    _query: dict

    def __init__(self, base_url: str):
        self.session = self._get_session(self)
        self._base_url = base_url
        self._url = ''
        self._query = {}

    @staticmethod
    def _get_proxies():
        http_proxy = os.getenv('http_proxy')
        https_proxy = os.getenv('https_proxy')
        proxy = os.getenv('PROXY')
        proxies = {}
        if proxy:
            proxies['http'] = proxy
            proxies['https'] = proxy
        elif http_proxy:
            proxies['http'] = http_proxy
        elif https_proxy:
            proxies['https'] = https_proxy

        return proxies if proxies else None

    @staticmethod
    def _get_session(self):
        session = requests.Session()
        proxies = self._get_proxies()
        if proxies:
            session.proxies.update(proxies)

        return session

    def bearer(self, token: str):
        self.session.headers.update({'Authorization': 'Bearer ' + token})

        return self

    def query(self, params: dict):
        self._query.update(params)

        return self

    def limit(self, limit: int):
        self._query.update({'limit': limit})

        return self

    def offset(self, offset: int):
        self._query.update({'offset': offset})

        return self

    def get(self, url: str = ''):
        return self.session.get(self._base_url + self._url + str(url), params=self._query)

    def post(self, url: str = '', json=None):
        if json is None:
            json = {}
        return self.session.post(self._base_url + self._url + str(url), json=json, params=self._query)

    def delete(self, url: str = ''):
        return self.session.delete(self._base_url + self._url + str(url), params=self._query)

    def put(self, url: str = '', json=None):
        if json is None:
            json = {}
        return self.session.put(self._base_url + self._url + str(url), json=json, params=self._query)

    def patch(self, url: str = '', json=None):
        if json is None:
            json = {}
        return self.session.patch(self._base_url + self._url + str(url), json=json, params=self._query)
