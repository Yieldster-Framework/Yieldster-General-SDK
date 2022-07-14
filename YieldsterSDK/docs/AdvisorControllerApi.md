# YieldsterSDK.openapi_client.AdvisorControllerApi

All URIs are relative to *http://localhost:8050*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_advisor_end_point**](AdvisorControllerApi.md#add_advisor_end_point) | **POST** /Advisor/add-end-point | API to add advisor endpoint
[**add_advisorkey**](AdvisorControllerApi.md#add_advisorkey) | **POST** /Advisor/sdk/v2.0/yieldster/addAdvisorKey | API to get Add Key 
[**get_advisor_by_end_point**](AdvisorControllerApi.md#get_advisor_by_end_point) | **GET** /Advisor/get-by-endPoint | API to get advisor by endpoint
[**get_advisor_by_id**](AdvisorControllerApi.md#get_advisor_by_id) | **GET** /Advisor/sdk/v2.0/yieldster/{id} | API to get Advisor by ID
[**get_all_advisor_keys**](AdvisorControllerApi.md#get_all_advisor_keys) | **GET** /Advisor/sdk/v2.0/yieldster/getAllKeys | API to get ALL_KEYS 
[**get_all_advisors**](AdvisorControllerApi.md#get_all_advisors) | **GET** /Advisor/sdk/v2.0/yieldster/get | API to get ALL_ADVISORS 
[**get_current_advisor**](AdvisorControllerApi.md#get_current_advisor) | **GET** /Advisor/sdk/v2.0/yieldster/currentAdvisor | API to get current advisor
[**run_advisor**](AdvisorControllerApi.md#run_advisor) | **GET** /Advisor/sdk/v2.0/yieldster/run | API to run advisor


# **add_advisor_end_point**
> SDKResponse add_advisor_end_point(advisor_id, end_point)

API to add advisor endpoint

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import advisor_controller_api
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
    api_instance = advisor_controller_api.AdvisorControllerApi(api_client)
    advisor_id = "advisorId_example" # str | 
    end_point = "endPoint_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to add advisor endpoint
        api_response = api_instance.add_advisor_end_point(advisor_id, end_point)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling AdvisorControllerApi->add_advisor_end_point: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advisor_id** | **str**|  |
 **end_point** | **str**|  |

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

# **add_advisorkey**
> SDKResponse add_advisorkey(advisor_key)

API to get Add Key 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import advisor_controller_api
from YieldsterSDK.openapi_client.model.advisor_key import AdvisorKey
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
    api_instance = advisor_controller_api.AdvisorControllerApi(api_client)
    advisor_key = AdvisorKey(
        id="id_example",
        key="key_example",
    ) # AdvisorKey | 

    # example passing only required values which don't have defaults set
    try:
        # API to get Add Key 
        api_response = api_instance.add_advisorkey(advisor_key)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling AdvisorControllerApi->add_advisorkey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advisor_key** | [**AdvisorKey**](AdvisorKey.md)|  |

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

# **get_advisor_by_end_point**
> SDKResponse get_advisor_by_end_point(advisor_id)

API to get advisor by endpoint

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import advisor_controller_api
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
    api_instance = advisor_controller_api.AdvisorControllerApi(api_client)
    advisor_id = "advisorId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get advisor by endpoint
        api_response = api_instance.get_advisor_by_end_point(advisor_id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling AdvisorControllerApi->get_advisor_by_end_point: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advisor_id** | **str**|  |

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

# **get_advisor_by_id**
> SDKResponse get_advisor_by_id(id)

API to get Advisor by ID

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import advisor_controller_api
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
    api_instance = advisor_controller_api.AdvisorControllerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get Advisor by ID
        api_response = api_instance.get_advisor_by_id(id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling AdvisorControllerApi->get_advisor_by_id: %s\n" % e)
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

# **get_all_advisor_keys**
> SDKResponse get_all_advisor_keys()

API to get ALL_KEYS 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import advisor_controller_api
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
    api_instance = advisor_controller_api.AdvisorControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API to get ALL_KEYS 
        api_response = api_instance.get_all_advisor_keys()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling AdvisorControllerApi->get_all_advisor_keys: %s\n" % e)
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

# **get_all_advisors**
> SDKResponse get_all_advisors()

API to get ALL_ADVISORS 

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import advisor_controller_api
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
    api_instance = advisor_controller_api.AdvisorControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API to get ALL_ADVISORS 
        api_response = api_instance.get_all_advisors()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling AdvisorControllerApi->get_all_advisors: %s\n" % e)
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

# **get_current_advisor**
> UIResponse get_current_advisor(vault_id)

API to get current advisor

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import advisor_controller_api
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
    api_instance = advisor_controller_api.AdvisorControllerApi(api_client)
    vault_id = "vaultId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API to get current advisor
        api_response = api_instance.get_current_advisor(vault_id)
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling AdvisorControllerApi->get_current_advisor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**|  |

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
**400** | Bad request, check the provided parameters |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | Response received |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_advisor**
> run_advisor()

API to run advisor

### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import advisor_controller_api
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
    api_instance = advisor_controller_api.AdvisorControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API to run advisor
        api_instance.run_advisor()
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling AdvisorControllerApi->run_advisor: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

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

