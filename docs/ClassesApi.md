# swagger_client.ClassesApi

All URIs are relative to *https://api.deepopinion.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_classes_class_id_delete**](ClassesApi.md#projects_project_id_classes_class_id_delete) | **DELETE** /projects/{project_id}/classes/{class_id} | Delete a class
[**projects_project_id_classes_class_id_get**](ClassesApi.md#projects_project_id_classes_class_id_get) | **GET** /projects/{project_id}/classes/{class_id} | Get a class
[**projects_project_id_classes_class_id_put**](ClassesApi.md#projects_project_id_classes_class_id_put) | **PUT** /projects/{project_id}/classes/{class_id} | Change class&#39;s data
[**projects_project_id_classes_download_get**](ClassesApi.md#projects_project_id_classes_download_get) | **GET** /projects/{project_id}/classes/download | Download all project&#39;s classes
[**projects_project_id_classes_get**](ClassesApi.md#projects_project_id_classes_get) | **GET** /projects/{project_id}/classes | Get all project&#39;s classes
[**projects_project_id_classes_post**](ClassesApi.md#projects_project_id_classes_post) | **POST** /projects/{project_id}/classes | Add a new class to a project
[**projects_project_id_classes_upload_post**](ClassesApi.md#projects_project_id_classes_upload_post) | **POST** /projects/{project_id}/classes/upload | Upload a file containing classes definition.
[**projects_project_id_upload_classes_post**](ClassesApi.md#projects_project_id_upload_classes_post) | **POST** /projects/{project_id}/upload-classes | Add multiple classes to a project


# **projects_project_id_classes_class_id_delete**
> projects_project_id_classes_class_id_delete(project_id, class_id)

Delete a class

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
api_instance = swagger_client.ClassesApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project that contains the class
class_id = 56 # int | ID of the class to delete

try:
    # Delete a class
    api_instance.projects_project_id_classes_class_id_delete(project_id, class_id)
except ApiException as e:
    print("Exception when calling ClassesApi->projects_project_id_classes_class_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project that contains the class | 
 **class_id** | **int**| ID of the class to delete | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_classes_class_id_get**
> ModelClass projects_project_id_classes_class_id_get(project_id, class_id)

Get a class

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
api_instance = swagger_client.ClassesApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project that contains the class
class_id = 56 # int | ID of the class to get

try:
    # Get a class
    api_response = api_instance.projects_project_id_classes_class_id_get(project_id, class_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassesApi->projects_project_id_classes_class_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project that contains the class | 
 **class_id** | **int**| ID of the class to get | 

### Return type

[**ModelClass**](ModelClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_classes_class_id_put**
> ModelClass projects_project_id_classes_class_id_put(project_id, class_id, body)

Change class's data

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
api_instance = swagger_client.ClassesApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project to change
class_id = 56 # int | ID of the class to change
body = swagger_client.ModelClass() # ModelClass | 

try:
    # Change class's data
    api_response = api_instance.projects_project_id_classes_class_id_put(project_id, class_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassesApi->projects_project_id_classes_class_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project to change | 
 **class_id** | **int**| ID of the class to change | 
 **body** | [**ModelClass**](ModelClass.md)|  | 

### Return type

[**ModelClass**](ModelClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_classes_download_get**
> projects_project_id_classes_download_get(project_id, format=format)

Download all project's classes

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
api_instance = swagger_client.ClassesApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
format = 'format_example' # str | File format. Possible values are csv, jsonl, json and xlsx (optional)

try:
    # Download all project's classes
    api_instance.projects_project_id_classes_download_get(project_id, format=format)
except ApiException as e:
    print("Exception when calling ClassesApi->projects_project_id_classes_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **format** | **str**| File format. Possible values are csv, jsonl, json and xlsx | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_classes_get**
> Classes projects_project_id_classes_get(project_id)

Get all project's classes

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
api_instance = swagger_client.ClassesApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project

try:
    # Get all project's classes
    api_response = api_instance.projects_project_id_classes_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassesApi->projects_project_id_classes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 

### Return type

[**Classes**](Classes.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_classes_post**
> ModelClass projects_project_id_classes_post(project_id, body)

Add a new class to a project

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
api_instance = swagger_client.ClassesApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project to get
body = swagger_client.ModelClass() # ModelClass | 

try:
    # Add a new class to a project
    api_response = api_instance.projects_project_id_classes_post(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassesApi->projects_project_id_classes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project to get | 
 **body** | [**ModelClass**](ModelClass.md)|  | 

### Return type

[**ModelClass**](ModelClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_classes_upload_post**
> Classes projects_project_id_classes_upload_post(project_id, file)

Upload a file containing classes definition.

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
api_instance = swagger_client.ClassesApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
file = '/path/to/file.txt' # file | file to upload

try:
    # Upload a file containing classes definition.
    api_response = api_instance.projects_project_id_classes_upload_post(project_id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassesApi->projects_project_id_classes_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **file** | **file**| file to upload | 

### Return type

[**Classes**](Classes.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_upload_classes_post**
> Classes projects_project_id_upload_classes_post(project_id, body)

Add multiple classes to a project

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
api_instance = swagger_client.ClassesApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project to get
body = swagger_client.Classes() # Classes | 

try:
    # Add multiple classes to a project
    api_response = api_instance.projects_project_id_upload_classes_post(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassesApi->projects_project_id_upload_classes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project to get | 
 **body** | [**Classes**](Classes.md)|  | 

### Return type

[**Classes**](Classes.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

