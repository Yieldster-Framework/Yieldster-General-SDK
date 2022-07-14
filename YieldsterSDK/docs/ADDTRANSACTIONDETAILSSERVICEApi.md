# YieldsterSDK.openapi_client.ADDTRANSACTIONDETAILSSERVICEApi

All URIs are relative to *http://localhost:8050*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_transaction**](ADDTRANSACTIONDETAILSSERVICEApi.md#add_transaction) | **POST** /transaction-details/v2.0/yieldster/add-transaction | 
[**delete_by_transaction_hash**](ADDTRANSACTIONDETAILSSERVICEApi.md#delete_by_transaction_hash) | **DELETE** /transaction-details/v2.0/yieldster/delete-transaction-by-hash | API to delete transaction details by transaction hash
[**get_advisor_transactions**](ADDTRANSACTIONDETAILSSERVICEApi.md#get_advisor_transactions) | **GET** /transaction-details/v2.0/yieldster/get-advisor-transactions | API to get advisor transactions by vault address
[**get_transaction_by_status**](ADDTRANSACTIONDETAILSSERVICEApi.md#get_transaction_by_status) | **GET** /transaction-details/v2.0/yieldster/filter-transaction-by-status | API to get all SUCCESS transactions of a vault.
[**get_transaction_details_by_hash**](ADDTRANSACTIONDETAILSSERVICEApi.md#get_transaction_details_by_hash) | **GET** /transaction-details/v2.0/yieldster/get-transaction-by-hash | API to get transaction details using transaction hash
[**get_transaction_details_by_type**](ADDTRANSACTIONDETAILSSERVICEApi.md#get_transaction_details_by_type) | **GET** /transaction-details/v2.0/yieldster/get-transaction-by-type | API to get transaction details using vault address
[**set_transaction_details**](ADDTRANSACTIONDETAILSSERVICEApi.md#set_transaction_details) | **POST** /transaction-details/v2.0/yieldster/save-transaction-details | API to save transaction details
[**transaction_scheduler**](ADDTRANSACTIONDETAILSSERVICEApi.md#transaction_scheduler) | **GET** /transaction-details/v2.0/yieldster/transaction-scheduler | API to update transaction details
[**update_temporary_transaction_hash**](ADDTRANSACTIONDETAILSSERVICEApi.md#update_temporary_transaction_hash) | **PUT** /transaction-details/v2.0/yieldster/update-temporary-transaction-hash | API to update temporary transaction hash
[**update_transaction_hash**](ADDTRANSACTIONDETAILSSERVICEApi.md#update_transaction_hash) | **PUT** /transaction-details/v2.0/yieldster/update-transaction-hash | API to update transaction hash
[**update_transaction_status**](ADDTRANSACTIONDETAILSSERVICEApi.md#update_transaction_status) | **PUT** /transaction-details/v2.0/yieldster/update-transaction-status | API to update transaction status


# **add_transaction**
> Response add_transaction(vault_transactions)



### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import add_transaction_details_service_api
from YieldsterSDK.openapi_client.model.response import Response
from YieldsterSDK.openapi_client.model.vault_transactions import VaultTransactions
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
    api_instance = add_transaction_details_service_api.ADDTRANSACTIONDETAILSSERVICEApi(api_client)
    vault_transactions = VaultTransactions(
        txn_id="txn_id_example",
        block_number=1,
        txn_hash="txn_hash_example",
        txn_type="DEPOSIT",
        txn_status="PENDING",
        txn_chain="ETHEREUM",
        txn_data="txn_data_example",
        wallet="METAMASK",
        from_address="from_address_example",
        to_address="to_address_example",
        signer_address="signer_address_example",
        txn_source="NORMAL",
        temp_txn_hash="temp_txn_hash_example",
        txn_time=1,
        date_of_transaction=dateutil_parser('1970-01-01T00:00:00.00Z'),
        parameter={},
        transaction_details={},
        account_address="account_address_example",
        nonce=1,
    ) # VaultTransactions | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_transaction(vault_transactions)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ADDTRANSACTIONDETAILSSERVICEApi->add_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_transactions** | [**VaultTransactions**](VaultTransactions.md)|  |

### Return type

[**Response**](Response.md)

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

# **delete_by_transaction_hash**
> Response delete_by_transaction_hash(old_txn_hash)

API to delete transaction details by transaction hash

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import add_transaction_details_service_api
from YieldsterSDK.openapi_client.model.response import Response
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
    api_instance = add_transaction_details_service_api.ADDTRANSACTIONDETAILSSERVICEApi(api_client)
    old_txn_hash = "oldTxnHash_example" # str | hash of the transaction to be delted

    # example passing only required values which don't have defaults set
    try:
        # API to delete transaction details by transaction hash
        api_response = api_instance.delete_by_transaction_hash(old_txn_hash)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ADDTRANSACTIONDETAILSSERVICEApi->delete_by_transaction_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_txn_hash** | **str**| hash of the transaction to be delted |

### Return type

[**Response**](Response.md)

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

# **get_advisor_transactions**
> Response get_advisor_transactions(vault_address)

API to get advisor transactions by vault address

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import add_transaction_details_service_api
from YieldsterSDK.openapi_client.model.response import Response
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
    api_instance = add_transaction_details_service_api.ADDTRANSACTIONDETAILSSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | vault address to get advisor transactions

    # example passing only required values which don't have defaults set
    try:
        # API to get advisor transactions by vault address
        api_response = api_instance.get_advisor_transactions(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ADDTRANSACTIONDETAILSSERVICEApi->get_advisor_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| vault address to get advisor transactions |

### Return type

[**Response**](Response.md)

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

# **get_transaction_by_status**
> Response get_transaction_by_status(vault_address)

API to get all SUCCESS transactions of a vault.

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import add_transaction_details_service_api
from YieldsterSDK.openapi_client.model.response import Response
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
    api_instance = add_transaction_details_service_api.ADDTRANSACTIONDETAILSSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get all SUCCESS transactions of a vault.
        api_response = api_instance.get_transaction_by_status(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ADDTRANSACTIONDETAILSSERVICEApi->get_transaction_by_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |

### Return type

[**Response**](Response.md)

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

# **get_transaction_details_by_hash**
> Response get_transaction_details_by_hash(txn_hash)

API to get transaction details using transaction hash

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import add_transaction_details_service_api
from YieldsterSDK.openapi_client.model.response import Response
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
    api_instance = add_transaction_details_service_api.ADDTRANSACTIONDETAILSSERVICEApi(api_client)
    txn_hash = "txnHash_example" # str | hash of the transaction

    # example passing only required values which don't have defaults set
    try:
        # API to get transaction details using transaction hash
        api_response = api_instance.get_transaction_details_by_hash(txn_hash)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ADDTRANSACTIONDETAILSSERVICEApi->get_transaction_details_by_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txn_hash** | **str**| hash of the transaction |

### Return type

[**Response**](Response.md)

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

# **get_transaction_details_by_type**
> Response get_transaction_details_by_type(vault_address)

API to get transaction details using vault address

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import add_transaction_details_service_api
from YieldsterSDK.openapi_client.model.response import Response
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
    api_instance = add_transaction_details_service_api.ADDTRANSACTIONDETAILSSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get transaction details using vault address
        api_response = api_instance.get_transaction_details_by_type(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ADDTRANSACTIONDETAILSSERVICEApi->get_transaction_details_by_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |

### Return type

[**Response**](Response.md)

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

# **set_transaction_details**
> Response set_transaction_details(block_numer, txn_hash, txn_type, txn_chain, txn_data, wallet, from_address, to_address, signer_address, tag, parameter, transaction_details)

API to save transaction details

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import add_transaction_details_service_api
from YieldsterSDK.openapi_client.model.response import Response
from YieldsterSDK.openapi_client.model.sdk_response import SDKResponse
from YieldsterSDK.openapi_client.model.str_bool_date_datetime_dict_float_int_list_str_none_type import StrBoolDateDatetimeDictFloatIntListStrNoneType
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
    api_instance = add_transaction_details_service_api.ADDTRANSACTIONDETAILSSERVICEApi(api_client)
    block_numer = 1 # int | block number of the transaction
    txn_hash = "txnHash_example" # str | hash of the transaction
    txn_type = "DEPOSIT" # str | type of the transaction
    txn_chain = "ETHEREUM" # str | chain in which transaction occured
    txn_data = "txnData_example" # str | transaction data
    wallet = "METAMASK" # str | type of the wallet used for transaction
    from_address = "fromAddress_example" # str | origin address of the transaction
    to_address = "toAddress_example" # str | destination address of the transaction
    signer_address = "signerAddress_example" # str | address used for signing the transaction
    tag = "NORMAL" # str | Source of transaction like multisig
    parameter = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Transaction parameter
    transaction_details = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Transaction details

    # example passing only required values which don't have defaults set
    try:
        # API to save transaction details
        api_response = api_instance.set_transaction_details(block_numer, txn_hash, txn_type, txn_chain, txn_data, wallet, from_address, to_address, signer_address, tag, parameter, transaction_details)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ADDTRANSACTIONDETAILSSERVICEApi->set_transaction_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_numer** | **int**| block number of the transaction |
 **txn_hash** | **str**| hash of the transaction |
 **txn_type** | **str**| type of the transaction |
 **txn_chain** | **str**| chain in which transaction occured |
 **txn_data** | **str**| transaction data |
 **wallet** | **str**| type of the wallet used for transaction |
 **from_address** | **str**| origin address of the transaction |
 **to_address** | **str**| destination address of the transaction |
 **signer_address** | **str**| address used for signing the transaction |
 **tag** | **str**| Source of transaction like multisig |
 **parameter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Transaction parameter |
 **transaction_details** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Transaction details |

### Return type

[**Response**](Response.md)

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

# **transaction_scheduler**
> Response transaction_scheduler()

API to update transaction details

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import add_transaction_details_service_api
from YieldsterSDK.openapi_client.model.response import Response
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
    api_instance = add_transaction_details_service_api.ADDTRANSACTIONDETAILSSERVICEApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API to update transaction details
        api_response = api_instance.transaction_scheduler()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ADDTRANSACTIONDETAILSSERVICEApi->transaction_scheduler: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Response**](Response.md)

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

# **update_temporary_transaction_hash**
> Response update_temporary_transaction_hash(old_txn_hash, new_txn_hash)

API to update temporary transaction hash

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import add_transaction_details_service_api
from YieldsterSDK.openapi_client.model.response import Response
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
    api_instance = add_transaction_details_service_api.ADDTRANSACTIONDETAILSSERVICEApi(api_client)
    old_txn_hash = "oldTxnHash_example" # str | old hash of the transaction
    new_txn_hash = "newTxnHash_example" # str | new hash of the transaction

    # example passing only required values which don't have defaults set
    try:
        # API to update temporary transaction hash
        api_response = api_instance.update_temporary_transaction_hash(old_txn_hash, new_txn_hash)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ADDTRANSACTIONDETAILSSERVICEApi->update_temporary_transaction_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_txn_hash** | **str**| old hash of the transaction |
 **new_txn_hash** | **str**| new hash of the transaction |

### Return type

[**Response**](Response.md)

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

# **update_transaction_hash**
> Response update_transaction_hash(old_txn_hash, new_txn_hash)

API to update transaction hash

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import add_transaction_details_service_api
from YieldsterSDK.openapi_client.model.response import Response
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
    api_instance = add_transaction_details_service_api.ADDTRANSACTIONDETAILSSERVICEApi(api_client)
    old_txn_hash = "oldTxnHash_example" # str | old hash of the transaction
    new_txn_hash = "newTxnHash_example" # str | new hash of the transaction

    # example passing only required values which don't have defaults set
    try:
        # API to update transaction hash
        api_response = api_instance.update_transaction_hash(old_txn_hash, new_txn_hash)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ADDTRANSACTIONDETAILSSERVICEApi->update_transaction_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_txn_hash** | **str**| old hash of the transaction |
 **new_txn_hash** | **str**| new hash of the transaction |

### Return type

[**Response**](Response.md)

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

# **update_transaction_status**
> SDKResponse update_transaction_status(txn_hash, new_txn_status)

API to update transaction status

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import add_transaction_details_service_api
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
    api_instance = add_transaction_details_service_api.ADDTRANSACTIONDETAILSSERVICEApi(api_client)
    txn_hash = "txnHash_example" # str | hash of the transaction
    new_txn_status = "PENDING" # str | new status of the transaction

    # example passing only required values which don't have defaults set
    try:
        # API to update transaction status
        api_response = api_instance.update_transaction_status(txn_hash, new_txn_status)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ADDTRANSACTIONDETAILSSERVICEApi->update_transaction_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txn_hash** | **str**| hash of the transaction |
 **new_txn_status** | **str**| new status of the transaction |

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

