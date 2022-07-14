# YieldsterSDK.openapi_client.Erc20TransactionControllerApi

All URIs are relative to *http://localhost:8050*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_transaction_details1**](Erc20TransactionControllerApi.md#set_transaction_details1) | **POST** /Erc20Transaction/v2.0/yieldster/save-Erc20-transaction-details | API to save Erc20Transaction details


# **set_transaction_details1**
> Response set_transaction_details1(token_name, token_symbol, token_decimal, hash, time_stamp, block_numer, transaction_index, nonce, _from, to, value, index, gas, gas_price, gas_used, cumulative_gas_used, input, confirmations, contract_address)

API to save Erc20Transaction details

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import erc_20_transaction_controller_api
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
    api_instance = erc_20_transaction_controller_api.Erc20TransactionControllerApi(api_client)
    token_name = "tokenName_example" # str | tokenName
    token_symbol = "tokenSymbol_example" # str | tokenSymbol
    token_decimal = "tokenDecimal_example" # str | tokenDecimal
    hash = "hash_example" # str | hash
    time_stamp = "timeStamp_example" # str | timeStamp
    block_numer = 1 # int | block number of the transaction
    transaction_index = "TransactionIndex_example" # str | TransactionIndex
    nonce = "nonce_example" # str | nonce
    _from = "from_example" # str | from
    to = "to_example" # str | to
    value = "value_example" # str | value
    index = "index_example" # str | index
    gas = "gas_example" # str | gas
    gas_price = "gasPrice_example" # str | gasPrice
    gas_used = "gasUsed_example" # str | gasUsed
    cumulative_gas_used = "cumulativeGasUsed_example" # str | cumulativeGasUsed
    input = "input_example" # str | input
    confirmations = "Confirmations_example" # str | Confirmations
    contract_address = "contractAddress_example" # str | contractAddress

    # example passing only required values which don't have defaults set
    try:
        # API to save Erc20Transaction details
        api_response = api_instance.set_transaction_details1(token_name, token_symbol, token_decimal, hash, time_stamp, block_numer, transaction_index, nonce, _from, to, value, index, gas, gas_price, gas_used, cumulative_gas_used, input, confirmations, contract_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling Erc20TransactionControllerApi->set_transaction_details1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_name** | **str**| tokenName |
 **token_symbol** | **str**| tokenSymbol |
 **token_decimal** | **str**| tokenDecimal |
 **hash** | **str**| hash |
 **time_stamp** | **str**| timeStamp |
 **block_numer** | **int**| block number of the transaction |
 **transaction_index** | **str**| TransactionIndex |
 **nonce** | **str**| nonce |
 **_from** | **str**| from |
 **to** | **str**| to |
 **value** | **str**| value |
 **index** | **str**| index |
 **gas** | **str**| gas |
 **gas_price** | **str**| gasPrice |
 **gas_used** | **str**| gasUsed |
 **cumulative_gas_used** | **str**| cumulativeGasUsed |
 **input** | **str**| input |
 **confirmations** | **str**| Confirmations |
 **contract_address** | **str**| contractAddress |

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

