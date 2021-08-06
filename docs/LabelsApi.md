# swagger_client.LabelsApi

All URIs are relative to *https://api.deepopinion.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_labels_download_get**](LabelsApi.md#projects_project_id_labels_download_get) | **GET** /projects/{project_id}/labels/download | Download all project&#39;s labels
[**projects_project_id_labels_get**](LabelsApi.md#projects_project_id_labels_get) | **GET** /projects/{project_id}/labels | Get all project&#39;s labels
[**projects_project_id_labels_label_id_delete**](LabelsApi.md#projects_project_id_labels_label_id_delete) | **DELETE** /projects/{project_id}/labels/{label_id} | Delete a label. Labels from ABSA projects cannot be deleted.
[**projects_project_id_labels_label_id_get**](LabelsApi.md#projects_project_id_labels_label_id_get) | **GET** /projects/{project_id}/labels/{label_id} | Get a particular label
[**projects_project_id_labels_label_id_put**](LabelsApi.md#projects_project_id_labels_label_id_put) | **PUT** /projects/{project_id}/labels/{label_id} | Change label&#39;s data
[**projects_project_id_labels_post**](LabelsApi.md#projects_project_id_labels_post) | **POST** /projects/{project_id}/labels | Add a new label to a project.
[**projects_project_id_labels_upload_post**](LabelsApi.md#projects_project_id_labels_upload_post) | **POST** /projects/{project_id}/labels/upload | Upload a file containing labels definition.


# **projects_project_id_labels_download_get**
> projects_project_id_labels_download_get(project_id, format=format)

Download all project's labels

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
format = 'format_example' # str | File format. Possible values are csv, jsonl, json and xlsx (optional)

try:
    # Download all project's labels
    api_instance.projects_project_id_labels_download_get(project_id, format=format)
except ApiException as e:
    print("Exception when calling LabelsApi->projects_project_id_labels_download_get: %s\n" % e)
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

# **projects_project_id_labels_get**
> LabelsResponse projects_project_id_labels_get(project_id)

Get all project's labels

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project

try:
    # Get all project's labels
    api_response = api_instance.projects_project_id_labels_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->projects_project_id_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_labels_label_id_delete**
> projects_project_id_labels_label_id_delete(project_id, label_id)

Delete a label. Labels from ABSA projects cannot be deleted.

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project that contains the class
label_id = 56 # int | ID of the label to delete

try:
    # Delete a label. Labels from ABSA projects cannot be deleted.
    api_instance.projects_project_id_labels_label_id_delete(project_id, label_id)
except ApiException as e:
    print("Exception when calling LabelsApi->projects_project_id_labels_label_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project that contains the class | 
 **label_id** | **int**| ID of the label to delete | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_labels_label_id_get**
> Label projects_project_id_labels_label_id_get(project_id, label_id)

Get a particular label

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
label_id = 56 # int | ID of the label

try:
    # Get a particular label
    api_response = api_instance.projects_project_id_labels_label_id_get(project_id, label_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->projects_project_id_labels_label_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **label_id** | **int**| ID of the label | 

### Return type

[**Label**](Label.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_labels_label_id_put**
> Label projects_project_id_labels_label_id_put(project_id, label_id, body)

Change label's data

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project to change
label_id = 56 # int | ID of the label to change
body = swagger_client.LabelInput() # LabelInput | 

try:
    # Change label's data
    api_response = api_instance.projects_project_id_labels_label_id_put(project_id, label_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->projects_project_id_labels_label_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project to change | 
 **label_id** | **int**| ID of the label to change | 
 **body** | [**LabelInput**](LabelInput.md)|  | 

### Return type

[**Label**](Label.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_labels_post**
> Label projects_project_id_labels_post(project_id, body)

Add a new label to a project.

<br/>You cannot add labels to an ABSA project<br/>

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project to get
body = swagger_client.LabelInput() # LabelInput | 

try:
    # Add a new label to a project.
    api_response = api_instance.projects_project_id_labels_post(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->projects_project_id_labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project to get | 
 **body** | [**LabelInput**](LabelInput.md)|  | 

### Return type

[**Label**](Label.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_labels_upload_post**
> LabelsResponse projects_project_id_labels_upload_post(project_id, file)

Upload a file containing labels definition.

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
file = '/path/to/file.txt' # file | file to upload

try:
    # Upload a file containing labels definition.
    api_response = api_instance.projects_project_id_labels_upload_post(project_id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->projects_project_id_labels_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **file** | **file**| file to upload | 

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

