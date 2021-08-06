# swagger_client.DocumentsApi

All URIs are relative to *https://api.deepopinion.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_documents_document_id_delete**](DocumentsApi.md#projects_project_id_documents_document_id_delete) | **DELETE** /projects/{project_id}/documents/{document_id} | Delete a document of a project.
[**projects_project_id_documents_document_id_get**](DocumentsApi.md#projects_project_id_documents_document_id_get) | **GET** /projects/{project_id}/documents/{document_id} | Get a particular document of a project.
[**projects_project_id_documents_document_id_put**](DocumentsApi.md#projects_project_id_documents_document_id_put) | **PUT** /projects/{project_id}/documents/{document_id} | Change a document.
[**projects_project_id_documents_get**](DocumentsApi.md#projects_project_id_documents_get) | **GET** /projects/{project_id}/documents | Fetches all documents of a given project
[**projects_project_id_documents_post**](DocumentsApi.md#projects_project_id_documents_post) | **POST** /projects/{project_id}/documents | Create a new document.
[**projects_project_id_upload_documents_post**](DocumentsApi.md#projects_project_id_upload_documents_post) | **POST** /projects/{project_id}/upload-documents | Upload new documents.


# **projects_project_id_documents_document_id_delete**
> projects_project_id_documents_document_id_delete(project_id, document_id)

Delete a document of a project.

<br/>Use URL params to control the result:<br/>- ?details=segments<br/> * segments: Show segments of a document<br/><br/>

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
document_id = 56 # int | ID of the document

try:
    # Delete a document of a project.
    api_instance.projects_project_id_documents_document_id_delete(project_id, document_id)
except ApiException as e:
    print("Exception when calling DocumentsApi->projects_project_id_documents_document_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **document_id** | **int**| ID of the document | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_documents_document_id_get**
> DocumentsSegments projects_project_id_documents_document_id_get(project_id, document_id, details=details)

Get a particular document of a project.

<br/>Use URL params to control the result:<br/>- ?details=segments<br/> * segments: Show segments of a document<br/><br/>

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
document_id = 56 # int | ID of the document
details = 'details_example' # str | Which documents' details API should return. Only \"segments\" is supported. (optional)

try:
    # Get a particular document of a project.
    api_response = api_instance.projects_project_id_documents_document_id_get(project_id, document_id, details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->projects_project_id_documents_document_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **document_id** | **int**| ID of the document | 
 **details** | **str**| Which documents&#39; details API should return. Only \&quot;segments\&quot; is supported. | [optional] 

### Return type

[**DocumentsSegments**](DocumentsSegments.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_documents_document_id_put**
> Document projects_project_id_documents_document_id_put(project_id, document_id, body)

Change a document.

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
document_id = 56 # int | ID of the document group
body = swagger_client.DocumentChangeInput() # DocumentChangeInput | 

try:
    # Change a document.
    api_response = api_instance.projects_project_id_documents_document_id_put(project_id, document_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->projects_project_id_documents_document_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **document_id** | **int**| ID of the document group | 
 **body** | [**DocumentChangeInput**](DocumentChangeInput.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_documents_get**
> DocumentsSegmentsResponse projects_project_id_documents_get(project_id, details=details, search=search, annotation_id=annotation_id, analysis_id=analysis_id, group_id=group_id, grouped=grouped, analysed=analysed, offset=offset, limit=limit)

Fetches all documents of a given project

<br/>Use URL params to control or filter the result:<br/>- ?search=wordto only show documents that contain word<br/>- ?offset=0&limit=10 to have a paginated view<br/>- ?classes=1,746 to filter by these class ids<br/>- ?labels=110,111,112 to filter by these class ids<br/>- ?details=segments,meta,tags to show details of a document<br/>     * segments: Show segments of a document<br/>     * tags: Show tags of a document<br/>     * meta: Show all the additional attributes that were originally given as the document was uploaded<br/>

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project to get
details = 'details_example' # str | Which details API should return. Values might be any combination of 'segments', 'meta', 'tags' and 'stats'. (optional)
search = 'search_example' # str | Search by name (optional)
annotation_id = 56 # int | Filter by annotation ID (optional)
analysis_id = 56 # int | Filter by analysis ID (optional)
group_id = 56 # int | Filter by group ID (optional)
grouped = true # bool | If true, return only documents that belong to a group (optional)
analysed = true # bool | If true, return only documents that belong to an analysis (optional)
offset = 56 # int | An offset is simply the number of records you wish to skip before selecting records. (optional)
limit = 56 # int | Limit of entries that should be returned. (optional)

try:
    # Fetches all documents of a given project
    api_response = api_instance.projects_project_id_documents_get(project_id, details=details, search=search, annotation_id=annotation_id, analysis_id=analysis_id, group_id=group_id, grouped=grouped, analysed=analysed, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->projects_project_id_documents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project to get | 
 **details** | **str**| Which details API should return. Values might be any combination of &#39;segments&#39;, &#39;meta&#39;, &#39;tags&#39; and &#39;stats&#39;. | [optional] 
 **search** | **str**| Search by name | [optional] 
 **annotation_id** | **int**| Filter by annotation ID | [optional] 
 **analysis_id** | **int**| Filter by analysis ID | [optional] 
 **group_id** | **int**| Filter by group ID | [optional] 
 **grouped** | **bool**| If true, return only documents that belong to a group | [optional] 
 **analysed** | **bool**| If true, return only documents that belong to an analysis | [optional] 
 **offset** | **int**| An offset is simply the number of records you wish to skip before selecting records. | [optional] 
 **limit** | **int**| Limit of entries that should be returned. | [optional] 

### Return type

[**DocumentsSegmentsResponse**](DocumentsSegmentsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_documents_post**
> Document projects_project_id_documents_post(project_id, body)

Create a new document.

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
body = swagger_client.DocumentCreate() # DocumentCreate | 

try:
    # Create a new document.
    api_response = api_instance.projects_project_id_documents_post(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->projects_project_id_documents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**DocumentCreate**](DocumentCreate.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_upload_documents_post**
> projects_project_id_upload_documents_post(project_id, body)

Upload new documents.

<br/>Implemented as asynchronous request and returns 202 ACCEPTED.<br/><br/>Documents will be uploaded, segmented and analyzed.<br/><br/>If any annotations are given, these will also be analyzed and added to the database.<br/>

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
body = swagger_client.UploadDocuments() # UploadDocuments | 

try:
    # Upload new documents.
    api_instance.projects_project_id_upload_documents_post(project_id, body)
except ApiException as e:
    print("Exception when calling DocumentsApi->projects_project_id_upload_documents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**UploadDocuments**](UploadDocuments.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

