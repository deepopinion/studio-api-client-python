# swagger_client.LabelingApi

All URIs are relative to *https://api.deepopinion.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_annotations_annotation_id_delete**](LabelingApi.md#projects_project_id_annotations_annotation_id_delete) | **DELETE** /projects/{project_id}/annotations/{annotation_id} | Delete a labeling session.
[**projects_project_id_annotations_annotation_id_documents_document_id_get**](LabelingApi.md#projects_project_id_annotations_annotation_id_documents_document_id_get) | **GET** /projects/{project_id}/annotations/{annotation_id}/documents/{document_id} | Get a particular document of a labeling session.
[**projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_statuses_post**](LabelingApi.md#projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_statuses_post) | **POST** /projects/{project_id}/annotations/{annotation_id}/documents/{document_id}/segments/{segment_id}/statuses | Mark a segment as annotated.
[**projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_get**](LabelingApi.md#projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_get) | **GET** /projects/{project_id}/annotations/{annotation_id}/documents/{document_id}/segments/{segment_id}/tags | Return a list of tags of a segment.
[**projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_post**](LabelingApi.md#projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_post) | **POST** /projects/{project_id}/annotations/{annotation_id}/documents/{document_id}/segments/{segment_id}/tags | Add a tag to a segment.
[**projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_delete**](LabelingApi.md#projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_delete) | **DELETE** /projects/{project_id}/annotations/{annotation_id}/documents/{document_id}/segments/{segment_id}/tags/{tag_id} | Delete a tag.
[**projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_get**](LabelingApi.md#projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_get) | **GET** /projects/{project_id}/annotations/{annotation_id}/documents/{document_id}/segments/{segment_id}/tags/{tag_id} | Get a tag.
[**projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_put**](LabelingApi.md#projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_put) | **PUT** /projects/{project_id}/annotations/{annotation_id}/documents/{document_id}/segments/{segment_id}/tags/{tag_id} | Change a tag.
[**projects_project_id_annotations_annotation_id_documents_document_id_statuses_post**](LabelingApi.md#projects_project_id_annotations_annotation_id_documents_document_id_statuses_post) | **POST** /projects/{project_id}/annotations/{annotation_id}/documents/{document_id}/statuses | Mark a document as annotated.
[**projects_project_id_annotations_annotation_id_documents_get**](LabelingApi.md#projects_project_id_annotations_annotation_id_documents_get) | **GET** /projects/{project_id}/annotations/{annotation_id}/documents | Get all documents of a labeling session
[**projects_project_id_annotations_annotation_id_download_get**](LabelingApi.md#projects_project_id_annotations_annotation_id_download_get) | **GET** /projects/{project_id}/annotations/{annotation_id}/download | Download a labeling session
[**projects_project_id_annotations_annotation_id_get**](LabelingApi.md#projects_project_id_annotations_annotation_id_get) | **GET** /projects/{project_id}/annotations/{annotation_id} | Return a labeling session.
[**projects_project_id_annotations_annotation_id_put**](LabelingApi.md#projects_project_id_annotations_annotation_id_put) | **PUT** /projects/{project_id}/annotations/{annotation_id} | Change a labeling session.
[**projects_project_id_annotations_download_get**](LabelingApi.md#projects_project_id_annotations_download_get) | **GET** /projects/{project_id}/annotations/download | Download all labeling sessions of a project.
[**projects_project_id_annotations_get**](LabelingApi.md#projects_project_id_annotations_get) | **GET** /projects/{project_id}/annotations | Return a list of labeling sessions that belongs to a project.
[**projects_project_id_annotations_post**](LabelingApi.md#projects_project_id_annotations_post) | **POST** /projects/{project_id}/annotations | Create a new labeling session.
[**projects_project_id_annotations_upload_post**](LabelingApi.md#projects_project_id_annotations_upload_post) | **POST** /projects/{project_id}/annotations/upload | Upload a file for a new labeling session.


# **projects_project_id_annotations_annotation_id_delete**
> projects_project_id_annotations_annotation_id_delete(project_id, annotation_id)

Delete a labeling session.

<br/>This operation cannot be undone. The original document group will be preserved.<br/><br/> 

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
annotation_id = 56 # int | ID of the labeling session to be deleted

try:
    # Delete a labeling session.
    api_instance.projects_project_id_annotations_annotation_id_delete(project_id, annotation_id)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_annotation_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **annotation_id** | **int**| ID of the labeling session to be deleted | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_annotation_id_documents_document_id_get**
> LabelledDocument projects_project_id_annotations_annotation_id_documents_document_id_get(project_id, annotation_id, document_id, details=details)

Get a particular document of a labeling session.

<br/>Use URL params to control the result:<br/>- ?details=segments,meta,tags to show details of a document<br/> * segments: Show segments of a document<br/> * tags: Show tags of a document<br/> * meta: Show all the additional attributes that were originally given as the document was uploaded<br/><br/>

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
annotation_id = 56 # int | ID of the session
document_id = 56 # int | ID of the document
details = 'details_example' # str | Which documents' details API should return. Values might be any combination of 'segments', 'meta' and 'tags'. (optional)

try:
    # Get a particular document of a labeling session.
    api_response = api_instance.projects_project_id_annotations_annotation_id_documents_document_id_get(project_id, annotation_id, document_id, details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_annotation_id_documents_document_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **annotation_id** | **int**| ID of the session | 
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

# **projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_statuses_post**
> SegmentAnnotationStatus projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_statuses_post(project_id, annotation_id, document_id, segment_id, body)

Mark a segment as annotated.

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
annotation_id = 56 # int | ID of the labeling session
document_id = 56 # int | ID of the document
segment_id = 56 # int | ID of the segment
body = swagger_client.Body3() # Body3 | 

try:
    # Mark a segment as annotated.
    api_response = api_instance.projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_statuses_post(project_id, annotation_id, document_id, segment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_statuses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **annotation_id** | **int**| ID of the labeling session | 
 **document_id** | **int**| ID of the document | 
 **segment_id** | **int**| ID of the segment | 
 **body** | [**Body3**](Body3.md)|  | 

### Return type

[**SegmentAnnotationStatus**](SegmentAnnotationStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_get**
> ClassLabelTags projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_get(project_id, annotation_id, document_id, segment_id)

Return a list of tags of a segment.

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
annotation_id = 56 # int | ID of the labeling session
document_id = 56 # int | ID of the document
segment_id = 56 # int | ID of the segment

try:
    # Return a list of tags of a segment.
    api_response = api_instance.projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_get(project_id, annotation_id, document_id, segment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **annotation_id** | **int**| ID of the labeling session | 
 **document_id** | **int**| ID of the document | 
 **segment_id** | **int**| ID of the segment | 

### Return type

[**ClassLabelTags**](ClassLabelTags.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_post**
> ClassLabelTag projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_post(project_id, annotation_id, document_id, segment_id)

Add a tag to a segment.

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
annotation_id = 56 # int | ID of the labeling session
document_id = 56 # int | ID of the document
segment_id = 56 # int | ID of the segment

try:
    # Add a tag to a segment.
    api_response = api_instance.projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_post(project_id, annotation_id, document_id, segment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **annotation_id** | **int**| ID of the labeling session | 
 **document_id** | **int**| ID of the document | 
 **segment_id** | **int**| ID of the segment | 

### Return type

[**ClassLabelTag**](ClassLabelTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_delete**
> projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_delete(project_id, annotation_id, document_id, segment_id, tag_id)

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
annotation_id = 56 # int | ID of the labeling session
document_id = 56 # int | ID of the document
segment_id = 56 # int | ID of the segment
tag_id = 56 # int | ID of the tag

try:
    # Delete a tag.
    api_instance.projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_delete(project_id, annotation_id, document_id, segment_id, tag_id)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **annotation_id** | **int**| ID of the labeling session | 
 **document_id** | **int**| ID of the document | 
 **segment_id** | **int**| ID of the segment | 
 **tag_id** | **int**| ID of the tag | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_get**
> ClassLabelTag projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_get(project_id, annotation_id, document_id, segment_id, tag_id)

Get a tag.

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
annotation_id = 56 # int | ID of the labeling session
document_id = 56 # int | ID of the document
segment_id = 56 # int | ID of the segment
tag_id = 56 # int | ID of the tag

try:
    # Get a tag.
    api_response = api_instance.projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_get(project_id, annotation_id, document_id, segment_id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **annotation_id** | **int**| ID of the labeling session | 
 **document_id** | **int**| ID of the document | 
 **segment_id** | **int**| ID of the segment | 
 **tag_id** | **int**| ID of the tag | 

### Return type

[**ClassLabelTag**](ClassLabelTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_put**
> ClassLabelTag projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_put(body, project_id, annotation_id, document_id, segment_id, tag_id)

Change a tag.

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChangeAnnotationTag() # ChangeAnnotationTag | 
project_id = 56 # int | ID of the project
annotation_id = 56 # int | ID of the labeling session
document_id = 56 # int | ID of the document
segment_id = 56 # int | ID of the segment
tag_id = 56 # int | ID of the tag

try:
    # Change a tag.
    api_response = api_instance.projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_put(body, project_id, annotation_id, document_id, segment_id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_annotation_id_documents_document_id_segments_segment_id_tags_tag_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeAnnotationTag**](ChangeAnnotationTag.md)|  | 
 **project_id** | **int**| ID of the project | 
 **annotation_id** | **int**| ID of the labeling session | 
 **document_id** | **int**| ID of the document | 
 **segment_id** | **int**| ID of the segment | 
 **tag_id** | **int**| ID of the tag | 

### Return type

[**ClassLabelTag**](ClassLabelTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_annotation_id_documents_document_id_statuses_post**
> DocumentAnnotationStatus projects_project_id_annotations_annotation_id_documents_document_id_statuses_post(project_id, annotation_id, document_id, body)

Mark a document as annotated.

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
annotation_id = 56 # int | ID of the labeling session
document_id = 56 # int | ID of the document
body = swagger_client.Body4() # Body4 | 

try:
    # Mark a document as annotated.
    api_response = api_instance.projects_project_id_annotations_annotation_id_documents_document_id_statuses_post(project_id, annotation_id, document_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_annotation_id_documents_document_id_statuses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **annotation_id** | **int**| ID of the labeling session | 
 **document_id** | **int**| ID of the document | 
 **body** | [**Body4**](Body4.md)|  | 

### Return type

[**DocumentAnnotationStatus**](DocumentAnnotationStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_annotation_id_documents_get**
> LabelingSessionWithDocs projects_project_id_annotations_annotation_id_documents_get(project_id, annotation_id, details=details, offset=offset, limit=limit)

Get all documents of a labeling session

<br/>Use URL params to control or filter the result:<br/>- ?search=wordto only show documents that contain word<br/>- ?offset=0&limit=10 to have a paginated view<br/>- ?details=segments,meta,tags to show details of a document<br/> * segments: Show segments of a document<br/> * tags: Show tags of a document<br/> * meta: Show all the additional attributes that were originally given as the document was uploaded<br/><br/>

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
annotation_id = 56 # int | ID of the session
details = 'details_example' # str | Which details API should return. Values might be any combination of 'segments', 'meta' and 'tags'. (optional)
offset = 56 # int | An offset is simply the number of records you wish to skip before selecting records. (optional)
limit = 56 # int | Limit of entries that should be returned. (optional)

try:
    # Get all documents of a labeling session
    api_response = api_instance.projects_project_id_annotations_annotation_id_documents_get(project_id, annotation_id, details=details, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_annotation_id_documents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **annotation_id** | **int**| ID of the session | 
 **details** | **str**| Which details API should return. Values might be any combination of &#39;segments&#39;, &#39;meta&#39; and &#39;tags&#39;. | [optional] 
 **offset** | **int**| An offset is simply the number of records you wish to skip before selecting records. | [optional] 
 **limit** | **int**| Limit of entries that should be returned. | [optional] 

### Return type

[**LabelingSessionWithDocs**](LabelingSessionWithDocs.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_annotation_id_download_get**
> projects_project_id_annotations_annotation_id_download_get(project_id, annotation_id, format=format)

Download a labeling session

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
annotation_id = 56 # int | ID of the session
format = 'format_example' # str | File format. Possible values are csv, jsonl, json and xlsx (optional)

try:
    # Download a labeling session
    api_instance.projects_project_id_annotations_annotation_id_download_get(project_id, annotation_id, format=format)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_annotation_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **annotation_id** | **int**| ID of the session | 
 **format** | **str**| File format. Possible values are csv, jsonl, json and xlsx | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_annotation_id_get**
> LabelingSession projects_project_id_annotations_annotation_id_get(project_id, annotation_id)

Return a labeling session.

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
annotation_id = 56 # int | ID of the labeling session

try:
    # Return a labeling session.
    api_response = api_instance.projects_project_id_annotations_annotation_id_get(project_id, annotation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_annotation_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **annotation_id** | **int**| ID of the labeling session | 

### Return type

[**LabelingSession**](LabelingSession.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_annotation_id_put**
> LabelingSession projects_project_id_annotations_annotation_id_put(project_id, annotation_id, body)

Change a labeling session.

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
annotation_id = 56 # int | ID of the labeling session to changed
body = swagger_client.LabelingSessionChange() # LabelingSessionChange | 

try:
    # Change a labeling session.
    api_response = api_instance.projects_project_id_annotations_annotation_id_put(project_id, annotation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_annotation_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **annotation_id** | **int**| ID of the labeling session to changed | 
 **body** | [**LabelingSessionChange**](LabelingSessionChange.md)|  | 

### Return type

[**LabelingSession**](LabelingSession.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_download_get**
> projects_project_id_annotations_download_get(project_id, format=format)

Download all labeling sessions of a project.

<br/>The result will be combined into one single file.<br/>

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
format = 'format_example' # str | File format. Possible values are csv, jsonl, json and xlsx (optional)

try:
    # Download all labeling sessions of a project.
    api_instance.projects_project_id_annotations_download_get(project_id, format=format)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_download_get: %s\n" % e)
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

# **projects_project_id_annotations_get**
> LabelingSessions projects_project_id_annotations_get(project_id, mode=mode, status=status)

Return a list of labeling sessions that belongs to a project.

<br/>You can combine any of the parameters to filter the results.<br/>

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
mode = 'mode_example' # str | Labeling mode. Any combination of ANNOTATION or CORRECTION (optional)
status = 'status_example' # str | Labeling status. Any of CREATED, STARTED, ANNOTATING, FAILED, FINISHED, SAMPLING, PREDICTING or DELETING (optional)

try:
    # Return a list of labeling sessions that belongs to a project.
    api_response = api_instance.projects_project_id_annotations_get(project_id, mode=mode, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **mode** | **str**| Labeling mode. Any combination of ANNOTATION or CORRECTION | [optional] 
 **status** | **str**| Labeling status. Any of CREATED, STARTED, ANNOTATING, FAILED, FINISHED, SAMPLING, PREDICTING or DELETING | [optional] 

### Return type

[**LabelingSessions**](LabelingSessions.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_post**
> LabelingSession projects_project_id_annotations_post(project_id, body)

Create a new labeling session.

<br/>If neither documents nor document_ids are given, the whole documents of the system are used for this annotation.<br/>

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
body = swagger_client.LabelingSessionCreate() # LabelingSessionCreate | 

try:
    # Create a new labeling session.
    api_response = api_instance.projects_project_id_annotations_post(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**LabelingSessionCreate**](LabelingSessionCreate.md)|  | 

### Return type

[**LabelingSession**](LabelingSession.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_annotations_upload_post**
> LabelingSession projects_project_id_annotations_upload_post(project_id, file, show_preview=show_preview)

Upload a file for a new labeling session.

<br/>A file contains one or more documents that can be used to create a labeling session.<br/><br/>If show_preview is True, a preview will be shown and the endpoint to create<br/>a new labeling session must be called using the \"id\" and a column name<br/>obtained in the preview response.<br/>

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
api_instance = swagger_client.LabelingApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
file = '/path/to/file.txt' # file | file to upload
show_preview = true # bool | If true, a preview will be shown. (optional)

try:
    # Upload a file for a new labeling session.
    api_response = api_instance.projects_project_id_annotations_upload_post(project_id, file, show_preview=show_preview)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelingApi->projects_project_id_annotations_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **file** | **file**| file to upload | 
 **show_preview** | **bool**| If true, a preview will be shown. | [optional] 

### Return type

[**LabelingSession**](LabelingSession.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

