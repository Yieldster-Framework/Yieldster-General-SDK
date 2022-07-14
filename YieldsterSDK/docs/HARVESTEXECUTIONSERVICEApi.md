# YieldsterSDK.openapi_client.HARVESTEXECUTIONSERVICEApi

All URIs are relative to *http://localhost:8050*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_staking_contract**](HARVESTEXECUTIONSERVICEApi.md#add_staking_contract) | **POST** /harvest/v2.0/yieldster/add-staking-contract | API to add staking contracts and their respective rewards from file
[**add_staking_contract_and_reward**](HARVESTEXECUTIONSERVICEApi.md#add_staking_contract_and_reward) | **POST** /harvest/v2.0/yieldster/add-staking-contract-and-reward | API to add address of staking contract and its rewards
[**delete_staking_contract**](HARVESTEXECUTIONSERVICEApi.md#delete_staking_contract) | **DELETE** /harvest/v2.0/yieldster/delete-staking-contracts | API to get delete staking contract by address
[**get_harvest_gas_estimate**](HARVESTEXECUTIONSERVICEApi.md#get_harvest_gas_estimate) | **GET** /harvest/v2.0/yieldster/get-harvest-gas | API to get gas estimate of harvest function
[**get_reward_amount**](HARVESTEXECUTIONSERVICEApi.md#get_reward_amount) | **GET** /harvest/v2.0/yieldster/get-reward-amount | API to get amount of rewards of a particular contract for a vault
[**get_reward_contract**](HARVESTEXECUTIONSERVICEApi.md#get_reward_contract) | **GET** /harvest/v2.0/yieldster/get-reward-contracts | API to get address of rewards of a particular staking contract
[**get_staked_asset_of_a_pool**](HARVESTEXECUTIONSERVICEApi.md#get_staked_asset_of_a_pool) | **GET** /harvest/v2.0/yieldster/get-staking-token-from-stakedcontract | API to get address of staking token of a particular staking contract
[**harvest_reward**](HARVESTEXECUTIONSERVICEApi.md#harvest_reward) | **POST** /harvest/v2.0/yieldster/harvest-reward | API to harvest rewards of a particular contract for a vault


# **add_staking_contract**
> SDKResponse add_staking_contract()

API to add staking contracts and their respective rewards from file

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import harvest_execution_service_api
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
    api_instance = harvest_execution_service_api.HARVESTEXECUTIONSERVICEApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API to add staking contracts and their respective rewards from file
        api_response = api_instance.add_staking_contract()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling HARVESTEXECUTIONSERVICEApi->add_staking_contract: %s\n" % e)
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

# **add_staking_contract_and_reward**
> SDKResponse add_staking_contract_and_reward(staking_contract, rewards)

API to add address of staking contract and its rewards

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import harvest_execution_service_api
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
    api_instance = harvest_execution_service_api.HARVESTEXECUTIONSERVICEApi(api_client)
    staking_contract = "stakingContract_example" # str | Address of staking contract
    rewards = [
        "rewards_example",
    ] # [str] | List of reward contracts

    # example passing only required values which don't have defaults set
    try:
        # API to add address of staking contract and its rewards
        api_response = api_instance.add_staking_contract_and_reward(staking_contract, rewards)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling HARVESTEXECUTIONSERVICEApi->add_staking_contract_and_reward: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staking_contract** | **str**| Address of staking contract |
 **rewards** | **[str]**| List of reward contracts |

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

# **delete_staking_contract**
> SDKResponse delete_staking_contract(staking_contract)

API to get delete staking contract by address

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import harvest_execution_service_api
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
    api_instance = harvest_execution_service_api.HARVESTEXECUTIONSERVICEApi(api_client)
    staking_contract = "stakingContract_example" # str | Address of staking contract

    # example passing only required values which don't have defaults set
    try:
        # API to get delete staking contract by address
        api_response = api_instance.delete_staking_contract(staking_contract)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling HARVESTEXECUTIONSERVICEApi->delete_staking_contract: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staking_contract** | **str**| Address of staking contract |

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

# **get_harvest_gas_estimate**
> SDKResponse get_harvest_gas_estimate(staking_contract, vault_address)

API to get gas estimate of harvest function

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import harvest_execution_service_api
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
    api_instance = harvest_execution_service_api.HARVESTEXECUTIONSERVICEApi(api_client)
    staking_contract = "stakingContract_example" # str | Address of staking contract
    vault_address = "vaultAddress_example" # str | Address of vault

    # example passing only required values which don't have defaults set
    try:
        # API to get gas estimate of harvest function
        api_response = api_instance.get_harvest_gas_estimate(staking_contract, vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling HARVESTEXECUTIONSERVICEApi->get_harvest_gas_estimate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staking_contract** | **str**| Address of staking contract |
 **vault_address** | **str**| Address of vault |

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

# **get_reward_amount**
> SDKResponse get_reward_amount(vault_address, staking_contract)

API to get amount of rewards of a particular contract for a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import harvest_execution_service_api
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
    api_instance = harvest_execution_service_api.HARVESTEXECUTIONSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | Address of vault
    staking_contract = "stakingContract_example" # str | Address of staking contract

    # example passing only required values which don't have defaults set
    try:
        # API to get amount of rewards of a particular contract for a vault
        api_response = api_instance.get_reward_amount(vault_address, staking_contract)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling HARVESTEXECUTIONSERVICEApi->get_reward_amount: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| Address of vault |
 **staking_contract** | **str**| Address of staking contract |

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

# **get_reward_contract**
> SDKResponse get_reward_contract(staking_contract)

API to get address of rewards of a particular staking contract

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import harvest_execution_service_api
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
    api_instance = harvest_execution_service_api.HARVESTEXECUTIONSERVICEApi(api_client)
    staking_contract = "stakingContract_example" # str | Address of staking contract

    # example passing only required values which don't have defaults set
    try:
        # API to get address of rewards of a particular staking contract
        api_response = api_instance.get_reward_contract(staking_contract)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling HARVESTEXECUTIONSERVICEApi->get_reward_contract: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staking_contract** | **str**| Address of staking contract |

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

# **get_staked_asset_of_a_pool**
> SDKResponse get_staked_asset_of_a_pool(staking_contract)

API to get address of staking token of a particular staking contract

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import harvest_execution_service_api
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
    api_instance = harvest_execution_service_api.HARVESTEXECUTIONSERVICEApi(api_client)
    staking_contract = "stakingContract_example" # str | Address of staking contract

    # example passing only required values which don't have defaults set
    try:
        # API to get address of staking token of a particular staking contract
        api_response = api_instance.get_staked_asset_of_a_pool(staking_contract)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling HARVESTEXECUTIONSERVICEApi->get_staked_asset_of_a_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staking_contract** | **str**| Address of staking contract |

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

# **harvest_reward**
> SDKResponse harvest_reward(vault_address, staking_contract, return_tokens, api_key)

API to harvest rewards of a particular contract for a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import harvest_execution_service_api
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
    api_instance = harvest_execution_service_api.HARVESTEXECUTIONSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | Address of vault
    staking_contract = "stakingContract_example" # str | Address of staking contract
    return_tokens = [
        "returnTokens_example",
    ] # [str] | Array tokens that will be received after harvesting
    api_key = "apiKey_example" # str | APIKey of staking advisor

    # example passing only required values which don't have defaults set
    try:
        # API to harvest rewards of a particular contract for a vault
        api_response = api_instance.harvest_reward(vault_address, staking_contract, return_tokens, api_key)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling HARVESTEXECUTIONSERVICEApi->harvest_reward: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| Address of vault |
 **staking_contract** | **str**| Address of staking contract |
 **return_tokens** | **[str]**| Array tokens that will be received after harvesting |
 **api_key** | **str**| APIKey of staking advisor |

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

