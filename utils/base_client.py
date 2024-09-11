import os
import allure

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

    @allure.step("Задать параметры {params}")
    def query(self, params: dict):
        self._query.update(params)

        return self

    @allure.step("Задать параметр limit {limit}")
    def limit(self, limit: int):
        self._query.update({'limit': limit})

        return self

    @allure.step("Задать параметр offset {offset}")
    def offset(self, offset: int):
        self._query.update({'offset': offset})

        return self

    @allure.step("Отправить get запрос")
    def get(self, url: str = ''):
        return self.session.get(self._base_url + self._url + str(url), params=self._query)

    @allure.step("Отправить post запрос")
    def post(self, url: str = '', json=None):
        if json is None:
            json = {}
        return self.session.post(self._base_url + self._url + str(url), json=json, params=self._query)

    @allure.step("Отправить delete запрос")
    def delete(self, url: str = ''):
        return self.session.delete(self._base_url + self._url + str(url), params=self._query)

    @allure.step("Отправить put запрос")
    def put(self, url: str = '', json=None):
        if json is None:
            json = {}
        return self.session.put(self._base_url + self._url + str(url), json=json, params=self._query)

    @allure.step("Отправить patch запрос")
    def patch(self, url: str = '', json=None):
        if json is None:
            json = {}
        return self.session.patch(self._base_url + self._url + str(url), json=json, params=self._query)
