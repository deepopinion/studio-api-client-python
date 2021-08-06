# swagger_client.ProjectsApi

All URIs are relative to *https://api.deepopinion.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_get**](ProjectsApi.md#projects_get) | **GET** /projects | List all projects that the authorized user has access to.
[**projects_post**](ProjectsApi.md#projects_post) | **POST** /projects | Create a new project.
[**projects_project_id_analyses_get**](ProjectsApi.md#projects_project_id_analyses_get) | **GET** /projects/{project_id}/analyses | Get all projects&#39; analyses.
[**projects_project_id_clone_post**](ProjectsApi.md#projects_project_id_clone_post) | **POST** /projects/{project_id}/clone | Clone a project.
[**projects_project_id_delete**](ProjectsApi.md#projects_project_id_delete) | **DELETE** /projects/{project_id} | Delete a project.
[**projects_project_id_get**](ProjectsApi.md#projects_project_id_get) | **GET** /projects/{project_id} | Get a project
[**projects_project_id_permissions_get**](ProjectsApi.md#projects_project_id_permissions_get) | **GET** /projects/{project_id}/permissions | Get all projects&#39; permission.
[**projects_project_id_put**](ProjectsApi.md#projects_project_id_put) | **PUT** /projects/{project_id} | Change project data.
[**projects_project_id_tags_get**](ProjectsApi.md#projects_project_id_tags_get) | **GET** /projects/{project_id}/tags | Get all tags of a project
[**projects_project_id_tags_tag_id_delete**](ProjectsApi.md#projects_project_id_tags_tag_id_delete) | **DELETE** /projects/{project_id}/tags/{tag_id} | Delete a tag.
[**projects_project_id_tags_tag_id_put**](ProjectsApi.md#projects_project_id_tags_tag_id_put) | **PUT** /projects/{project_id}/tags/{tag_id} | Edit a tag
[**projects_project_id_transfer_post**](ProjectsApi.md#projects_project_id_transfer_post) | **POST** /projects/{project_id}/transfer | Transfer a project to a workspace.


# **projects_get**
> Projects projects_get()

List all projects that the authorized user has access to.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))

try:
    # List all projects that the authorized user has access to.
    api_response = api_instance.projects_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Projects**](Projects.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_post**
> Project projects_post(body)

Create a new project.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body1() # Body1 | 

try:
    # Create a new project.
    api_response = api_instance.projects_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_analyses_get**
> Analyses projects_project_id_analyses_get(project_id, offset=offset, limit=limit, details=details)

Get all projects' analyses.

<br/>Use URL params to control or filter the result.<br/><br/>The pagination should be done by increasing the offset by the value of limit until the property has_more is false<br/> 

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
offset = 56 # int | An offset is simply the number of records you wish to skip before selecting records. (optional)
limit = 56 # int | Limit of entries that should be returned. (optional)
details = 'details_example' # str | Which documents' details API should return. Values might be any combination of 'segments', 'meta' and 'tags'. (optional)

try:
    # Get all projects' analyses.
    api_response = api_instance.projects_project_id_analyses_get(project_id, offset=offset, limit=limit, details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_project_id_analyses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **offset** | **int**| An offset is simply the number of records you wish to skip before selecting records. | [optional] 
 **limit** | **int**| Limit of entries that should be returned. | [optional] 
 **details** | **str**| Which documents&#39; details API should return. Values might be any combination of &#39;segments&#39;, &#39;meta&#39; and &#39;tags&#39;. | [optional] 

### Return type

[**Analyses**](Analyses.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_clone_post**
> Project projects_project_id_clone_post(project_id, body)

Clone a project.

<br/>Cloning a project will clone all data associated to this project.<br/>

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project to change
body = swagger_client.Body5() # Body5 | 

try:
    # Clone a project.
    api_response = api_instance.projects_project_id_clone_post(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_project_id_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project to change | 
 **body** | [**Body5**](Body5.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_delete**
> projects_project_id_delete(project_id)

Delete a project.

<br/>By deleting a project, all data that is managed by the project (document, models) will be deleted as well and cannot be restored.<br/><br/> 

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project to change

try:
    # Delete a project.
    api_instance.projects_project_id_delete(project_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_project_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project to change | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_get**
> Project projects_project_id_get(project_id)

Get a project

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project to get

try:
    # Get a project
    api_response = api_instance.projects_project_id_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_project_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project to get | 

### Return type

[**Project**](Project.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_permissions_get**
> ProjectPermissions projects_project_id_permissions_get(project_id)

Get all projects' permission.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project

try:
    # Get all projects' permission.
    api_response = api_instance.projects_project_id_permissions_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_project_id_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 

### Return type

[**ProjectPermissions**](ProjectPermissions.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_put**
> Project projects_project_id_put(project_id, body)

Change project data.

<br/>Any project attribute can be given that should be updated.<br/>

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project to change
body = swagger_client.Body2() # Body2 | 

try:
    # Change project data.
    api_response = api_instance.projects_project_id_put(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_project_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project to change | 
 **body** | [**Body2**](Body2.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_tags_get**
> ProjectTagsResponse projects_project_id_tags_get(project_id, classes=classes, labels=labels, offset=offset, limit=limit)

Get all tags of a project

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
classes = true # bool | if true, the whole class object will be returned instead of just strings (optional)
labels = true # bool | if true, the whole label object will be returned instead of just strings (optional)
offset = 56 # int | An offset is simply the number of records you wish to skip before selecting records. (optional)
limit = 56 # int | Limit of entries that should be returned. (optional)

try:
    # Get all tags of a project
    api_response = api_instance.projects_project_id_tags_get(project_id, classes=classes, labels=labels, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_project_id_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **classes** | **bool**| if true, the whole class object will be returned instead of just strings | [optional] 
 **labels** | **bool**| if true, the whole label object will be returned instead of just strings | [optional] 
 **offset** | **int**| An offset is simply the number of records you wish to skip before selecting records. | [optional] 
 **limit** | **int**| Limit of entries that should be returned. | [optional] 

### Return type

[**ProjectTagsResponse**](ProjectTagsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_tags_tag_id_delete**
> projects_project_id_tags_tag_id_delete(project_id, tag_id)

Delete a tag.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
tag_id = 56 # int | ID of the tag

try:
    # Delete a tag.
    api_instance.projects_project_id_tags_tag_id_delete(project_id, tag_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_project_id_tags_tag_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **tag_id** | **int**| ID of the tag | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_tags_tag_id_put**
> ClassLabelTags projects_project_id_tags_tag_id_put(project_id, tag_id, body)

Edit a tag

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
tag_id = 56 # int | ID of the tag
body = swagger_client.ChangeAnnotationTag() # ChangeAnnotationTag | 

try:
    # Edit a tag
    api_response = api_instance.projects_project_id_tags_tag_id_put(project_id, tag_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_project_id_tags_tag_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **tag_id** | **int**| ID of the tag | 
 **body** | [**ChangeAnnotationTag**](ChangeAnnotationTag.md)|  | 

### Return type

[**ClassLabelTags**](ClassLabelTags.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_transfer_post**
> projects_project_id_transfer_post(project_id, body)

Transfer a project to a workspace.

<br/>Transferring a project will transfer all data associated to this project.<br/>

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project to change
body = swagger_client.Body7() # Body7 | 

try:
    # Transfer a project to a workspace.
    api_instance.projects_project_id_transfer_post(project_id, body)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_project_id_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project to change | 
 **body** | [**Body7**](Body7.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

