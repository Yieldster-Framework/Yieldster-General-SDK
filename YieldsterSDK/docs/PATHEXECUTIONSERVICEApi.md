# YieldsterSDK.openapi_client.PATHEXECUTIONSERVICEApi

All URIs are relative to *http://localhost:8050*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_path_for_test**](PATHEXECUTIONSERVICEApi.md#execute_path_for_test) | **GET** /path-execution/execute-path-for-test | 
[**execute_strategy_path**](PATHEXECUTIONSERVICEApi.md#execute_strategy_path) | **GET** /path-execution/v2.0/yieldster/execute-strategy-path | API to execute strategy path
[**fetch_all_paths**](PATHEXECUTIONSERVICEApi.md#fetch_all_paths) | **GET** /path-execution/v2.0/yieldster/fetch-all-paths | API to get all available execution paths
[**find_paths**](PATHEXECUTIONSERVICEApi.md#find_paths) | **GET** /path-execution/v2.0/yieldster/fetch-particular-paths | API to get paths that lead us from start token to end token
[**gas_estimator**](PATHEXECUTIONSERVICEApi.md#gas_estimator) | **GET** /path-execution/gas-estimate | 
[**sample_erc20_token_balance**](PATHEXECUTIONSERVICEApi.md#sample_erc20_token_balance) | **GET** /path-execution/erctoken-balance | 
[**sample_function**](PATHEXECUTIONSERVICEApi.md#sample_function) | **GET** /path-execution/test-map | 


# **execute_path_for_test**
> SDKResponse execute_path_for_test(from_token_amount, from_token, to_token, vault_address)



### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import path_execution_service_api
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
    api_instance = path_execution_service_api.PATHEXECUTIONSERVICEApi(api_client)
    from_token_amount = 1 # int | amount of the initial token that you plan to provide for execution
    from_token = "fromToken_example" # str | Symbol of the initial token that you are providing for execution
    to_token = "toToken_example" # str | Symbol of the final token that you wish to receive at the end of the execution
    vault_address = "vaultAddress_example" # str | Symbol of the final token that you wish to receive at the end of the execution

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.execute_path_for_test(from_token_amount, from_token, to_token, vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PATHEXECUTIONSERVICEApi->execute_path_for_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_token_amount** | **int**| amount of the initial token that you plan to provide for execution |
 **from_token** | **str**| Symbol of the initial token that you are providing for execution |
 **to_token** | **str**| Symbol of the final token that you wish to receive at the end of the execution |
 **vault_address** | **str**| Symbol of the final token that you wish to receive at the end of the execution |

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
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_strategy_path**
> SDKResponse execute_strategy_path(path_id, amount, vault_address, from_token_address, to_token_address)

API to execute strategy path

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import path_execution_service_api
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
    api_instance = path_execution_service_api.PATHEXECUTIONSERVICEApi(api_client)
    path_id = "pathId_example" # str | Id of the path which you wish to execute
    amount = 1 # int | amount of the initial token that you plan to provide for execution
    vault_address = "vaultAddress_example" # str | Address of the vault through which we need to initiate the execution
    from_token_address = "fromTokenAddress_example" # str | Address of the initial token
    to_token_address = "toTokenAddress_example" # str | Address of the final token

    # example passing only required values which don't have defaults set
    try:
        # API to execute strategy path
        api_response = api_instance.execute_strategy_path(path_id, amount, vault_address, from_token_address, to_token_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PATHEXECUTIONSERVICEApi->execute_strategy_path: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_id** | **str**| Id of the path which you wish to execute |
 **amount** | **int**| amount of the initial token that you plan to provide for execution |
 **vault_address** | **str**| Address of the vault through which we need to initiate the execution |
 **from_token_address** | **str**| Address of the initial token |
 **to_token_address** | **str**| Address of the final token |

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

# **fetch_all_paths**
> SDKResponse fetch_all_paths()

API to get all available execution paths

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import path_execution_service_api
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
    api_instance = path_execution_service_api.PATHEXECUTIONSERVICEApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API to get all available execution paths
        api_response = api_instance.fetch_all_paths()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PATHEXECUTIONSERVICEApi->fetch_all_paths: %s\n" % e)
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
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_paths**
> SDKResponse find_paths(from_token_amount, from_token, to_token)

API to get paths that lead us from start token to end token

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import path_execution_service_api
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
    api_instance = path_execution_service_api.PATHEXECUTIONSERVICEApi(api_client)
    from_token_amount = "fromTokenAmount_example" # str | amount of the initial token that you plan to provide for execution
    from_token = "fromToken_example" # str | Symbol of the initial token that you are providing for execution
    to_token = "toToken_example" # str | Symbol of the final token that you wish to receive at the end of the execution

    # example passing only required values which don't have defaults set
    try:
        # API to get paths that lead us from start token to end token
        api_response = api_instance.find_paths(from_token_amount, from_token, to_token)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PATHEXECUTIONSERVICEApi->find_paths: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_token_amount** | **str**| amount of the initial token that you plan to provide for execution |
 **from_token** | **str**| Symbol of the initial token that you are providing for execution |
 **to_token** | **str**| Symbol of the final token that you wish to receive at the end of the execution |

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

# **gas_estimator**
> SDKResponse gas_estimator(from_token_amount, from_token, to_token)



### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import path_execution_service_api
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
    api_instance = path_execution_service_api.PATHEXECUTIONSERVICEApi(api_client)
    from_token_amount = "fromTokenAmount_example" # str | amount of the initial token that you plan to provide for execution
    from_token = "fromToken_example" # str | Symbol of the initial token that you are providing for execution
    to_token = "toToken_example" # str | Symbol of the final token that you wish to receive at the end of the execution

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.gas_estimator(from_token_amount, from_token, to_token)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PATHEXECUTIONSERVICEApi->gas_estimator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_token_amount** | **str**| amount of the initial token that you plan to provide for execution |
 **from_token** | **str**| Symbol of the initial token that you are providing for execution |
 **to_token** | **str**| Symbol of the final token that you wish to receive at the end of the execution |

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
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_erc20_token_balance**
> SDKResponse sample_erc20_token_balance()



### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import path_execution_service_api
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
    api_instance = path_execution_service_api.PATHEXECUTIONSERVICEApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.sample_erc20_token_balance()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PATHEXECUTIONSERVICEApi->sample_erc20_token_balance: %s\n" % e)
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
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_function**
> str sample_function()



### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import path_execution_service_api
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
    api_instance = path_execution_service_api.PATHEXECUTIONSERVICEApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.sample_function()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PATHEXECUTIONSERVICEApi->sample_function: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[bearer-jwt](../README.md#bearer-jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

