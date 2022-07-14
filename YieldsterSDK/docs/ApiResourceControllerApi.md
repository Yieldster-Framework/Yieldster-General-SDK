# YieldsterSDK.openapi_client.ApiResourceControllerApi

All URIs are relative to *http://localhost:8050*

Method | HTTP request | Description
------------- | ------------- | -------------
[**security_configuration**](ApiResourceControllerApi.md#security_configuration) | **GET** /swagger-resources/configuration/security | 
[**swagger_resources**](ApiResourceControllerApi.md#swagger_resources) | **GET** /swagger-resources | 
[**ui_configuration**](ApiResourceControllerApi.md#ui_configuration) | **GET** /swagger-resources/configuration/ui | 


# **security_configuration**
> SecurityConfiguration security_configuration()



### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import api_resource_controller_api
from YieldsterSDK.openapi_client.model.security_configuration import SecurityConfiguration
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
    api_instance = api_resource_controller_api.ApiResourceControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.security_configuration()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ApiResourceControllerApi->security_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SecurityConfiguration**](SecurityConfiguration.md)

### Authorization

[bearer-jwt](../README.md#bearer-jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **swagger_resources**
> [SwaggerResource] swagger_resources()



### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import api_resource_controller_api
from YieldsterSDK.openapi_client.model.sdk_response import SDKResponse
from YieldsterSDK.openapi_client.model.swagger_resource import SwaggerResource
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
    api_instance = api_resource_controller_api.ApiResourceControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.swagger_resources()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ApiResourceControllerApi->swagger_resources: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[SwaggerResource]**](SwaggerResource.md)

### Authorization

[bearer-jwt](../README.md#bearer-jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_configuration**
> UiConfiguration ui_configuration()



### Example

* Bearer (JWT) Authentication (bearer-jwt):

```python
import time
import YieldsterSDK.openapi_client
from YieldsterSDK.openapi_client.api import api_resource_controller_api
from YieldsterSDK.openapi_client.model.ui_configuration import UiConfiguration
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
    api_instance = api_resource_controller_api.ApiResourceControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.ui_configuration()
        pprint(api_response)
    except YieldsterSDK.openapi_client.ApiException as e:
        print("Exception when calling ApiResourceControllerApi->ui_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UiConfiguration**](UiConfiguration.md)

### Authorization

[bearer-jwt](../README.md#bearer-jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Server Error |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

