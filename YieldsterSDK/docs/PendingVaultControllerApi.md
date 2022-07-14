# YieldsterSDK.openapi_client.PendingVaultControllerApi

All URIs are relative to *http://localhost:8050*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pending_vault1**](PendingVaultControllerApi.md#create_pending_vault1) | **POST** /pendingVault/sdk/v2.0/yieldster/create | API to CREATE_PENDING_VAULT
[**get_all_pending_vaults1**](PendingVaultControllerApi.md#get_all_pending_vaults1) | **GET** /pendingVault/sdk/v2.0/yieldster/get | API to get ALL_PENDING_VAULTS
[**get_pending_vault_by_id1**](PendingVaultControllerApi.md#get_pending_vault_by_id1) | **GET** /pendingVault/sdk/v2.0/yieldster/{id} | API to get PENDING_VAULT_BY_ID
[**set_vault_icon_image**](PendingVaultControllerApi.md#set_vault_icon_image) | **POST** /pendingVault/sdk/v2.0/yieldster/setIcon/{vaultId} | API to SET_VAULT_ICON
[**vault_creation_queue**](PendingVaultControllerApi.md#vault_creation_queue) | **GET** /pendingVault/sdk/v2.0/yieldster/queue | API to POLLING_VAULT_CREATION


# **create_pending_vault1**
> SDKResponse create_pending_vault1(pending_vault)

API to CREATE_PENDING_VAULT

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import pending_vault_controller_api
from YieldsterSDK.openapi_client.model.pending_vault import PendingVault
from YieldsterSDK.openapi_client.model.sdk_response import SDKResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8050
# See configuration.py for a list of all supported configuration parameters.
configuration = YieldsterSDK.openapi_client.Configuration(
    host = "http://localhost:8050"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-jwt
configuration = YieldsterSDK.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with YieldsterSDK.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pending_vault_controller_api.PendingVaultControllerApi(api_client)
    pending_vault = PendingVault(
        id="id_example",
        call_arguments={
            "key": {
                "key": "key_example",
            },
        },
        supported_assets=[
            {},
        ],
        supported_vaults=[
            {},
        ],
        vault_creation_status="WHITELIST_CREATION",
        vault_name="vault_name_example",
        token_name="token_name_example",
        token_symbol="token_symbol_example",
        vault_admin="vault_admin_example",
        account_address="account_address_example",
        vault_address="vault_address_example",
        vault_type="PUBLIC",
        base_currency="base_currency_example",
        advisor_id="advisor_id_example",
        vault_advisor_setting={
            "key": {},
        },
        advisor_end_point="advisor_end_point_example",
        advisor_email="advisor_email_example",
        deposit_strategy="deposit_strategy_example",
        withdrawal_strategy="withdrawal_strategy_example",
        vault_icon=Binary(
            type='YQ==',
            data=[
                'YQ==',
            ],
        ),
        fee_strategy_list=[
            "fee_strategy_list_example",
        ],
        management_fee_details={
            "key": FeeModel(
                beneficiary="beneficiary_example",
                percentage=3.14,
            ),
        },
        white_list_group_id=[
            "white_list_group_id_example",
        ],
        while_list_members=[
            "while_list_members_example",
        ],
        white_list_group_name="white_list_group_name_example",
        supported_protocols=[
            {},
        ],
        emergency_vault_address="emergency_vault_address_example",
    ) # PendingVault | 

    # example passing only required values which don't have defaults set
    try:
        # API to CREATE_PENDING_VAULT
        api_response = api_instance.create_pending_vault1(pending_vault)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PendingVaultControllerApi->create_pending_vault1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pending_vault** | [**PendingVault**](PendingVault.md)|  |

### Return type

[**SDKResponse**](SDKResponse.md)

### Authorization

[bearer-jwt](../README.md#bearer-jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**400** | Bad request, check the provided parameters |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | Response received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_pending_vaults1**
> SDKResponse get_all_pending_vaults1()

API to get ALL_PENDING_VAULTS

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import pending_vault_controller_api
from YieldsterSDK.openapi_client.model.sdk_response import SDKResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8050
# See configuration.py for a list of all supported configuration parameters.
configuration = YieldsterSDK.openapi_client.Configuration(
    host = "http://localhost:8050"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-jwt
configuration = YieldsterSDK.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with YieldsterSDK.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pending_vault_controller_api.PendingVaultControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API to get ALL_PENDING_VAULTS
        api_response = api_instance.get_all_pending_vaults1()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PendingVaultControllerApi->get_all_pending_vaults1: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SDKResponse**](SDKResponse.md)

### Authorization

[bearer-jwt](../README.md#bearer-jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**400** | Bad request, check the provided parameters |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | Response received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_vault_by_id1**
> SDKResponse get_pending_vault_by_id1(id)

API to get PENDING_VAULT_BY_ID

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import pending_vault_controller_api
from YieldsterSDK.openapi_client.model.sdk_response import SDKResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8050
# See configuration.py for a list of all supported configuration parameters.
configuration = YieldsterSDK.openapi_client.Configuration(
    host = "http://localhost:8050"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-jwt
configuration = YieldsterSDK.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with YieldsterSDK.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pending_vault_controller_api.PendingVaultControllerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get PENDING_VAULT_BY_ID
        api_response = api_instance.get_pending_vault_by_id1(id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PendingVaultControllerApi->get_pending_vault_by_id1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**SDKResponse**](SDKResponse.md)

### Authorization

[bearer-jwt](../README.md#bearer-jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**400** | Bad request, check the provided parameters |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | Response received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_vault_icon_image**
> SDKResponse set_vault_icon_image(vault_id)

API to SET_VAULT_ICON

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import pending_vault_controller_api
from YieldsterSDK.openapi_client.model.sdk_response import SDKResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8050
# See configuration.py for a list of all supported configuration parameters.
configuration = YieldsterSDK.openapi_client.Configuration(
    host = "http://localhost:8050"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-jwt
configuration = YieldsterSDK.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with YieldsterSDK.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pending_vault_controller_api.PendingVaultControllerApi(api_client)
    vault_id = "vaultId_example" # str | 
    image_upload = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # API to SET_VAULT_ICON
        api_response = api_instance.set_vault_icon_image(vault_id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PendingVaultControllerApi->set_vault_icon_image: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to SET_VAULT_ICON
        api_response = api_instance.set_vault_icon_image(vault_id, image_upload=image_upload)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PendingVaultControllerApi->set_vault_icon_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**|  |
 **image_upload** | **file_type**|  | [optional]

### Return type

[**SDKResponse**](SDKResponse.md)

### Authorization

[bearer-jwt](../README.md#bearer-jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**400** | Bad request, check the provided parameters |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | Response received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_creation_queue**
> SDKResponse vault_creation_queue(id)

API to POLLING_VAULT_CREATION

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import pending_vault_controller_api
from YieldsterSDK.openapi_client.model.sdk_response import SDKResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8050
# See configuration.py for a list of all supported configuration parameters.
configuration = YieldsterSDK.openapi_client.Configuration(
    host = "http://localhost:8050"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-jwt
configuration = YieldsterSDK.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with YieldsterSDK.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pending_vault_controller_api.PendingVaultControllerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to POLLING_VAULT_CREATION
        api_response = api_instance.vault_creation_queue(id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PendingVaultControllerApi->vault_creation_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**SDKResponse**](SDKResponse.md)

### Authorization

[bearer-jwt](../README.md#bearer-jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**400** | Bad request, check the provided parameters |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | Response received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

