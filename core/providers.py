import os
from requests import get

class DartProvider:
    api_key: str

    BASE_URL = "https://opendart.fss.or.kr"

    def __init__(self):
        self.api_key = os.environ["OPENDART_API_KEY"]

    @property
    def base_query(self):
        return { "crtfc_key" : self.api_key }

    def get(self, *, path, params = {}):
        params = { **self.base_query, **params }
        result = get(f"{self.BASE_URL}{path}", params).json()
        print(result)

    @classmethod
    def get_list(cls):
        provider: DartProvider = cls()
        params = {
            'corp_code': '00126380' # 삼성전자
        }
        provider.get(path = "/api/list.json", params = params)

    @classmethod
    def get_company(cls):
        provider: DartProvider = cls()
        params = {
            'corp_code': '00126380' # 삼성전자
        }
        provider.get(path = "/api/company.json", params = params)
