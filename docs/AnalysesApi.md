# swagger_client.AnalysesApi

All URIs are relative to *https://api.deepopinion.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyses_analysis_id_delete**](AnalysesApi.md#analyses_analysis_id_delete) | **DELETE** /analyses/{analysis_id} | Delete an analyses.
[**analyses_analysis_id_documents_download_get**](AnalysesApi.md#analyses_analysis_id_documents_download_get) | **GET** /analyses/{analysis_id}/documents/download | Download analysis&#39;s documents.
[**analyses_analysis_id_documents_get**](AnalysesApi.md#analyses_analysis_id_documents_get) | **GET** /analyses/{analysis_id}/documents | Fetches all documents of a given analysis
[**analyses_analysis_id_get**](AnalysesApi.md#analyses_analysis_id_get) | **GET** /analyses/{analysis_id} | Get an Analysis
[**analyses_analysis_id_put**](AnalysesApi.md#analyses_analysis_id_put) | **PUT** /analyses/{analysis_id} | Change analysis&#39;s name
[**analyses_get**](AnalysesApi.md#analyses_get) | **GET** /analyses | Return a list of analyses.
[**analyses_post**](AnalysesApi.md#analyses_post) | **POST** /analyses | Create a new analysis.
[**analyses_upload_post**](AnalysesApi.md#analyses_upload_post) | **POST** /analyses/upload | Upload a file for a new batch analysis.
[**analyze_post**](AnalysesApi.md#analyze_post) | **POST** /analyze | Ad-hoc analysis of a list of documents.


# **analyses_analysis_id_delete**
> analyses_analysis_id_delete(analysis_id)

Delete an analyses.

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
api_instance = swagger_client.AnalysesApi(swagger_client.ApiClient(configuration))
analysis_id = 56 # int | ID of the analysis to delete

try:
    # Delete an analyses.
    api_instance.analyses_analysis_id_delete(analysis_id)
except ApiException as e:
    print("Exception when calling AnalysesApi->analyses_analysis_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| ID of the analysis to delete | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analyses_analysis_id_documents_download_get**
> analyses_analysis_id_documents_download_get(analysis_id, format=format)

Download analysis's documents.

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
api_instance = swagger_client.AnalysesApi(swagger_client.ApiClient(configuration))
analysis_id = 56 # int | ID of the analysis_id to get
format = 'format_example' # str | File format. Possible values are csv, jsonl, json and xlsx (optional)

try:
    # Download analysis's documents.
    api_instance.analyses_analysis_id_documents_download_get(analysis_id, format=format)
except ApiException as e:
    print("Exception when calling AnalysesApi->analyses_analysis_id_documents_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| ID of the analysis_id to get | 
 **format** | **str**| File format. Possible values are csv, jsonl, json and xlsx | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analyses_analysis_id_documents_get**
> LabelledDocumentsResponse analyses_analysis_id_documents_get(analysis_id, details=details, search=search, offset=offset, limit=limit)

Fetches all documents of a given analysis

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
api_instance = swagger_client.AnalysesApi(swagger_client.ApiClient(configuration))
analysis_id = 56 # int | ID of the analysis to get
details = 'details_example' # str | Which details API should return. Values might be any combination of 'segments', 'meta', 'tags' and 'stats'. (optional)
search = 'search_example' # str | Search by name (optional)
offset = 56 # int | An offset is simply the number of records you wish to skip before selecting records. (optional)
limit = 56 # int | Limit of entries that should be returned. (optional)

try:
    # Fetches all documents of a given analysis
    api_response = api_instance.analyses_analysis_id_documents_get(analysis_id, details=details, search=search, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysesApi->analyses_analysis_id_documents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| ID of the analysis to get | 
 **details** | **str**| Which details API should return. Values might be any combination of &#39;segments&#39;, &#39;meta&#39;, &#39;tags&#39; and &#39;stats&#39;. | [optional] 
 **search** | **str**| Search by name | [optional] 
 **offset** | **int**| An offset is simply the number of records you wish to skip before selecting records. | [optional] 
 **limit** | **int**| Limit of entries that should be returned. | [optional] 

### Return type

[**LabelledDocumentsResponse**](LabelledDocumentsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analyses_analysis_id_get**
> Analysis analyses_analysis_id_get(analysis_id)

Get an Analysis

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
api_instance = swagger_client.AnalysesApi(swagger_client.ApiClient(configuration))
analysis_id = 56 # int | ID of the analysis_id to get

try:
    # Get an Analysis
    api_response = api_instance.analyses_analysis_id_get(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysesApi->analyses_analysis_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| ID of the analysis_id to get | 

### Return type

[**Analysis**](Analysis.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analyses_analysis_id_put**
> Analysis analyses_analysis_id_put(analysis_id, body)

Change analysis's name

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
api_instance = swagger_client.AnalysesApi(swagger_client.ApiClient(configuration))
analysis_id = 56 # int | ID of the analysis to change
body = swagger_client.Body() # Body | 

try:
    # Change analysis's name
    api_response = api_instance.analyses_analysis_id_put(analysis_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysesApi->analyses_analysis_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **int**| ID of the analysis to change | 
 **body** | [**Body**](Body.md)|  | 

### Return type

[**Analysis**](Analysis.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analyses_get**
> Analyses analyses_get(model=model, offset=offset, limit=limit)

Return a list of analyses.

<br/>Lists all available analyses for a user. You can combine any of the parameters to filter the result<br/>

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
api_instance = swagger_client.AnalysesApi(swagger_client.ApiClient(configuration))
model = 56 # int | ID of the model (optional)
offset = 56 # int | An offset is simply the number of records you wish to skip before selecting records. (optional)
limit = 56 # int | Limit of entries that should be returned. (optional)

try:
    # Return a list of analyses.
    api_response = api_instance.analyses_get(model=model, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysesApi->analyses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **int**| ID of the model | [optional] 
 **offset** | **int**| An offset is simply the number of records you wish to skip before selecting records. | [optional] 
 **limit** | **int**| Limit of entries that should be returned. | [optional] 

### Return type

[**Analyses**](Analyses.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analyses_post**
> Analysis analyses_post(body)

Create a new analysis.

<br/>There are two ways of creating an analysis:<br/>- By calling the Create analysis endpoint with all the documents you want to analyze<br/>- In two steps: first one, upload a file in CSV, JSON, JSONL or XLSX format using the Upload a File endpoint. Then, use the file_id received and the column you want<br/>

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
api_instance = swagger_client.AnalysesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AnalysisCreate() # AnalysisCreate | 

try:
    # Create a new analysis.
    api_response = api_instance.analyses_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysesApi->analyses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnalysisCreate**](AnalysisCreate.md)|  | 

### Return type

[**Analysis**](Analysis.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analyses_upload_post**
> FilePreview analyses_upload_post(file)

Upload a file for a new batch analysis.

<br/>A file contains one or more documents that can be used to create a batch<br/>analysis.<br/>

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
api_instance = swagger_client.AnalysesApi(swagger_client.ApiClient(configuration))
file = '/path/to/file.txt' # file | file to upload

try:
    # Upload a file for a new batch analysis.
    api_response = api_instance.analyses_upload_post(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysesApi->analyses_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file to upload | 

### Return type

[**FilePreview**](FilePreview.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analyze_post**
> AdHocAnalysis analyze_post(body)

Ad-hoc analysis of a list of documents.

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
api_instance = swagger_client.AnalysesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdHocAnalysisCreate() # AdHocAnalysisCreate | 

try:
    # Ad-hoc analysis of a list of documents.
    api_response = api_instance.analyze_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysesApi->analyze_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdHocAnalysisCreate**](AdHocAnalysisCreate.md)|  | 

### Return type

[**AdHocAnalysis**](AdHocAnalysis.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

