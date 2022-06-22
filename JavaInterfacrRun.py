from JavaInterface import openapi_client
from JavaInterface.openapi_client.api import auth_controller_api, user_controller_api
from config import Config


class Runner:

    def __init__(self, jwt_token=None):
        self.jwt_token = ""
        configuration = openapi_client.Configuration(
            host=Config.JAVA_INTERFACE_URL,
            access_token=jwt_token
        )

        with openapi_client.ApiClient(configuration) as api_client:
            self.authentication_instance = auth_controller_api.AuthControllerApi(api_client)
            self.user_instance = user_controller_api.UserControllerApi(api_client)

    def login(self, _userName, _password):
        try:
            login_response = self.authentication_instance.user_login(_userName, _password, async_req=True)
            return login_response.get()
        except openapi_client.ApiException as e:
            return "Exception when calling AuthControllerApi->login: %s\n" % e.body

    def get_user_by_email(self, _email):
        try:
            response = self.user_instance.find_by_email(_email, async_req=True)
            return response.get()
        except openapi_client.ApiException as e:
            return "Exception while calling UserControllerAPI-->find_by_email: ", e.body

    def logout(self):
        try:
            response = self.authentication_instance.user_logout(async_req=True)
            return response.get()
        except openapi_client.ApiException as e:
            return "Exception while calling AuthControllerAPI-->user_logout: ", e.body
