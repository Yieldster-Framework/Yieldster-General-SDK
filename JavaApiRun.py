from YieldsterSDK import openapi_client
from YieldsterSDK.openapi_client.api import sdk_service_api, vault_service_api
from config import Config


class Run:

    def __init__(self):
        configuration = openapi_client.Configuration(
            host=Config.JAVA_API_URL
        )

        with openapi_client.ApiClient(configuration) as api_client:
            self.api_instance = sdk_service_api.SDKSERVICEApi(api_client)
            self.vault_api_instance = vault_service_api.VAULTSERVICEApi(api_client)

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

    def get_token_decimal(self, token_address):
        try:
            api_response = self.api_instance.get_token_decimal(token_address, async_req=True)
            return api_response.get()
        except openapi_client.ApiException as e:
            return "Exception while getting token decimal: ", e.body

    def get_estimated_gas(self, vault_address, token_address, encoded_instruction, account_address):
        try:
            api_response = self.vault_api_instance.get_gas_estimate(vault_address, token_address, encoded_instruction,
                                                                    account_address, async_req=True)
            return api_response.get()
        except openapi_client.ApiException as e:
            return "Exception while getting estimated gas: ", e.body

    def execute_withdraw(self, account_address, value, token_address, amount,
                         encoded_instruction, vault_address):
        try:
            api_response = self.vault_api_instance.execute_withdraw(account_address, value, token_address, amount,
                                                                    encoded_instruction, vault_address, async_req=True)
            return api_response.get()
        except openapi_client.ApiException as e:
            return "Exception while executing withdraw: ", e.body
