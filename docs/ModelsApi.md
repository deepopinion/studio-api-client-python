# swagger_client.ModelsApi

All URIs are relative to *https://api.deepopinion.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**models_get**](ModelsApi.md#models_get) | **GET** /models | Get models user is authorized to see.
[**models_model_download_get**](ModelsApi.md#models_model_download_get) | **GET** /models/{model}/download | Download a model by name
[**models_model_id_analyses_get**](ModelsApi.md#models_model_id_analyses_get) | **GET** /models/{model_id}/analyses | Fetches all analyses related to this model.
[**models_model_id_delete**](ModelsApi.md#models_model_id_delete) | **DELETE** /models/{model_id} | Delete a model.
[**models_model_id_download_get**](ModelsApi.md#models_model_id_download_get) | **GET** /models/{model_id}/download | Download a model
[**models_model_id_get**](ModelsApi.md#models_model_id_get) | **GET** /models/{model_id} | Get a model by its ID
[**models_model_id_permissions_get**](ModelsApi.md#models_model_id_permissions_get) | **GET** /models/{model_id}/permissions | Get all model&#39;s permission.
[**models_model_id_put**](ModelsApi.md#models_model_id_put) | **PUT** /models/{model_id} | Update a model.
[**models_model_id_star_post**](ModelsApi.md#models_model_id_star_post) | **POST** /models/{model_id}/star | Favorite a model.
[**models_model_id_unstar_post**](ModelsApi.md#models_model_id_unstar_post) | **POST** /models/{model_id}/unstar | Remove a model from favorites.
[**models_upload_post**](ModelsApi.md#models_upload_post) | **POST** /models/upload | Upload a model.
[**organizations_organization_models_get**](ModelsApi.md#organizations_organization_models_get) | **GET** /organizations/{organization}/models | Get models user is authorized to see.
[**organizations_organization_models_model_download_get**](ModelsApi.md#organizations_organization_models_model_download_get) | **GET** /organizations/{organization}/models/{model}/download | Download a model by organization name and model name
[**projects_project_id_models_get**](ModelsApi.md#projects_project_id_models_get) | **GET** /projects/{project_id}/models | Get models that belongs to a project
[**projects_project_id_models_model_id_delete**](ModelsApi.md#projects_project_id_models_model_id_delete) | **DELETE** /projects/{project_id}/models/{model_id} | Delete a model that belongs to a project..
[**projects_project_id_models_model_id_download_get**](ModelsApi.md#projects_project_id_models_model_id_download_get) | **GET** /projects/{project_id}/models/{model_id}/download | Download a model that belongs to a project
[**projects_project_id_models_model_id_get**](ModelsApi.md#projects_project_id_models_model_id_get) | **GET** /projects/{project_id}/models/{model_id} | Get a specific model that belongs to a project
[**projects_project_id_models_model_id_put**](ModelsApi.md#projects_project_id_models_model_id_put) | **PUT** /projects/{project_id}/models/{model_id} | Update a model that belongs to a project.
[**projects_project_id_models_post**](ModelsApi.md#projects_project_id_models_post) | **POST** /projects/{project_id}/models | Train a new model.


# **models_get**
> GetModels models_get(collection_id=collection_id, public=public, starred=starred, search=search, type=type, offset=offset, limit=limit)

Get models user is authorized to see.

<br/>Parameters can be combined to filter models.<br/>

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
collection_id = 56 # int | The collection ID of the model (optional)
public = true # bool | if model is public or not (optional)
starred = true # bool | if model is starred or not (optional)
search = 'search_example' # str | Search a model by name (optional)
type = 'type_example' # str | model type (optional)
offset = 56 # int | An offset is simply the number of records you wish to skip before selecting records. (optional)
limit = 56 # int | Limit of entries that should be returned. (optional)

try:
    # Get models user is authorized to see.
    api_response = api_instance.models_get(collection_id=collection_id, public=public, starred=starred, search=search, type=type, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->models_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| The collection ID of the model | [optional] 
 **public** | **bool**| if model is public or not | [optional] 
 **starred** | **bool**| if model is starred or not | [optional] 
 **search** | **str**| Search a model by name | [optional] 
 **type** | **str**| model type | [optional] 
 **offset** | **int**| An offset is simply the number of records you wish to skip before selecting records. | [optional] 
 **limit** | **int**| Limit of entries that should be returned. | [optional] 

### Return type

[**GetModels**](GetModels.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_model_download_get**
> models_model_download_get(model)

Download a model by name

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
model = 'model_example' # str | The model name

try:
    # Download a model by name
    api_instance.models_model_download_get(model)
except ApiException as e:
    print("Exception when calling ModelsApi->models_model_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| The model name | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_model_id_analyses_get**
> GetAnalyses models_model_id_analyses_get(model_id, offset=offset, limit=limit)

Fetches all analyses related to this model.

<br/>Use URL params to control or filter the result:<br/>- ?offset=0&limit=10 to have a paginated view<br/>- ?details=segments,meta,tags to show details of a document<br/>     * segments: Show segments of a document<br/>     * tags: Show tags of a document<br/>     * meta: Show all the additional attributes that were originally given as the document was uploaded<br/><br/>The pagination should be done by increasing the offset by the value of limit until the property has_more is false<br/>

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
model_id = 56 # int | ID of the model
offset = 56 # int | An offset is simply the number of records you wish to skip before selecting records. (optional)
limit = 56 # int | Limit of entries that should be returned. (optional)

try:
    # Fetches all analyses related to this model.
    api_response = api_instance.models_model_id_analyses_get(model_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->models_model_id_analyses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| ID of the model | 
 **offset** | **int**| An offset is simply the number of records you wish to skip before selecting records. | [optional] 
 **limit** | **int**| Limit of entries that should be returned. | [optional] 

### Return type

[**GetAnalyses**](GetAnalyses.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_model_id_delete**
> models_model_id_delete(model_id)

Delete a model.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
model_id = 56 # int | ID of the model

try:
    # Delete a model.
    api_instance.models_model_id_delete(model_id)
except ApiException as e:
    print("Exception when calling ModelsApi->models_model_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| ID of the model | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_model_id_download_get**
> models_model_id_download_get(model_id)

Download a model

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
model_id = 56 # int | ID of the model

try:
    # Download a model
    api_instance.models_model_id_download_get(model_id)
except ApiException as e:
    print("Exception when calling ModelsApi->models_model_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| ID of the model | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_model_id_get**
> GetModels models_model_id_get(model_id)

Get a model by its ID

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
model_id = 56 # int | ID of the model

try:
    # Get a model by its ID
    api_response = api_instance.models_model_id_get(model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->models_model_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| ID of the model | 

### Return type

[**GetModels**](GetModels.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_model_id_permissions_get**
> ModelPermissions models_model_id_permissions_get(model_id)

Get all model's permission.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
model_id = 56 # int | ID of the model

try:
    # Get all model's permission.
    api_response = api_instance.models_model_id_permissions_get(model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->models_model_id_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| ID of the model | 

### Return type

[**ModelPermissions**](ModelPermissions.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_model_id_put**
> Model models_model_id_put(model_id, body)

Update a model.

<br/>Updates meta data of a model. All model's attributes can be changed:<br/>

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
model_id = 56 # int | ID of the model
body = swagger_client.Model() # Model | 

try:
    # Update a model.
    api_response = api_instance.models_model_id_put(model_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->models_model_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| ID of the model | 
 **body** | [**Model**](Model.md)|  | 

### Return type

[**Model**](Model.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_model_id_star_post**
> models_model_id_star_post(model_id)

Favorite a model.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
model_id = 56 # int | ID of the model

try:
    # Favorite a model.
    api_instance.models_model_id_star_post(model_id)
except ApiException as e:
    print("Exception when calling ModelsApi->models_model_id_star_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| ID of the model | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_model_id_unstar_post**
> models_model_id_unstar_post(model_id)

Remove a model from favorites.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
model_id = 56 # int | ID of the model

try:
    # Remove a model from favorites.
    api_instance.models_model_id_unstar_post(model_id)
except ApiException as e:
    print("Exception when calling ModelsApi->models_model_id_unstar_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| ID of the model | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_upload_post**
> Model models_upload_post(file, display_name, base=base, score=score, long_description=long_description, short_description=short_description, status=status, language=language, name=name)

Upload a model.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
file = '/path/to/file.txt' # file | file to upload
display_name = 'display_name_example' # str | a friendly name
base = 'base_example' # str | the name of the model used to create the modal that's being changed (optional)
score = 56 # int | model score. As this is a result of a training session, this value shouldn't be touched (optional)
long_description = 'long_description_example' # str | a longer description which proper describes the model (optional)
short_description = 'short_description_example' # str | a short description to help users quickly identify the model (optional)
status = 'status_example' # str | the model status (optional)
language = 'language_example' # str |  (optional)
name = 'name_example' # str | internal name. It should be unique for a workspace (optional)

try:
    # Upload a model.
    api_response = api_instance.models_upload_post(file, display_name, base=base, score=score, long_description=long_description, short_description=short_description, status=status, language=language, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->models_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file to upload | 
 **display_name** | **str**| a friendly name | 
 **base** | **str**| the name of the model used to create the modal that&#39;s being changed | [optional] 
 **score** | **int**| model score. As this is a result of a training session, this value shouldn&#39;t be touched | [optional] 
 **long_description** | **str**| a longer description which proper describes the model | [optional] 
 **short_description** | **str**| a short description to help users quickly identify the model | [optional] 
 **status** | **str**| the model status | [optional] 
 **language** | **str**|  | [optional] 
 **name** | **str**| internal name. It should be unique for a workspace | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_models_get**
> GetModels organizations_organization_models_get(organization, collection_id=collection_id, public=public, starred=starred, type=type, offset=offset, limit=limit)

Get models user is authorized to see.

<br/>Parameters can be combined to filter models.<br/>

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
organization = 'organization_example' # str | organization name
collection_id = 56 # int | The collection ID of the model (optional)
public = true # bool | if model is public or not (optional)
starred = true # bool | if model is starred or not (optional)
type = 'type_example' # str | model type (optional)
offset = 56 # int | An offset is simply the number of records you wish to skip before selecting records. (optional)
limit = 56 # int | Limit of entries that should be returned. (optional)

try:
    # Get models user is authorized to see.
    api_response = api_instance.organizations_organization_models_get(organization, collection_id=collection_id, public=public, starred=starred, type=type, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->organizations_organization_models_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**| organization name | 
 **collection_id** | **int**| The collection ID of the model | [optional] 
 **public** | **bool**| if model is public or not | [optional] 
 **starred** | **bool**| if model is starred or not | [optional] 
 **type** | **str**| model type | [optional] 
 **offset** | **int**| An offset is simply the number of records you wish to skip before selecting records. | [optional] 
 **limit** | **int**| Limit of entries that should be returned. | [optional] 

### Return type

[**GetModels**](GetModels.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_models_model_download_get**
> organizations_organization_models_model_download_get(organization, model)

Download a model by organization name and model name

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
organization = 'organization_example' # str | The organization name
model = 'model_example' # str | The model name

try:
    # Download a model by organization name and model name
    api_instance.organizations_organization_models_model_download_get(organization, model)
except ApiException as e:
    print("Exception when calling ModelsApi->organizations_organization_models_model_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**| The organization name | 
 **model** | **str**| The model name | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_models_get**
> Models projects_project_id_models_get(project_id)

Get models that belongs to a project

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project

try:
    # Get models that belongs to a project
    api_response = api_instance.projects_project_id_models_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->projects_project_id_models_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 

### Return type

[**Models**](Models.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_models_model_id_delete**
> projects_project_id_models_model_id_delete(project_id, model_id)

Delete a model that belongs to a project..

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
model_id = 56 # int | ID of the model

try:
    # Delete a model that belongs to a project..
    api_instance.projects_project_id_models_model_id_delete(project_id, model_id)
except ApiException as e:
    print("Exception when calling ModelsApi->projects_project_id_models_model_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **model_id** | **int**| ID of the model | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_models_model_id_download_get**
> projects_project_id_models_model_id_download_get(project_id, model_id)

Download a model that belongs to a project

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
model_id = 56 # int | ID of the model

try:
    # Download a model that belongs to a project
    api_instance.projects_project_id_models_model_id_download_get(project_id, model_id)
except ApiException as e:
    print("Exception when calling ModelsApi->projects_project_id_models_model_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **model_id** | **int**| ID of the model | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_models_model_id_get**
> DetailedModel projects_project_id_models_model_id_get(project_id, model_id)

Get a specific model that belongs to a project

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
model_id = 56 # int | ID of the model

try:
    # Get a specific model that belongs to a project
    api_response = api_instance.projects_project_id_models_model_id_get(project_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->projects_project_id_models_model_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **model_id** | **int**| ID of the model | 

### Return type

[**DetailedModel**](DetailedModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_models_model_id_put**
> Model projects_project_id_models_model_id_put(project_id, model_id, body)

Update a model that belongs to a project.

<br/>Updates meta data of a model. All model's attributes can be changed:<br/>

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
model_id = 56 # int | ID of the model
body = swagger_client.Model() # Model | 

try:
    # Update a model that belongs to a project.
    api_response = api_instance.projects_project_id_models_model_id_put(project_id, model_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->projects_project_id_models_model_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **model_id** | **int**| ID of the model | 
 **body** | [**Model**](Model.md)|  | 

### Return type

[**Model**](Model.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_models_post**
> Model projects_project_id_models_post(project_id, body)

Train a new model.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | ID of the project
body = swagger_client.ModelCreate() # ModelCreate | 

try:
    # Train a new model.
    api_response = api_instance.projects_project_id_models_post(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->projects_project_id_models_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**ModelCreate**](ModelCreate.md)|  | 

### Return type

[**Model**](Model.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

