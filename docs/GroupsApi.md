# swagger_client.GroupsApi

All URIs are relative to *https://api.deepopinion.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_groups_get**](GroupsApi.md#projects_project_id_groups_get) | **GET** /projects/{project_id}/groups | List all document groups that belongs to a project
[**projects_project_id_groups_group_id_delete**](GroupsApi.md#projects_project_id_groups_group_id_delete) | **DELETE** /projects/{project_id}/groups/{group_id} | Delete a group of documents.
[**projects_project_id_groups_group_id_documents_document_id_get**](GroupsApi.md#projects_project_id_groups_group_id_documents_document_id_get) | **GET** /projects/{project_id}/groups/{group_id}/documents/{document_id} | Get a particular document of a group.
[**projects_project_id_groups_group_id_documents_get**](GroupsApi.md#projects_project_id_groups_group_id_documents_get) | **GET** /projects/{project_id}/groups/{group_id}/documents | Get documents of a group
[**projects_project_id_groups_group_id_download_get**](GroupsApi.md#projects_project_id_groups_group_id_download_get) | **GET** /projects/{project_id}/groups/{group_id}/download | Download all the documents of a group
[**projects_project_id_groups_group_id_get**](GroupsApi.md#projects_project_id_groups_group_id_get) | **GET** /projects/{project_id}/groups/{group_id} | Get a Document Group
[**projects_project_id_groups_group_id_put**](GroupsApi.md#projects_project_id_groups_group_id_put) | **PUT** /projects/{project_id}/groups/{group_id} | Change a document group.
[**projects_project_id_groups_post**](GroupsApi.md#projects_project_id_groups_post) | **POST** /projects/{project_id}/groups | Create a new document group.
[**projects_project_id_groups_upload_post**](GroupsApi.md#projects_project_id_groups_upload_post) | **POST** /projects/{project_id}/groups/upload | Upload a file to a project. A file contains one or more documents that can


# **projects_project_id_groups_get**
> DocumentGroups projects_project_id_groups_get(project_id)

List all document groups that belongs to a project

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project to get

try:
    # List all document groups that belongs to a project
    api_response = api_instance.projects_project_id_groups_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->projects_project_id_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project to get | 

### Return type

[**DocumentGroups**](DocumentGroups.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_groups_group_id_delete**
> projects_project_id_groups_group_id_delete(project_id, group_id)

Delete a group of documents.

<br/>By deleting a group, all analyses or annotations created from that group will be deleted.<br/><br/> 

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project that contains the group
group_id = 56 # int | ID of the group to delete

try:
    # Delete a group of documents.
    api_instance.projects_project_id_groups_group_id_delete(project_id, group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->projects_project_id_groups_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project that contains the group | 
 **group_id** | **int**| ID of the group to delete | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_groups_group_id_documents_document_id_get**
> LabelledDocument projects_project_id_groups_group_id_documents_document_id_get(project_id, group_id, document_id, details=details)

Get a particular document of a group.

<br/>Use URL params to control or filter the result:<br/>- ?details=segments,meta,tags to show details of a document<br/>     * segments: Show segments of a document<br/>     * tags: Show tags of a document<br/>     * meta: Show all the additional attributes that were originally given as the document was uploaded<br/>

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
group_id = 56 # int | ID of the document group
document_id = 56 # int | ID of the document
details = 'details_example' # str | Which documents' details API should return. Values might be any combination of 'segments', 'meta' and 'tags'. (optional)

try:
    # Get a particular document of a group.
    api_response = api_instance.projects_project_id_groups_group_id_documents_document_id_get(project_id, group_id, document_id, details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->projects_project_id_groups_group_id_documents_document_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **group_id** | **int**| ID of the document group | 
 **document_id** | **int**| ID of the document | 
 **details** | **str**| Which documents&#39; details API should return. Values might be any combination of &#39;segments&#39;, &#39;meta&#39; and &#39;tags&#39;. | [optional] 

### Return type

[**LabelledDocument**](LabelledDocument.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_groups_group_id_documents_get**
> LabelledDocuments projects_project_id_groups_group_id_documents_get(project_id, group_id, search=search, details=details, offset=offset, limit=limit)

Get documents of a group

<br/>Fetches all documents of a given group<br/><br/>Use URL params to control or filter the result:<br/>- ?search=wordto only show documents that contain word<br/>- ?offset=0&limit=10 to have a paginated view<br/>- ?details=segments,meta,tags to show details of a document<br/>     * segments: Show segments of a document<br/>     * tags: Show tags of a document<br/>     * meta: Show all the additional attributes that were originally given as the document was uploaded<br/>

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
group_id = 56 # int | ID of the document group
search = 'search_example' # str | Search by name (optional)
details = 'details_example' # str | Which documents' details API should return. Values might be any combination of 'segments', 'meta' and 'tags'. (optional)
offset = 56 # int | An offset is simply the number of records you wish to skip before selecting records. (optional)
limit = 56 # int | Limit of entries that should be returned. (optional)

try:
    # Get documents of a group
    api_response = api_instance.projects_project_id_groups_group_id_documents_get(project_id, group_id, search=search, details=details, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->projects_project_id_groups_group_id_documents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **group_id** | **int**| ID of the document group | 
 **search** | **str**| Search by name | [optional] 
 **details** | **str**| Which documents&#39; details API should return. Values might be any combination of &#39;segments&#39;, &#39;meta&#39; and &#39;tags&#39;. | [optional] 
 **offset** | **int**| An offset is simply the number of records you wish to skip before selecting records. | [optional] 
 **limit** | **int**| Limit of entries that should be returned. | [optional] 

### Return type

[**LabelledDocuments**](LabelledDocuments.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_groups_group_id_download_get**
> projects_project_id_groups_group_id_download_get(project_id, group_id, format=format)

Download all the documents of a group

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
group_id = 56 # int | ID of the document group
format = 'format_example' # str | File format. Possible values are csv, jsonl, json and xlsx (optional)

try:
    # Download all the documents of a group
    api_instance.projects_project_id_groups_group_id_download_get(project_id, group_id, format=format)
except ApiException as e:
    print("Exception when calling GroupsApi->projects_project_id_groups_group_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **group_id** | **int**| ID of the document group | 
 **format** | **str**| File format. Possible values are csv, jsonl, json and xlsx | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_groups_group_id_get**
> DocumentGroup projects_project_id_groups_group_id_get(project_id, group_id)

Get a Document Group

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project that contains the group
group_id = 56 # int | ID of the group to get

try:
    # Get a Document Group
    api_response = api_instance.projects_project_id_groups_group_id_get(project_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->projects_project_id_groups_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project that contains the group | 
 **group_id** | **int**| ID of the group to get | 

### Return type

[**DocumentGroup**](DocumentGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_groups_group_id_put**
> LabelingSession projects_project_id_groups_group_id_put(project_id, group_id, body)

Change a document group.

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
group_id = 56 # int | ID of the document group
body = swagger_client.DocumentGroupChange() # DocumentGroupChange | 

try:
    # Change a document group.
    api_response = api_instance.projects_project_id_groups_group_id_put(project_id, group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->projects_project_id_groups_group_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **group_id** | **int**| ID of the document group | 
 **body** | [**DocumentGroupChange**](DocumentGroupChange.md)|  | 

### Return type

[**LabelingSession**](LabelingSession.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_groups_post**
> DocumentGroup projects_project_id_groups_post(project_id, body)

Create a new document group.

<br/>A document group is, as the name suggests, a group of documents. There are two ways of creating a group:<br/>- By calling the Create group endpoint with all the documents you want to add to the group<br/>- In two steps: first one, upload a file in CSV, TXT, JSON, JSONL or XLSX format using the Upload a File endpoint. Then, use the file_id received and the column you want<br/>

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project to get
body = swagger_client.GroupCreate() # GroupCreate | 

try:
    # Create a new document group.
    api_response = api_instance.projects_project_id_groups_post(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->projects_project_id_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project to get | 
 **body** | [**GroupCreate**](GroupCreate.md)|  | 

### Return type

[**DocumentGroup**](DocumentGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_groups_upload_post**
> FilePreview projects_project_id_groups_upload_post(project_id, file, to_list=to_list)

Upload a file to a project. A file contains one or more documents that can

be used to create a document group<br/>

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
file = '/path/to/file.txt' # file | file to upload
to_list = true # bool | DEPRECATED: If set to false, the file preview will be in JSON format instead of a list. The default behavior will soon be changed to return a JSON and this parameter won't be needed anymore (optional)

try:
    # Upload a file to a project. A file contains one or more documents that can
    api_response = api_instance.projects_project_id_groups_upload_post(project_id, file, to_list=to_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->projects_project_id_groups_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **file** | **file**| file to upload | 
 **to_list** | **bool**| DEPRECATED: If set to false, the file preview will be in JSON format instead of a list. The default behavior will soon be changed to return a JSON and this parameter won&#39;t be needed anymore | [optional] 

### Return type

[**FilePreview**](FilePreview.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

