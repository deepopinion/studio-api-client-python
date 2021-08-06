# swagger_client.CorrectionApi

All URIs are relative to *https://api.deepopinion.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_corrections_correction_id_delete**](CorrectionApi.md#projects_project_id_corrections_correction_id_delete) | **DELETE** /projects/{project_id}/corrections/{correction_id} | Delete a correction session.
[**projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_statuses_post**](CorrectionApi.md#projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_statuses_post) | **POST** /projects/{project_id}/corrections/{correction_id}/documents/{document_id}/segments/{segment_id}/statuses | Mark a segment as corrected.
[**projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_post**](CorrectionApi.md#projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_post) | **POST** /projects/{project_id}/corrections/{correction_id}/documents/{document_id}/segments/{segment_id}/tags | Add a tag to a segment.
[**projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_delete**](CorrectionApi.md#projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_delete) | **DELETE** /projects/{project_id}/corrections/{correction_id}/documents/{document_id}/segments/{segment_id}/tags/{tag_id} | Delete a tag.
[**projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_put**](CorrectionApi.md#projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_put) | **PUT** /projects/{project_id}/corrections/{correction_id}/documents/{document_id}/segments/{segment_id}/tags/{tag_id} | Change a tag.
[**projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_statuses_post**](CorrectionApi.md#projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_statuses_post) | **POST** /projects/{project_id}/corrections/{correction_id}/documents/{document_id}/segments/{segment_id}/tags/{tag_id}/statuses | Confirm a tag.
[**projects_project_id_corrections_correction_id_documents_get**](CorrectionApi.md#projects_project_id_corrections_correction_id_documents_get) | **GET** /projects/{project_id}/corrections/{correction_id}/documents | Get correction session&#39;s documents.
[**projects_project_id_corrections_correction_id_get**](CorrectionApi.md#projects_project_id_corrections_correction_id_get) | **GET** /projects/{project_id}/corrections/{correction_id} | Return a correction session.
[**projects_project_id_corrections_get**](CorrectionApi.md#projects_project_id_corrections_get) | **GET** /projects/{project_id}/corrections | Return a list of correction sessions that belongs to a project.
[**projects_project_id_corrections_post**](CorrectionApi.md#projects_project_id_corrections_post) | **POST** /projects/{project_id}/corrections | Create a new correction session.


# **projects_project_id_corrections_correction_id_delete**
> projects_project_id_corrections_correction_id_delete(project_id, correction_id)

Delete a correction session.

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
api_instance = swagger_client.CorrectionApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
correction_id = 56 # int | ID of the correction session to be deleted

try:
    # Delete a correction session.
    api_instance.projects_project_id_corrections_correction_id_delete(project_id, correction_id)
except ApiException as e:
    print("Exception when calling CorrectionApi->projects_project_id_corrections_correction_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **correction_id** | **int**| ID of the correction session to be deleted | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_statuses_post**
> AnnotateCorrectionResponse projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_statuses_post(project_id, correction_id, document_id, segment_id, body)

Mark a segment as corrected.

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
api_instance = swagger_client.CorrectionApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
correction_id = 56 # int | ID of the correction session
document_id = 56 # int | ID of the document
segment_id = 56 # int | ID of the segment
body = swagger_client.Body6() # Body6 | 

try:
    # Mark a segment as corrected.
    api_response = api_instance.projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_statuses_post(project_id, correction_id, document_id, segment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrectionApi->projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_statuses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **correction_id** | **int**| ID of the correction session | 
 **document_id** | **int**| ID of the document | 
 **segment_id** | **int**| ID of the segment | 
 **body** | [**Body6**](Body6.md)|  | 

### Return type

[**AnnotateCorrectionResponse**](AnnotateCorrectionResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_post**
> CreateCorrectionTagResponse projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_post(project_id, correction_id, document_id, segment_id)

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
api_instance = swagger_client.CorrectionApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
correction_id = 56 # int | ID of the correction session
document_id = 56 # int | ID of the document
segment_id = 56 # int | ID of the segment

try:
    # Add a tag to a segment.
    api_response = api_instance.projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_post(project_id, correction_id, document_id, segment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrectionApi->projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **correction_id** | **int**| ID of the correction session | 
 **document_id** | **int**| ID of the document | 
 **segment_id** | **int**| ID of the segment | 

### Return type

[**CreateCorrectionTagResponse**](CreateCorrectionTagResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_delete**
> AnnotateCorrectionResponse projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_delete(project_id, correction_id, document_id, segment_id, tag_id)

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
api_instance = swagger_client.CorrectionApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
correction_id = 56 # int | ID of the correction session
document_id = 56 # int | ID of the document
segment_id = 56 # int | ID of the segment
tag_id = 56 # int | ID of the tag

try:
    # Delete a tag.
    api_response = api_instance.projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_delete(project_id, correction_id, document_id, segment_id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrectionApi->projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **correction_id** | **int**| ID of the correction session | 
 **document_id** | **int**| ID of the document | 
 **segment_id** | **int**| ID of the segment | 
 **tag_id** | **int**| ID of the tag | 

### Return type

[**AnnotateCorrectionResponse**](AnnotateCorrectionResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_put**
> CreateCorrectionTagResponse projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_put(body, project_id, correction_id, document_id, segment_id, tag_id)

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
api_instance = swagger_client.CorrectionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChangeAnnotationTag() # ChangeAnnotationTag | 
project_id = 56 # int | ID of the project
correction_id = 56 # int | ID of the correction session
document_id = 56 # int | ID of the document
segment_id = 56 # int | ID of the segment
tag_id = 56 # int | ID of the tag

try:
    # Change a tag.
    api_response = api_instance.projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_put(body, project_id, correction_id, document_id, segment_id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrectionApi->projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeAnnotationTag**](ChangeAnnotationTag.md)|  | 
 **project_id** | **int**| ID of the project | 
 **correction_id** | **int**| ID of the correction session | 
 **document_id** | **int**| ID of the document | 
 **segment_id** | **int**| ID of the segment | 
 **tag_id** | **int**| ID of the tag | 

### Return type

[**CreateCorrectionTagResponse**](CreateCorrectionTagResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_statuses_post**
> CreateCorrectionTagResponse projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_statuses_post(project_id, correction_id, document_id, segment_id, tag_id, body)

Confirm a tag.

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
api_instance = swagger_client.CorrectionApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
correction_id = 56 # int | ID of the correction session
document_id = 56 # int | ID of the document
segment_id = 56 # int | ID of the segment
tag_id = 56 # int | ID of the tag
body = swagger_client.ConfirmCorrectionTag() # ConfirmCorrectionTag | 

try:
    # Confirm a tag.
    api_response = api_instance.projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_statuses_post(project_id, correction_id, document_id, segment_id, tag_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrectionApi->projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_statuses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **correction_id** | **int**| ID of the correction session | 
 **document_id** | **int**| ID of the document | 
 **segment_id** | **int**| ID of the segment | 
 **tag_id** | **int**| ID of the tag | 
 **body** | [**ConfirmCorrectionTag**](ConfirmCorrectionTag.md)|  | 

### Return type

[**CreateCorrectionTagResponse**](CreateCorrectionTagResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_corrections_correction_id_documents_get**
> LabelingSessionWithDocs projects_project_id_corrections_correction_id_documents_get(project_id, correction_id, details=details, offset=offset, limit=limit)

Get correction session's documents.

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
api_instance = swagger_client.CorrectionApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
correction_id = 56 # int | ID of the session
details = 'details_example' # str | Which details API should return. Values might be any combination of 'segments', 'meta' and 'tags'. (optional)
offset = 56 # int | An offset is simply the number of records you wish to skip before selecting records. (optional)
limit = 56 # int | Limit of entries that should be returned. (optional)

try:
    # Get correction session's documents.
    api_response = api_instance.projects_project_id_corrections_correction_id_documents_get(project_id, correction_id, details=details, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrectionApi->projects_project_id_corrections_correction_id_documents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **correction_id** | **int**| ID of the session | 
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

# **projects_project_id_corrections_correction_id_get**
> Correction projects_project_id_corrections_correction_id_get(project_id, correction_id)

Return a correction session.

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
api_instance = swagger_client.CorrectionApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
correction_id = 56 # int | ID of the correction session

try:
    # Return a correction session.
    api_response = api_instance.projects_project_id_corrections_correction_id_get(project_id, correction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrectionApi->projects_project_id_corrections_correction_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **correction_id** | **int**| ID of the correction session | 

### Return type

[**Correction**](Correction.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_corrections_get**
> Corrections projects_project_id_corrections_get(project_id, status=status)

Return a list of correction sessions that belongs to a project.

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
api_instance = swagger_client.CorrectionApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
status = 'status_example' # str | Correction status. Any of CREATED, STARTED, ANNOTATING, FAILED, FINISHED, SAMPLING, PREDICTING or DELETING (optional)

try:
    # Return a list of correction sessions that belongs to a project.
    api_response = api_instance.projects_project_id_corrections_get(project_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrectionApi->projects_project_id_corrections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **status** | **str**| Correction status. Any of CREATED, STARTED, ANNOTATING, FAILED, FINISHED, SAMPLING, PREDICTING or DELETING | [optional] 

### Return type

[**Corrections**](Corrections.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_corrections_post**
> Correction projects_project_id_corrections_post(project_id, body)

Create a new correction session.

<br/>If no documents are given, they will be randomly chosen.<br/>

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
api_instance = swagger_client.CorrectionApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
body = swagger_client.CorrectionCreate() # CorrectionCreate | 

try:
    # Create a new correction session.
    api_response = api_instance.projects_project_id_corrections_post(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorrectionApi->projects_project_id_corrections_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**CorrectionCreate**](CorrectionCreate.md)|  | 

### Return type

[**Correction**](Correction.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

