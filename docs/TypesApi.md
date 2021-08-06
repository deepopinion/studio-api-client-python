# swagger_client.TypesApi

All URIs are relative to *https://api.deepopinion.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**types_get**](TypesApi.md#types_get) | **GET** /types | List all available task types


# **types_get**
> Types types_get()

List all available task types

<br/>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TypesApi(swagger_client.ApiClient(configuration))

try:
    # List all available task types
    api_response = api_instance.types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TypesApi->types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Types**](Types.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

