# JavaApi.openapi_client.SDKSERVICEApi

All URIs are relative to *http://localhost:8050*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token_balance**](SDKSERVICEApi.md#get_token_balance) | **GET** /smart-contract/sdk/v2.0/yieldster/tokenBalance | API to get Historical Token Balance of Vault
[**get_token_price**](SDKSERVICEApi.md#get_token_price) | **GET** /smart-contract/sdk/v2.0/yieldster/tokenPrice | API to get Historical Token Price of Vault
[**get_vault_assets**](SDKSERVICEApi.md#get_vault_assets) | **GET** /smart-contract/sdk/v2.0/yieldster/vaultAssets/{vaultAddress} | API to get Assets of a vault
[**get_vault_nav**](SDKSERVICEApi.md#get_vault_nav) | **GET** /smart-contract/sdk/v2.0/yieldster/vaultNAV | API to get Historical NAV of a vault


# **get_token_balance**
> SDKResponse get_token_balance(vault_address, token_address)

API to get Historical Token Balance of Vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import JavaApi.openapi_client
from JavaApi.openapi_client.api import sdk_service_api
from JavaApi.openapi_client.model.sdk_response import SDKResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8050
# See configuration.py for a list of all supported configuration parameters.
configuration = JavaApi.openapi_client.Configuration(
    host = "http://localhost:8050"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-jwt
configuration = JavaApi.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with JavaApi.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sdk_service_api.SDKSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | Address of the vault that want to know Token Balance
    token_address = "tokenAddress_example" # str | Address of the Token that want to know Balance 
    timestamp = "timestamp_example" # str | Unix timestamp or date in the format DD-MM-YYYY HH:MM:SS  (optional)
    is_date = True # bool | Boolean value which represent the time is in the format date or not  (optional)

    # example passing only required values which don't have defaults set
    try:
        # API to get Historical Token Balance of Vault
        api_response = api_instance.get_token_balance(vault_address, token_address)
        pprint(api_response)
    except JavaApi.openapi_client.ApiException as e:
        print("Exception when calling SDKSERVICEApi->get_token_balance: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to get Historical Token Balance of Vault
        api_response = api_instance.get_token_balance(vault_address, token_address, timestamp=timestamp, is_date=is_date)
        pprint(api_response)
    except JavaApi.openapi_client.ApiException as e:
        print("Exception when calling SDKSERVICEApi->get_token_balance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| Address of the vault that want to know Token Balance |
 **token_address** | **str**| Address of the Token that want to know Balance  |
 **timestamp** | **str**| Unix timestamp or date in the format DD-MM-YYYY HH:MM:SS  | [optional]
 **is_date** | **bool**| Boolean value which represent the time is in the format date or not  | [optional]

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**200** | Response received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_price**
> SDKResponse get_token_price(token_address, is_vault_token)

API to get Historical Token Price of Vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import JavaApi.openapi_client
from JavaApi.openapi_client.api import sdk_service_api
from JavaApi.openapi_client.model.sdk_response import SDKResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8050
# See configuration.py for a list of all supported configuration parameters.
configuration = JavaApi.openapi_client.Configuration(
    host = "http://localhost:8050"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-jwt
configuration = JavaApi.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with JavaApi.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sdk_service_api.SDKSERVICEApi(api_client)
    token_address = "tokenAddress_example" # str | Address of the token that want to know Token Price 
    is_vault_token = True # bool | Whether the provided token is a vault token or not
    timestamp = "timestamp_example" # str | Unix timestamp or date in the format DD-MM-YYYY HH:MM:SS  (optional)
    is_date = True # bool | Boolean value which represent the time is in the format date or not  (optional)

    # example passing only required values which don't have defaults set
    try:
        # API to get Historical Token Price of Vault
        api_response = api_instance.get_token_price(token_address, is_vault_token)
        pprint(api_response)
    except JavaApi.openapi_client.ApiException as e:
        print("Exception when calling SDKSERVICEApi->get_token_price: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to get Historical Token Price of Vault
        api_response = api_instance.get_token_price(token_address, is_vault_token, timestamp=timestamp, is_date=is_date)
        pprint(api_response)
    except JavaApi.openapi_client.ApiException as e:
        print("Exception when calling SDKSERVICEApi->get_token_price: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_address** | **str**| Address of the token that want to know Token Price  |
 **is_vault_token** | **bool**| Whether the provided token is a vault token or not |
 **timestamp** | **str**| Unix timestamp or date in the format DD-MM-YYYY HH:MM:SS  | [optional]
 **is_date** | **bool**| Boolean value which represent the time is in the format date or not  | [optional]

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**200** | Response received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_assets**
> SDKResponse get_vault_assets(vault_address)

API to get Assets of a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import JavaApi.openapi_client
from JavaApi.openapi_client.api import sdk_service_api
from JavaApi.openapi_client.model.sdk_response import SDKResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8050
# See configuration.py for a list of all supported configuration parameters.
configuration = JavaApi.openapi_client.Configuration(
    host = "http://localhost:8050"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-jwt
configuration = JavaApi.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with JavaApi.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sdk_service_api.SDKSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | Address of the vault that want to know Assets 

    # example passing only required values which don't have defaults set
    try:
        # API to get Assets of a vault
        api_response = api_instance.get_vault_assets(vault_address)
        pprint(api_response)
    except JavaApi.openapi_client.ApiException as e:
        print("Exception when calling SDKSERVICEApi->get_vault_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| Address of the vault that want to know Assets  |

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**200** | Response received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_nav**
> SDKResponse get_vault_nav(vault_address)

API to get Historical NAV of a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import JavaApi.openapi_client
from JavaApi.openapi_client.api import sdk_service_api
from JavaApi.openapi_client.model.sdk_response import SDKResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8050
# See configuration.py for a list of all supported configuration parameters.
configuration = JavaApi.openapi_client.Configuration(
    host = "http://localhost:8050"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-jwt
configuration = JavaApi.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with JavaApi.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sdk_service_api.SDKSERVICEApi(api_client)
    vault_address = "vault address_example" # str | Address of the vault that want to know vault address 
    timestamp = "timestamp_example" # str | Unix timestamp or date in the format DD-MM-YYYY HH:MM:SS  (optional)
    is_date = True # bool | Boolean value which represent the time is in the format date or not  (optional)

    # example passing only required values which don't have defaults set
    try:
        # API to get Historical NAV of a vault
        api_response = api_instance.get_vault_nav(vault_address)
        pprint(api_response)
    except JavaApi.openapi_client.ApiException as e:
        print("Exception when calling SDKSERVICEApi->get_vault_nav: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to get Historical NAV of a vault
        api_response = api_instance.get_vault_nav(vault_address, timestamp=timestamp, is_date=is_date)
        pprint(api_response)
    except JavaApi.openapi_client.ApiException as e:
        print("Exception when calling SDKSERVICEApi->get_vault_nav: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| Address of the vault that want to know vault address  |
 **timestamp** | **str**| Unix timestamp or date in the format DD-MM-YYYY HH:MM:SS  | [optional]
 **is_date** | **bool**| Boolean value which represent the time is in the format date or not  | [optional]

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**200** | Response received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

