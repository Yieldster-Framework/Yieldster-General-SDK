# YieldsterSDK.openapi_client.VAULTSERVICEApi

All URIs are relative to *http://localhost:8050*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_staked_pools**](VAULTSERVICEApi.md#add_staked_pools) | **POST** /Vault/v2.0/yieldster/addStakedPools | API to add staked pools of a vault
[**edge_activator**](VAULTSERVICEApi.md#edge_activator) | **GET** /Vault/v2.0/yieldster/edge-activator | 
[**execute_withdraw**](VAULTSERVICEApi.md#execute_withdraw) | **GET** /Vault/v2.0/yieldster/withdraw | API to execute a withdraw from a vault
[**featured_status**](VAULTSERVICEApi.md#featured_status) | **PUT** /Vault/v2.0/yieldster/update_featured_status | API to update featured Vault by Id 
[**get_advisor_details**](VAULTSERVICEApi.md#get_advisor_details) | **GET** /Vault/v2.0/yieldster/advisor-details | API to get advisor details of a vault
[**get_advisor_setting_by_vault_id**](VAULTSERVICEApi.md#get_advisor_setting_by_vault_id) | **GET** /Vault/v2.0/yieldster/getAdvisorSettingByVaultId/{vaultId} | API to get VAULT_ADVISOR_SETTINGS 
[**get_all_my_vaults**](VAULTSERVICEApi.md#get_all_my_vaults) | **GET** /Vault/v2.0/yieldster/getMyVaults/{accountAddress} | API to get MY_VAULTS by pagination
[**get_all_vaults**](VAULTSERVICEApi.md#get_all_vaults) | **GET** /Vault/v2.0/yieldster/get | API to get all vault details
[**get_all_vaults_by_pagination**](VAULTSERVICEApi.md#get_all_vaults_by_pagination) | **GET** /Vault/v2.0/yieldster/getAllVaults | API to get ALL_VAULTS By Paginating
[**get_apr**](VAULTSERVICEApi.md#get_apr) | **GET** /Vault/sdk/v2.0/yieldster/apr | API to get APR 
[**get_asset_by_vault_id**](VAULTSERVICEApi.md#get_asset_by_vault_id) | **GET** /Vault/v2.0/yieldster/getAssetByVaultId/{id} | API to get asset details of a vault
[**get_dashboard_graph**](VAULTSERVICEApi.md#get_dashboard_graph) | **GET** /Vault/v2.0/yieldster/graphData | 
[**get_details_by_search**](VAULTSERVICEApi.md#get_details_by_search) | **GET** /Vault/v2.0/yieldster/getDetailsBySearch | API to get asset, protocol and vault details by SEARCHING
[**get_details_for_auto_complete**](VAULTSERVICEApi.md#get_details_for_auto_complete) | **GET** /Vault/v2.0/yieldster/getDetailsForAutoComplete | API to achieve AUTO_COMPLETE on the basis of protocols, assets and vaults
[**get_featured_vault_details_by_pagination**](VAULTSERVICEApi.md#get_featured_vault_details_by_pagination) | **GET** /Vault/v2.0/yieldster/getFeaturedVaultDetailsByPagination | API to get FEATURED_VAULTS by pagination
[**get_fee_summary**](VAULTSERVICEApi.md#get_fee_summary) | **GET** /Vault/v2.0/yieldster/get-fee-summary | 
[**get_gas_estimate**](VAULTSERVICEApi.md#get_gas_estimate) | **GET** /Vault/v2.0/yieldster/get-gas-estimate/ | API to get gas estimate for a particular transaction
[**get_invested_protocol_by_vault_id**](VAULTSERVICEApi.md#get_invested_protocol_by_vault_id) | **GET** /Vault/v2.0/yieldster/getInvestedProtocolByVaultId/{id} | API to get invested protocol of a vault
[**get_nav_and_liquidated_value**](VAULTSERVICEApi.md#get_nav_and_liquidated_value) | **GET** /Vault/v2.0/yieldster/NAV-LiquidatedValue | API to get NAV and Liquidated value
[**get_protocols_by_vault_id**](VAULTSERVICEApi.md#get_protocols_by_vault_id) | **GET** /Vault/v2.0/yieldster/getProtocolsByVaultId/{id} | API to get supported protocols of a vault
[**get_public_vaults**](VAULTSERVICEApi.md#get_public_vaults) | **GET** /Vault/v2.0/yieldster/public-vaults | API to list all public vaults
[**get_staked_pools**](VAULTSERVICEApi.md#get_staked_pools) | **GET** /Vault/v2.0/yieldster/getStakedPools | API to get staked pools of a vault
[**get_vault_asset_listwith_historical_data**](VAULTSERVICEApi.md#get_vault_asset_listwith_historical_data) | **GET** /Vault/v2.0/yieldster/vaultAssetListwithHistoricalData | API to filter vault assetList along with historical Data 
[**get_vault_by_address**](VAULTSERVICEApi.md#get_vault_by_address) | **GET** /Vault/v2.0/yieldster/vaultByAddress | API to get VaultByAddress
[**get_vault_by_base_currency**](VAULTSERVICEApi.md#get_vault_by_base_currency) | **GET** /Vault/v2.0/yieldster/getVaultByBaseCurrency/{baseCurrency} | API to get VAULT_BY_BASE_CURRENCY
[**get_vault_by_financial_details1**](VAULTSERVICEApi.md#get_vault_by_financial_details1) | **GET** /Vault/v2.0/yieldster/getFinancialDetails/{accountAddress} | API to get Investment Details like TOTAL_BALANCE and TOTAL_RETURN for NAV BAR
[**get_vault_by_id**](VAULTSERVICEApi.md#get_vault_by_id) | **GET** /Vault/v2.0/yieldster/{id} | API to get vault details by ID 
[**get_vault_by_id1**](VAULTSERVICEApi.md#get_vault_by_id1) | **GET** /Vault/v2.0/yieldster/UserAndNavDetailsOfVaultToken | API to get vault token details of user and Token Nav 
[**get_vault_by_vault_address**](VAULTSERVICEApi.md#get_vault_by_vault_address) | **GET** /Vault/v2.0/yieldster/strategy/{vaultAddress} | API to get deposit and withdrawal strategy by Vault Address 
[**get_vault_details**](VAULTSERVICEApi.md#get_vault_details) | **GET** /Vault/v2.0/yieldster/vault-details/{vaultAddress} | 
[**get_vault_details_by_filtering_with_pagination**](VAULTSERVICEApi.md#get_vault_details_by_filtering_with_pagination) | **GET** /Vault/v2.0/yieldster/getVaultDetailsByFilter | API to get VAULT_BY_FILTERING
[**get_vault_image**](VAULTSERVICEApi.md#get_vault_image) | **GET** /Vault/sdk/v2.0/yieldster/getVaultIcon/{vaultAddress} | API to get VAULT_ICON
[**get_vault_sorted**](VAULTSERVICEApi.md#get_vault_sorted) | **POST** /Vault/v2.0/yieldster/getVaultsSorted | API to get SORTED_VAULTS
[**get_vault_transaction_by_vault_address_and_pending_or_reverted**](VAULTSERVICEApi.md#get_vault_transaction_by_vault_address_and_pending_or_reverted) | **GET** /Vault/v2.0/yieldster/filterVaultTransactionbytxstatuspendingorreverted/{vaultAddress} | API to filter vault transaction by txStatus (PENDING/REVERTED) 
[**get_whitelist_details**](VAULTSERVICEApi.md#get_whitelist_details) | **GET** /Vault/v2.0/yieldster/get-whitelist-details/{vaultAddress} | API to get whitelist details of a vault
[**profit_management_fee**](VAULTSERVICEApi.md#profit_management_fee) | **PUT** /Vault/v2.0/yieldster/updateFee | API to update PROFIT MANAGEMENT FEE 
[**switch_vault_to_private**](VAULTSERVICEApi.md#switch_vault_to_private) | **PUT** /Vault/v2.0/yieldster/switchVaultToPrivate/{vaultAddress} | API to  switch vault to private.
[**switch_vault_to_public**](VAULTSERVICEApi.md#switch_vault_to_public) | **PUT** /Vault/v2.0/yieldster/switchVaultToPublic | API to  switch vault to public.
[**update_advisor_config**](VAULTSERVICEApi.md#update_advisor_config) | **PUT** /Vault/v2.0/yieldster/update-advisor-config/{vaultAddress} | API to update advisor configuration of vault
[**update_asset_list**](VAULTSERVICEApi.md#update_asset_list) | **PUT** /Vault/v2.0/yieldster/updateAssetList | API to update Supported AssetList in a vault
[**update_deposit_strategy**](VAULTSERVICEApi.md#update_deposit_strategy) | **PUT** /Vault/v2.0/yieldster/update-deposit-strategy | API to update deposit strategy of a vault
[**update_emergency_vault_address**](VAULTSERVICEApi.md#update_emergency_vault_address) | **PUT** /Vault/v2.0/yieldster/update-emergency-vault-address/{vaultId} | API to update emergency vault address 
[**update_management_fee_percentage_and_beneficiary**](VAULTSERVICEApi.md#update_management_fee_percentage_and_beneficiary) | **PUT** /Vault/v2.0/yieldster/update-ManagementFee-Percentage-And-Beneficiary | API to update managementFee Percentage and Beneficiary 
[**update_protocol_list**](VAULTSERVICEApi.md#update_protocol_list) | **PUT** /Vault/v2.0/yieldster/updateProtocolList | API to update Supported ProtocolList in a vault
[**update_supported_assets**](VAULTSERVICEApi.md#update_supported_assets) | **PUT** /Vault/v2.0/yieldster/update-supported-assets/{vaultAddress} | API to update supported assets of vault
[**update_supported_protocols**](VAULTSERVICEApi.md#update_supported_protocols) | **PUT** /Vault/v2.0/yieldster/update-supported-protocols/{vaultAddress} | API to update supported protocols of vault
[**update_supported_vaults**](VAULTSERVICEApi.md#update_supported_vaults) | **PUT** /Vault/v2.0/yieldster/update-supported-vaults/{vaultAddress} | API to update supported vaults
[**update_vault_admin**](VAULTSERVICEApi.md#update_vault_admin) | **PUT** /Vault/v2.0/yieldster/updateVaultAdmin | API to update vault admin 
[**update_vault_name**](VAULTSERVICEApi.md#update_vault_name) | **PUT** /Vault/v2.0/yieldster/update-vault-name/{vaultId} | API to update vault name 
[**update_vault_visibility**](VAULTSERVICEApi.md#update_vault_visibility) | **PUT** /Vault/v2.0/yieldster/update-vault-visibility/ | API to update vault visibility 
[**update_withdrawal_strategy**](VAULTSERVICEApi.md#update_withdrawal_strategy) | **PUT** /Vault/v2.0/yieldster/update-withdrawal-strategy/{vaultAddress} | API to update withdrawal strategy of vault
[**user_investment_details**](VAULTSERVICEApi.md#user_investment_details) | **GET** /Vault/v2.0/yieldster/user-investment-details | 


# **add_staked_pools**
> SDKResponse add_staked_pools(vault_address, pool_address)

API to add staked pools of a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | address of vault
    pool_address = "poolAddress_example" # str | address of pool

    # example passing only required values which don't have defaults set
    try:
        # API to add staked pools of a vault
        api_response = api_instance.add_staked_pools(vault_address, pool_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->add_staked_pools: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| address of vault |
 **pool_address** | **str**| address of pool |

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

# **edge_activator**
> UIResponse edge_activator(vault_address)



### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
from YieldsterSDK.openapi_client.model.sdk_response import SDKResponse
from YieldsterSDK.openapi_client.model.ui_response import UIResponse
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | address of vault

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edge_activator(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->edge_activator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| address of vault |

### Return type

[**UIResponse**](UIResponse.md)

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

# **execute_withdraw**
> Response execute_withdraw(account_address, value, to_token, amount, instruction, vault_address)

API to execute a withdraw from a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    account_address = "accountAddress_example" # str | accountAddress
    value = 3.14 # float | value
    to_token = "toToken_example" # str | To Token Address 
    amount = 3.14 # float | amount
    instruction = "instruction_example" # str | Signed Instruction 
    vault_address = "vaultAddress_example" # str | Vault Address

    # example passing only required values which don't have defaults set
    try:
        # API to execute a withdraw from a vault
        api_response = api_instance.execute_withdraw(account_address, value, to_token, amount, instruction, vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->execute_withdraw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_address** | **str**| accountAddress |
 **value** | **float**| value |
 **to_token** | **str**| To Token Address  |
 **amount** | **float**| amount |
 **instruction** | **str**| Signed Instruction  |
 **vault_address** | **str**| Vault Address |

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

# **featured_status**
> SDKResponse featured_status(id)

API to update featured Vault by Id 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    id = "id_example" # str | 
    featured_vault = False # bool | boolean value (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # API to update featured Vault by Id 
        api_response = api_instance.featured_status(id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->featured_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to update featured Vault by Id 
        api_response = api_instance.featured_status(id, featured_vault=featured_vault)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->featured_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **featured_vault** | **bool**| boolean value | [optional] if omitted the server will use the default value of False

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

# **get_advisor_details**
> Response get_advisor_details(vault_address)

API to get advisor details of a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | vault address

    # example passing only required values which don't have defaults set
    try:
        # API to get advisor details of a vault
        api_response = api_instance.get_advisor_details(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_advisor_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| vault address |

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
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advisor_setting_by_vault_id**
> SDKResponse get_advisor_setting_by_vault_id(vault_id)

API to get VAULT_ADVISOR_SETTINGS 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_id = "vaultId_example" # str | VaultId of a particular Vault whose strategy details you need to know

    # example passing only required values which don't have defaults set
    try:
        # API to get VAULT_ADVISOR_SETTINGS 
        api_response = api_instance.get_advisor_setting_by_vault_id(vault_id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_advisor_setting_by_vault_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**| VaultId of a particular Vault whose strategy details you need to know |

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

# **get_all_my_vaults**
> SDKResponse get_all_my_vaults(account_address)

API to get MY_VAULTS by pagination

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    account_address = "accountAddress_example" # str | 
    page_no = 0 # int |  (optional) if omitted the server will use the default value of 0
    page_size = 0 # int |  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # API to get MY_VAULTS by pagination
        api_response = api_instance.get_all_my_vaults(account_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_all_my_vaults: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to get MY_VAULTS by pagination
        api_response = api_instance.get_all_my_vaults(account_address, page_no=page_no, page_size=page_size)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_all_my_vaults: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_address** | **str**|  |
 **page_no** | **int**|  | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 0

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

# **get_all_vaults**
> SDKResponse get_all_vaults()

API to get all vault details

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API to get all vault details
        api_response = api_instance.get_all_vaults()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_all_vaults: %s\n" % e)
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

# **get_all_vaults_by_pagination**
> SDKResponse get_all_vaults_by_pagination()

API to get ALL_VAULTS By Paginating

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    page_number = 0 # int | Expected page number to be displayed: Starting from 0  (optional) if omitted the server will use the default value of 0
    page_size = 0 # int | Expected size of a page to be displayed: Starting from 1 (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to get ALL_VAULTS By Paginating
        api_response = api_instance.get_all_vaults_by_pagination(page_number=page_number, page_size=page_size)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_all_vaults_by_pagination: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Expected page number to be displayed: Starting from 0  | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| Expected size of a page to be displayed: Starting from 1 | [optional] if omitted the server will use the default value of 0

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

# **get_apr**
> Response get_apr(vault_address)

API to get APR 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get APR 
        api_response = api_instance.get_apr(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_apr: %s\n" % e)
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

# **get_asset_by_vault_id**
> Response get_asset_by_vault_id(id)

API to get asset details of a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get asset details of a vault
        api_response = api_instance.get_asset_by_vault_id(id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_asset_by_vault_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_graph**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dashboard_graph(vault_address, account_address, filter)



### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | address of vault
    account_address = "accountAddress_example" # str | address of user
    filter = "filter_example" # str | filter type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_dashboard_graph(vault_address, account_address, filter)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_dashboard_graph: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| address of vault |
 **account_address** | **str**| address of user |
 **filter** | **str**| filter type |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **get_details_by_search**
> SDKResponse get_details_by_search(data)

API to get asset, protocol and vault details by SEARCHING

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    data = "data_example" # str | Name that you need to filter 

    # example passing only required values which don't have defaults set
    try:
        # API to get asset, protocol and vault details by SEARCHING
        api_response = api_instance.get_details_by_search(data)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_details_by_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**| Name that you need to filter  |

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

# **get_details_for_auto_complete**
> SDKResponse get_details_for_auto_complete(data)

API to achieve AUTO_COMPLETE on the basis of protocols, assets and vaults

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    data = "data_example" # str | Name of a protocol,asset or vault

    # example passing only required values which don't have defaults set
    try:
        # API to achieve AUTO_COMPLETE on the basis of protocols, assets and vaults
        api_response = api_instance.get_details_for_auto_complete(data)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_details_for_auto_complete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**| Name of a protocol,asset or vault |

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

# **get_featured_vault_details_by_pagination**
> SDKResponse get_featured_vault_details_by_pagination()

API to get FEATURED_VAULTS by pagination

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    page_number = 0 # int | Expected page number to be displayed: Starting from 0  (optional) if omitted the server will use the default value of 0
    page_size = 0 # int | Expected size of a page to be displayed: Starting from 1 (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to get FEATURED_VAULTS by pagination
        api_response = api_instance.get_featured_vault_details_by_pagination(page_number=page_number, page_size=page_size)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_featured_vault_details_by_pagination: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Expected page number to be displayed: Starting from 0  | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| Expected size of a page to be displayed: Starting from 1 | [optional] if omitted the server will use the default value of 0

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

# **get_fee_summary**
> Response get_fee_summary(vault_address)



### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | fee summary of a vault

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fee_summary(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_fee_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| fee summary of a vault |

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
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gas_estimate**
> Response get_gas_estimate(vault_address, token_address, transaction_data, account_address)

API to get gas estimate for a particular transaction

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    token_address = "tokenAddress_example" # str | 
    transaction_data = "transactionData_example" # str | 
    account_address = "accountAddress_example" # str | 
    amount = 0.0 # float |  (optional) if omitted the server will use the default value of 0.0

    # example passing only required values which don't have defaults set
    try:
        # API to get gas estimate for a particular transaction
        api_response = api_instance.get_gas_estimate(vault_address, token_address, transaction_data, account_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_gas_estimate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to get gas estimate for a particular transaction
        api_response = api_instance.get_gas_estimate(vault_address, token_address, transaction_data, account_address, amount=amount)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_gas_estimate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **token_address** | **str**|  |
 **transaction_data** | **str**|  |
 **account_address** | **str**|  |
 **amount** | **float**|  | [optional] if omitted the server will use the default value of 0.0

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

# **get_invested_protocol_by_vault_id**
> SDKResponse get_invested_protocol_by_vault_id(id)

API to get invested protocol of a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get invested protocol of a vault
        api_response = api_instance.get_invested_protocol_by_vault_id(id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_invested_protocol_by_vault_id: %s\n" % e)
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

# **get_nav_and_liquidated_value**
> Response get_nav_and_liquidated_value(vault_address, account_address)

API to get NAV and Liquidated value

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | vault address of the user
    account_address = "accountAddress_example" # str | account address of the user

    # example passing only required values which don't have defaults set
    try:
        # API to get NAV and Liquidated value
        api_response = api_instance.get_nav_and_liquidated_value(vault_address, account_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_nav_and_liquidated_value: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| vault address of the user |
 **account_address** | **str**| account address of the user |

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

# **get_protocols_by_vault_id**
> SDKResponse get_protocols_by_vault_id(id)

API to get supported protocols of a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get supported protocols of a vault
        api_response = api_instance.get_protocols_by_vault_id(id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_protocols_by_vault_id: %s\n" % e)
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

# **get_public_vaults**
> Response get_public_vaults()

API to list all public vaults

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API to list all public vaults
        api_response = api_instance.get_public_vaults()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_public_vaults: %s\n" % e)
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

# **get_staked_pools**
> SDKResponse get_staked_pools(vault_address)

API to get staked pools of a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | address of vault

    # example passing only required values which don't have defaults set
    try:
        # API to get staked pools of a vault
        api_response = api_instance.get_staked_pools(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_staked_pools: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| address of vault |

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

# **get_vault_asset_listwith_historical_data**
> Response get_vault_asset_listwith_historical_data(vault_address, timestamp, base_currency)

API to filter vault assetList along with historical Data 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    timestamp = "timestamp_example" # str |  YYYY-MM-DD HH:MM:SS 
    base_currency = "baseCurrency_example" # str | Base Currency 

    # example passing only required values which don't have defaults set
    try:
        # API to filter vault assetList along with historical Data 
        api_response = api_instance.get_vault_asset_listwith_historical_data(vault_address, timestamp, base_currency)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_asset_listwith_historical_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **timestamp** | **str**|  YYYY-MM-DD HH:MM:SS  |
 **base_currency** | **str**| Base Currency  |

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

# **get_vault_by_address**
> Response get_vault_by_address(vault_address)

API to get VaultByAddress

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | vault address of the user

    # example passing only required values which don't have defaults set
    try:
        # API to get VaultByAddress
        api_response = api_instance.get_vault_by_address(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| vault address of the user |

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

# **get_vault_by_base_currency**
> SDKResponse get_vault_by_base_currency(base_currency)

API to get VAULT_BY_BASE_CURRENCY

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    base_currency = "baseCurrency_example" # str | VaultId of a particular Vault whose strategy details you need to know

    # example passing only required values which don't have defaults set
    try:
        # API to get VAULT_BY_BASE_CURRENCY
        api_response = api_instance.get_vault_by_base_currency(base_currency)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_by_base_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_currency** | **str**| VaultId of a particular Vault whose strategy details you need to know |

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

# **get_vault_by_financial_details1**
> SDKResponse get_vault_by_financial_details1(account_address)

API to get Investment Details like TOTAL_BALANCE and TOTAL_RETURN for NAV BAR

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    account_address = "accountAddress_example" # str | Account address of the user

    # example passing only required values which don't have defaults set
    try:
        # API to get Investment Details like TOTAL_BALANCE and TOTAL_RETURN for NAV BAR
        api_response = api_instance.get_vault_by_financial_details1(account_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_by_financial_details1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_address** | **str**| Account address of the user |

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

# **get_vault_by_id**
> SDKResponse get_vault_by_id(id)

API to get vault details by ID 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get vault details by ID 
        api_response = api_instance.get_vault_by_id(id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_by_id: %s\n" % e)
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

# **get_vault_by_id1**
> Response get_vault_by_id1(account_address, vault_address)

API to get vault token details of user and Token Nav 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    account_address = "accountAddress_example" # str | 
    vault_address = "vaultAddress_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get vault token details of user and Token Nav 
        api_response = api_instance.get_vault_by_id1(account_address, vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_by_id1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_address** | **str**|  |
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

# **get_vault_by_vault_address**
> Response get_vault_by_vault_address(vault_address)

API to get deposit and withdrawal strategy by Vault Address 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get deposit and withdrawal strategy by Vault Address 
        api_response = api_instance.get_vault_by_vault_address(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_by_vault_address: %s\n" % e)
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

# **get_vault_details**
> Response get_vault_details(vault_address)



### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_vault_details(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_details: %s\n" % e)
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
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_details_by_filtering_with_pagination**
> SDKResponse get_vault_details_by_filtering_with_pagination(type, account_address)

API to get VAULT_BY_FILTERING

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    type = "FEATURED_VAULT" # str | Expected type of vaultDetails to be displayed
    account_address = "accountAddress_example" # str | AccountAddress of a particular user
    data = "data_example" # str | Search Vault Details by AssetName, Protocol Name, Vault Name (optional)
    page_number = 0 # int | Expected page number to be displayed: Starting from 0  (optional) if omitted the server will use the default value of 0
    page_size = 0 # int | Expected size of a page to be displayed: Starting from 1 (optional) if omitted the server will use the default value of 0
    base_currency = "baseCurrency_example" # str | Expected vaultDetails by BaseCurrency to be displayed (optional)

    # example passing only required values which don't have defaults set
    try:
        # API to get VAULT_BY_FILTERING
        api_response = api_instance.get_vault_details_by_filtering_with_pagination(type, account_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_details_by_filtering_with_pagination: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to get VAULT_BY_FILTERING
        api_response = api_instance.get_vault_details_by_filtering_with_pagination(type, account_address, data=data, page_number=page_number, page_size=page_size, base_currency=base_currency)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_details_by_filtering_with_pagination: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Expected type of vaultDetails to be displayed |
 **account_address** | **str**| AccountAddress of a particular user |
 **data** | **str**| Search Vault Details by AssetName, Protocol Name, Vault Name | [optional]
 **page_number** | **int**| Expected page number to be displayed: Starting from 0  | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| Expected size of a page to be displayed: Starting from 1 | [optional] if omitted the server will use the default value of 0
 **base_currency** | **str**| Expected vaultDetails by BaseCurrency to be displayed | [optional]

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

# **get_vault_image**
> [str] get_vault_image(vault_address)

API to get VAULT_ICON

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get VAULT_ICON
        api_response = api_instance.get_vault_image(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |

### Return type

**[str]**

### Authorization

[bearer-jwt](../README.md#bearer-jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, image/png, image/jpeg


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_sorted**
> SDKResponse get_vault_sorted(vault_display_model)

API to get SORTED_VAULTS

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
from YieldsterSDK.openapi_client.model.vault_display_model import VaultDisplayModel
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_display_model = [
        VaultDisplayModel(
            vault=Vault(
                id="id_example",
                vault_address="vault_address_example",
                vault_name="vault_name_example",
                description="description_example",
                logo_img=Binary(
                    type='YQ==',
                    data=[
                        'YQ==',
                    ],
                ),
                base_currency="base_currency_example",
                organization_data="organization_data_example",
                supported_assets=[
                    "supported_assets_example",
                ],
                vault_type="PUBLIC",
                supported_protocols=[
                    "supported_protocols_example",
                ],
                supported_vaults=[
                    "supported_vaults_example",
                ],
                reward_token_name="reward_token_name_example",
                reward_token_symbol="reward_token_symbol_example",
                token_name="token_name_example",
                token_symbol="token_symbol_example",
                vault_admin="vault_admin_example",
                optimal_cash_balance=1,
                investment_limit=1,
                advisor_id="advisor_id_example",
                staked_pools=[
                    "staked_pools_example",
                ],
                advisor_end_point="advisor_end_point_example",
                advisor_email="advisor_email_example",
                white_list_group_id=[
                    "white_list_group_id_example",
                ],
                vault_advisor_setting={
                    "key": {},
                },
                invested_protocol="invested_protocol_example",
                mangement_fee=3.14,
                deposit_strategy="deposit_strategy_example",
                withdrawal_strategy="withdrawal_strategy_example",
                emergency_vault_address="emergency_vault_address_example",
                beneficiary_address="beneficiary_address_example",
                fee_strategy_list=[
                    "fee_strategy_list_example",
                ],
                last_advisor_execution_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                block_number=1,
                wallet_address="wallet_address_example",
                management_fee_details={
                    "key": FeeModel(
                        beneficiary="beneficiary_example",
                        percentage=3.14,
                    ),
                },
                locked=True,
                visible=True,
                featured_vault=True,
                emergency_break_set=True,
            ),
            total_nav=SDKResponse(
                data={},
                message="message_example",
                transaction_hash="transaction_hash_example",
                error={},
                status_code=1,
            ),
            token_nav=SDKResponse(
                data={},
                message="message_example",
                transaction_hash="transaction_hash_example",
                error={},
                status_code=1,
            ),
            total_apr=3.14,
            one_week_apr=3.14,
            one_month_apr=3.14,
            one_day_apr=3.14,
            asset_img_url=[
                "asset_img_url_example",
            ],
        ),
    ] # [VaultDisplayModel] | 
    category = "TotalNAV" # str | Category for sort (optional) if omitted the server will use the default value of "TotalNAV"
    type = "Descend" # str | Category for sort (optional) if omitted the server will use the default value of "Descend"

    # example passing only required values which don't have defaults set
    try:
        # API to get SORTED_VAULTS
        api_response = api_instance.get_vault_sorted(vault_display_model)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_sorted: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to get SORTED_VAULTS
        api_response = api_instance.get_vault_sorted(vault_display_model, category=category, type=type)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_sorted: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_display_model** | [**[VaultDisplayModel]**](VaultDisplayModel.md)|  |
 **category** | **str**| Category for sort | [optional] if omitted the server will use the default value of "TotalNAV"
 **type** | **str**| Category for sort | [optional] if omitted the server will use the default value of "Descend"

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

# **get_vault_transaction_by_vault_address_and_pending_or_reverted**
> Response get_vault_transaction_by_vault_address_and_pending_or_reverted(vault_address)

API to filter vault transaction by txStatus (PENDING/REVERTED) 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to filter vault transaction by txStatus (PENDING/REVERTED) 
        api_response = api_instance.get_vault_transaction_by_vault_address_and_pending_or_reverted(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_vault_transaction_by_vault_address_and_pending_or_reverted: %s\n" % e)
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

# **get_whitelist_details**
> Response get_whitelist_details(vault_address)

API to get whitelist details of a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get whitelist details of a vault
        api_response = api_instance.get_whitelist_details(vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->get_whitelist_details: %s\n" % e)
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

# **profit_management_fee**
> Response profit_management_fee(vault_address, management_fee)

API to update PROFIT MANAGEMENT FEE 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    management_fee = 3.14 # float | 

    # example passing only required values which don't have defaults set
    try:
        # API to update PROFIT MANAGEMENT FEE 
        api_response = api_instance.profit_management_fee(vault_address, management_fee)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->profit_management_fee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **management_fee** | **float**|  |

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

# **switch_vault_to_private**
> Response switch_vault_to_private(vault_address, white_list)

API to  switch vault to private.

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
from YieldsterSDK.openapi_client.model.response import Response
from YieldsterSDK.openapi_client.model.white_list import WhiteList
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    white_list = WhiteList(
        id="id_example",
        user_list=[
            {},
        ],
        admin="admin_example",
        group_name="group_name_example",
        group_id="group_id_example",
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        private=True,
    ) # WhiteList | 

    # example passing only required values which don't have defaults set
    try:
        # API to  switch vault to private.
        api_response = api_instance.switch_vault_to_private(vault_address, white_list)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->switch_vault_to_private: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **white_list** | [**WhiteList**](WhiteList.md)|  |

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

# **switch_vault_to_public**
> Response switch_vault_to_public(vault_address, account_address)

API to  switch vault to public.

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    account_address = "accountAddress_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to  switch vault to public.
        api_response = api_instance.switch_vault_to_public(vault_address, account_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->switch_vault_to_public: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **account_address** | **str**|  |

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

# **update_advisor_config**
> Response update_advisor_config(vault_address, advisor_id, request_body)

API to update advisor configuration of vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    advisor_id = "advisorId_example" # str | 
    request_body = {
        "key": {},
    } # {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)} | 

    # example passing only required values which don't have defaults set
    try:
        # API to update advisor configuration of vault
        api_response = api_instance.update_advisor_config(vault_address, advisor_id, request_body)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->update_advisor_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **advisor_id** | **str**|  |
 **request_body** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}**|  |

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

# **update_asset_list**
> Response update_asset_list(vault_address, asset_address)

API to update Supported AssetList in a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    asset_address = [
        "assetAddress_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # API to update Supported AssetList in a vault
        api_response = api_instance.update_asset_list(vault_address, asset_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->update_asset_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **asset_address** | **[str]**|  |

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

# **update_deposit_strategy**
> Response update_deposit_strategy(vault_address, deposit_strategy)

API to update deposit strategy of a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    deposit_strategy = "depositStrategy_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to update deposit strategy of a vault
        api_response = api_instance.update_deposit_strategy(vault_address, deposit_strategy)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->update_deposit_strategy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **deposit_strategy** | **str**|  |

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
**400** | Bad Request, check the provided parameters |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | Response received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_emergency_vault_address**
> Response update_emergency_vault_address(vault_id, emergency_vault_address)

API to update emergency vault address 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_id = "vaultId_example" # str | 
    emergency_vault_address = "emergencyVaultAddress_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to update emergency vault address 
        api_response = api_instance.update_emergency_vault_address(vault_id, emergency_vault_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->update_emergency_vault_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**|  |
 **emergency_vault_address** | **str**|  |

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

# **update_management_fee_percentage_and_beneficiary**
> Response update_management_fee_percentage_and_beneficiary(vault_address, fee_address, beneficiary_address, percentage)

API to update managementFee Percentage and Beneficiary 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    fee_address = "feeAddress_example" # str | 
    beneficiary_address = "beneficiaryAddress_example" # str | 
    percentage = 3.14 # float | 

    # example passing only required values which don't have defaults set
    try:
        # API to update managementFee Percentage and Beneficiary 
        api_response = api_instance.update_management_fee_percentage_and_beneficiary(vault_address, fee_address, beneficiary_address, percentage)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->update_management_fee_percentage_and_beneficiary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **fee_address** | **str**|  |
 **beneficiary_address** | **str**|  |
 **percentage** | **float**|  |

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

# **update_protocol_list**
> Response update_protocol_list(vault_address, protocol_address)

API to update Supported ProtocolList in a vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    protocol_address = [
        "protocolAddress_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # API to update Supported ProtocolList in a vault
        api_response = api_instance.update_protocol_list(vault_address, protocol_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->update_protocol_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **protocol_address** | **[str]**|  |

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

# **update_supported_assets**
> Response update_supported_assets(vault_address, request_body)

API to update supported assets of vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    request_body = [
        "request_body_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # API to update supported assets of vault
        api_response = api_instance.update_supported_assets(vault_address, request_body)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->update_supported_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **request_body** | **[str]**|  |

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

# **update_supported_protocols**
> Response update_supported_protocols(vault_address, request_body)

API to update supported protocols of vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    request_body = [
        "request_body_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # API to update supported protocols of vault
        api_response = api_instance.update_supported_protocols(vault_address, request_body)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->update_supported_protocols: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **request_body** | **[str]**|  |

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

# **update_supported_vaults**
> Response update_supported_vaults(vault_address, request_body)

API to update supported vaults

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    request_body = [
        "request_body_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # API to update supported vaults
        api_response = api_instance.update_supported_vaults(vault_address, request_body)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->update_supported_vaults: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **request_body** | **[str]**|  |

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

# **update_vault_admin**
> Response update_vault_admin(vault_id, current_admin_address, new_admin_address)

API to update vault admin 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_id = "vaultId_example" # str | 
    current_admin_address = "currentAdminAddress_example" # str | 
    new_admin_address = "newAdminAddress_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to update vault admin 
        api_response = api_instance.update_vault_admin(vault_id, current_admin_address, new_admin_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->update_vault_admin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**|  |
 **current_admin_address** | **str**|  |
 **new_admin_address** | **str**|  |

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

# **update_vault_name**
> Response update_vault_name(vault_id, vault_name)

API to update vault name 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_id = "vaultId_example" # str | 
    vault_name = "vaultName_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to update vault name 
        api_response = api_instance.update_vault_name(vault_id, vault_name)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->update_vault_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**|  |
 **vault_name** | **str**|  |

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

# **update_vault_visibility**
> Response update_vault_visibility(vault_address, is_visible)

API to update vault visibility 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | vault address
    is_visible = True # bool | 

    # example passing only required values which don't have defaults set
    try:
        # API to update vault visibility 
        api_response = api_instance.update_vault_visibility(vault_address, is_visible)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->update_vault_visibility: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| vault address |
 **is_visible** | **bool**|  |

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

# **update_withdrawal_strategy**
> Response update_withdrawal_strategy(vault_address, withdrawal_strategy)

API to update withdrawal strategy of vault

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | 
    withdrawal_strategy = "withdrawalStrategy_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to update withdrawal strategy of vault
        api_response = api_instance.update_withdrawal_strategy(vault_address, withdrawal_strategy)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->update_withdrawal_strategy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**|  |
 **withdrawal_strategy** | **str**|  |

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

# **user_investment_details**
> UIResponse user_investment_details(vault_address, account_address)



### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import vault_service_api
from YieldsterSDK.openapi_client.model.sdk_response import SDKResponse
from YieldsterSDK.openapi_client.model.ui_response import UIResponse
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
    api_instance = vault_service_api.VAULTSERVICEApi(api_client)
    vault_address = "vaultAddress_example" # str | address of vault
    account_address = "accountAddress_example" # str | address of user

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_investment_details(vault_address, account_address)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling VAULTSERVICEApi->user_investment_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_address** | **str**| address of vault |
 **account_address** | **str**| address of user |

### Return type

[**UIResponse**](UIResponse.md)

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

