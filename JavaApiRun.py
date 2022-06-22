from JavaApi import openapi_client
from JavaApi.openapi_client.api import sdk_service_api
from config import Config


class Run:

    def __init__(self):
        configuration = openapi_client.Configuration(
            host=Config.JAVA_API_URL
        )

        with openapi_client.ApiClient(configuration) as api_client:
            self.api_instance = sdk_service_api.SDKSERVICEApi(api_client)

    def get_vault_nav(self, vault_address, **kwargs):
        try:
            if kwargs.__len__() == 0:
                api_response = self.api_instance.get_vault_nav(vault_address, async_req=True)
            else:
                api_response = self.api_instance.get_vault_nav(vault_address, timestamp=kwargs['time_stamp'],
                                                               is_date=kwargs['is_date'],
                                                               async_req=True)
            return api_response.get()
        except openapi_client.ApiException as e:
            return "Exception while calling get_vault_nav: ", e.body

    def get_token_price(self, token_address, is_vault_token, **kwargs):
        try:
            if kwargs.__len__() == 0:
                api_response = self.api_instance.get_token_price(token_address, is_vault_token=is_vault_token,
                                                                 async_req=True)
            else:
                api_response = self.api_instance.get_token_price(token_address, is_vault_token=is_vault_token,
                                                                 timestamp=kwargs['time_stamp'],
                                                                 is_date=kwargs['is_date'],
                                                                 async_req=True)
            return api_response.get()
        except openapi_client.ApiException as e:
            return "Exception while calling get_token_price: ", e.body

    def get_vault_assets(self, vault_address):
        try:
            api_response = self.api_instance.get_vault_assets(vault_address, async_req=True)
            return api_response.get()
        except openapi_client.ApiException as e:
            return "Exception while calling get_vault_assets: ", e.body

    def get_token_balance(self, vault_address, token_address, **kwargs):
        try:
            if kwargs.__len__() == 0:
                api_response = self.api_instance.get_token_balance(vault_address, token_address, async_req=True)
            else:
                api_response = self.api_instance.get_token_balance(vault_address, token_address,
                                                                   timestamp=kwargs['time_stamp'],
                                                                   is_date=kwargs['is_date'], async_req=True)
            return api_response.get()
        except openapi_client.ApiException as e:
            return "Exception while calling get_token_balance: ", e.body
