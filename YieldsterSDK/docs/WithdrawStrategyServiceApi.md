# YieldsterSDK.openapi_client.WithdrawStrategyServiceApi

All URIs are relative to *http://localhost:8050*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fee_list**](WithdrawStrategyServiceApi.md#add_fee_list) | **POST** /WithDrawStrategy/v2.0/yieldster/add-fee | API to add withdraw strategy
[**get_all_withdraw_strategy**](WithdrawStrategyServiceApi.md#get_all_withdraw_strategy) | **GET** /WithDrawStrategy/v2.0/yieldster/get | API to get all withdraw Strategy details
[**get_fee_strategy_by_id**](WithdrawStrategyServiceApi.md#get_fee_strategy_by_id) | **GET** /WithDrawStrategy/v2.0/yieldster/{id} | API to get withdrawal strategy details by ID 


# **add_fee_list**
> SDKResponse add_fee_list(withdrawal_strategy)

API to add withdraw strategy

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import withdraw_strategy_service_api
from YieldsterSDK.openapi_client.model.sdk_response import SDKResponse
from YieldsterSDK.openapi_client.model.withdrawal_strategy import WithdrawalStrategy
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
    api_instance = withdraw_strategy_service_api.WithdrawStrategyServiceApi(api_client)
    withdrawal_strategy = WithdrawalStrategy(
        id="id_example",
        name="name_example",
        description="description_example",
        strategy_address="strategy_address_example",
        strategy_img_url="strategy_img_url_example",
    ) # WithdrawalStrategy | 

    # example passing only required values which don't have defaults set
    try:
        # API to add withdraw strategy
        api_response = api_instance.add_fee_list(withdrawal_strategy)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling WithdrawStrategyServiceApi->add_fee_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withdrawal_strategy** | [**WithdrawalStrategy**](WithdrawalStrategy.md)|  |

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

# **get_all_withdraw_strategy**
> SDKResponse get_all_withdraw_strategy()

API to get all withdraw Strategy details

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import withdraw_strategy_service_api
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
    api_instance = withdraw_strategy_service_api.WithdrawStrategyServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API to get all withdraw Strategy details
        api_response = api_instance.get_all_withdraw_strategy()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling WithdrawStrategyServiceApi->get_all_withdraw_strategy: %s\n" % e)
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

# **get_fee_strategy_by_id**
> SDKResponse get_fee_strategy_by_id(id)

API to get withdrawal strategy details by ID 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import withdraw_strategy_service_api
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
    api_instance = withdraw_strategy_service_api.WithdrawStrategyServiceApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get withdrawal strategy details by ID 
        api_response = api_instance.get_fee_strategy_by_id(id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling WithdrawStrategyServiceApi->get_fee_strategy_by_id: %s\n" % e)
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

