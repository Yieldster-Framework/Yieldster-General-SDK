# YieldsterSDK.openapi_client.PendingVaultTransactionControllerApi

All URIs are relative to *http://localhost:8050*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_pending_vault_transaction**](PendingVaultTransactionControllerApi.md#complete_pending_vault_transaction) | **POST** /pendingVaultTx/v2.0/yieldster/completedTransaction | API to MONITOR_VAULT_CREATION
[**create_pending_vault**](PendingVaultTransactionControllerApi.md#create_pending_vault) | **POST** /pendingVaultTx/v2.0/yieldster/create | API to CREATE PendingVaultTransaction
[**get_all_pending_vaults**](PendingVaultTransactionControllerApi.md#get_all_pending_vaults) | **GET** /pendingVaultTx/v2.0/yieldster/get | API to get ALL_PENDING_VAULT_CREATION_TRANSACTION
[**get_pending_vault_by_id**](PendingVaultTransactionControllerApi.md#get_pending_vault_by_id) | **GET** /pendingVaultTx/v2.0/yieldster/{id} | API to get PENDING_VAULT_CREATION_STATUS By ID


# **complete_pending_vault_transaction**
> SDKResponse complete_pending_vault_transaction()

API to MONITOR_VAULT_CREATION

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import pending_vault_transaction_controller_api
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
    api_instance = pending_vault_transaction_controller_api.PendingVaultTransactionControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API to MONITOR_VAULT_CREATION
        api_response = api_instance.complete_pending_vault_transaction()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PendingVaultTransactionControllerApi->complete_pending_vault_transaction: %s\n" % e)
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

# **create_pending_vault**
> SDKResponse create_pending_vault(pending_vault_transaction)

API to CREATE PendingVaultTransaction

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import pending_vault_transaction_controller_api
from YieldsterSDK.openapi_client.model.pending_vault_transaction import PendingVaultTransaction
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
    api_instance = pending_vault_transaction_controller_api.PendingVaultTransactionControllerApi(api_client)
    pending_vault_transaction = PendingVaultTransaction(
        id="id_example",
        status="PENDING",
        vault_id="vault_id_example",
        tx_hash="tx_hash_example",
        tx_type="WHITELIST_CREATION",
        transaction_details={
            "key": EthTransaction(
                id=1,
                jsonrpc="jsonrpc_example",
                result=Transaction(
                    hash="hash_example",
                    nonce=1,
                    block_hash="block_hash_example",
                    block_number=1,
                    chain_id=1,
                    transaction_index=1,
                    _from="_from_example",
                    to="to_example",
                    value=1,
                    gas_price=1,
                    gas=1,
                    input="input_example",
                    creates="creates_example",
                    public_key="public_key_example",
                    raw="raw_example",
                    r="r_example",
                    s="s_example",
                    v=1,
                    type="type_example",
                    max_fee_per_gas=1,
                    max_priority_fee_per_gas=1,
                    access_list=[
                        AccessListObject(
                            address="address_example",
                            storage_keys=[
                                "storage_keys_example",
                            ],
                        ),
                    ],
                    max_fee_per_gas_raw="max_fee_per_gas_raw_example",
                    block_number_raw="block_number_raw_example",
                    max_priority_fee_per_gas_raw="max_priority_fee_per_gas_raw_example",
                    transaction_index_raw="transaction_index_raw_example",
                    nonce_raw="nonce_raw_example",
                    gas_price_raw="gas_price_raw_example",
                    chain_id_raw="chain_id_raw_example",
                    value_raw="value_raw_example",
                    gas_raw="gas_raw_example",
                ),
                error=Error(
                    code=1,
                    message="message_example",
                    data="data_example",
                ),
                raw_response="raw_response_example",
                transaction=Transaction(
                    hash="hash_example",
                    nonce=1,
                    block_hash="block_hash_example",
                    block_number=1,
                    chain_id=1,
                    transaction_index=1,
                    _from="_from_example",
                    to="to_example",
                    value=1,
                    gas_price=1,
                    gas=1,
                    input="input_example",
                    creates="creates_example",
                    public_key="public_key_example",
                    raw="raw_example",
                    r="r_example",
                    s="s_example",
                    v=1,
                    type="type_example",
                    max_fee_per_gas=1,
                    max_priority_fee_per_gas=1,
                    access_list=[
                        AccessListObject(
                            address="address_example",
                            storage_keys=[
                                "storage_keys_example",
                            ],
                        ),
                    ],
                    max_fee_per_gas_raw="max_fee_per_gas_raw_example",
                    block_number_raw="block_number_raw_example",
                    max_priority_fee_per_gas_raw="max_priority_fee_per_gas_raw_example",
                    transaction_index_raw="transaction_index_raw_example",
                    nonce_raw="nonce_raw_example",
                    gas_price_raw="gas_price_raw_example",
                    chain_id_raw="chain_id_raw_example",
                    value_raw="value_raw_example",
                    gas_raw="gas_raw_example",
                ),
            ),
        },
        wallet_type="METAMASK",
    ) # PendingVaultTransaction | 

    # example passing only required values which don't have defaults set
    try:
        # API to CREATE PendingVaultTransaction
        api_response = api_instance.create_pending_vault(pending_vault_transaction)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PendingVaultTransactionControllerApi->create_pending_vault: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pending_vault_transaction** | [**PendingVaultTransaction**](PendingVaultTransaction.md)|  |

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

# **get_all_pending_vaults**
> SDKResponse get_all_pending_vaults()

API to get ALL_PENDING_VAULT_CREATION_TRANSACTION

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import pending_vault_transaction_controller_api
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
    api_instance = pending_vault_transaction_controller_api.PendingVaultTransactionControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API to get ALL_PENDING_VAULT_CREATION_TRANSACTION
        api_response = api_instance.get_all_pending_vaults()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PendingVaultTransactionControllerApi->get_all_pending_vaults: %s\n" % e)
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

# **get_pending_vault_by_id**
> SDKResponse get_pending_vault_by_id(id)

API to get PENDING_VAULT_CREATION_STATUS By ID

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import pending_vault_transaction_controller_api
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
    api_instance = pending_vault_transaction_controller_api.PendingVaultTransactionControllerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get PENDING_VAULT_CREATION_STATUS By ID
        api_response = api_instance.get_pending_vault_by_id(id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling PendingVaultTransactionControllerApi->get_pending_vault_by_id: %s\n" % e)
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

