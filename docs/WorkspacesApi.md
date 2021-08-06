# swagger_client.WorkspacesApi

All URIs are relative to *https://api.deepopinion.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_organization_id_default_post**](WorkspacesApi.md#organizations_organization_id_default_post) | **POST** /organizations/{organization_id}/default | Set a workspace as the default one.
[**organizations_organization_id_delete**](WorkspacesApi.md#organizations_organization_id_delete) | **DELETE** /organizations/{organization_id} | Deactivates a workspace.
[**organizations_organization_id_get**](WorkspacesApi.md#organizations_organization_id_get) | **GET** /organizations/{organization_id} | Get a workspace.
[**organizations_organization_id_invitation_invitation_id_delete**](WorkspacesApi.md#organizations_organization_id_invitation_invitation_id_delete) | **DELETE** /organizations/{organization_id}/invitation/{invitation_id} | Cancel an invitation.
[**organizations_organization_id_invitation_invitation_id_resend_post**](WorkspacesApi.md#organizations_organization_id_invitation_invitation_id_resend_post) | **POST** /organizations/{organization_id}/invitation/{invitation_id}/resend | Resend an invitation.
[**organizations_organization_id_permissions_get**](WorkspacesApi.md#organizations_organization_id_permissions_get) | **GET** /organizations/{organization_id}/permissions | Get all users&#39; permissions from a workspace
[**organizations_organization_id_permissions_permission_id_delete**](WorkspacesApi.md#organizations_organization_id_permissions_permission_id_delete) | **DELETE** /organizations/{organization_id}/permissions/{permission_id} | Remove a user from a workspace.
[**organizations_organization_id_permissions_permission_id_put**](WorkspacesApi.md#organizations_organization_id_permissions_permission_id_put) | **PUT** /organizations/{organization_id}/permissions/{permission_id} | Change user&#39;s role.
[**organizations_organization_id_permissions_post**](WorkspacesApi.md#organizations_organization_id_permissions_post) | **POST** /organizations/{organization_id}/permissions | Add a new user to a workspace.
[**organizations_organization_id_put**](WorkspacesApi.md#organizations_organization_id_put) | **PUT** /organizations/{organization_id} | Change a workspace.
[**organizations_organization_id_users_get**](WorkspacesApi.md#organizations_organization_id_users_get) | **GET** /organizations/{organization_id}/users | Get all users of a workspace
[**organizations_organization_id_users_invite_post**](WorkspacesApi.md#organizations_organization_id_users_invite_post) | **POST** /organizations/{organization_id}/users/invite | Invite users to a workspace.
[**organizations_organization_id_users_invites_get**](WorkspacesApi.md#organizations_organization_id_users_invites_get) | **GET** /organizations/{organization_id}/users/invites | List all pending invitations.
[**organizations_post**](WorkspacesApi.md#organizations_post) | **POST** /organizations | Create a new workspace.
[**organizations_users_invite_accept_post**](WorkspacesApi.md#organizations_users_invite_accept_post) | **POST** /organizations/users/invite/accept | Accept an invitation.


# **organizations_organization_id_default_post**
> organizations_organization_id_default_post(organization_id, body)

Set a workspace as the default one.

<br/>Default workspaces will come pre-selected on Studio<br/>

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
organization_id = 56 # int | ID of the workspace
body = swagger_client.SetDefaultBody() # SetDefaultBody | 

try:
    # Set a workspace as the default one.
    api_instance.organizations_organization_id_default_post(organization_id, body)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_organization_id_default_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the workspace | 
 **body** | [**SetDefaultBody**](SetDefaultBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_id_delete**
> Workspace organizations_organization_id_delete(organization_id)

Deactivates a workspace.

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
organization_id = 56 # int | ID of the workspace

try:
    # Deactivates a workspace.
    api_response = api_instance.organizations_organization_id_delete(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_organization_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the workspace | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_id_get**
> Workspace organizations_organization_id_get(organization_id)

Get a workspace.

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
organization_id = 56 # int | ID of the workspace

try:
    # Get a workspace.
    api_response = api_instance.organizations_organization_id_get(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_organization_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the workspace | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_id_invitation_invitation_id_delete**
> organizations_organization_id_invitation_invitation_id_delete(organization_id, invitation_id)

Cancel an invitation.

<br/>The invitation will be removed and the link user received by email won't<br/>be valid anymore.<br/>

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
organization_id = 56 # int | ID of the workspace
invitation_id = 56 # int | ID of the invitation

try:
    # Cancel an invitation.
    api_instance.organizations_organization_id_invitation_invitation_id_delete(organization_id, invitation_id)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_organization_id_invitation_invitation_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the workspace | 
 **invitation_id** | **int**| ID of the invitation | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_id_invitation_invitation_id_resend_post**
> organizations_organization_id_invitation_invitation_id_resend_post(organization_id, invitation_id)

Resend an invitation.

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
organization_id = 56 # int | ID of the workspace
invitation_id = 56 # int | ID of the invitation

try:
    # Resend an invitation.
    api_instance.organizations_organization_id_invitation_invitation_id_resend_post(organization_id, invitation_id)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_organization_id_invitation_invitation_id_resend_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the workspace | 
 **invitation_id** | **int**| ID of the invitation | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_id_permissions_get**
> Permissions organizations_organization_id_permissions_get(organization_id)

Get all users' permissions from a workspace

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
organization_id = 56 # int | ID of the workspace

try:
    # Get all users' permissions from a workspace
    api_response = api_instance.organizations_organization_id_permissions_get(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_organization_id_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the workspace | 

### Return type

[**Permissions**](Permissions.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_id_permissions_permission_id_delete**
> organizations_organization_id_permissions_permission_id_delete(organization_id, permission_id)

Remove a user from a workspace.

<br/>A workspace must have at least one manager<br/>

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
organization_id = 56 # int | ID of the workspace
permission_id = 56 # int | ID of the permission to remove

try:
    # Remove a user from a workspace.
    api_instance.organizations_organization_id_permissions_permission_id_delete(organization_id, permission_id)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_organization_id_permissions_permission_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the workspace | 
 **permission_id** | **int**| ID of the permission to remove | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_id_permissions_permission_id_put**
> organizations_organization_id_permissions_permission_id_put(organization_id, permission_id, body)

Change user's role.

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
organization_id = 56 # int | ID of the workspace
permission_id = 56 # int | ID of the permission to change
body = swagger_client.ChangePermissionBody() # ChangePermissionBody | 

try:
    # Change user's role.
    api_instance.organizations_organization_id_permissions_permission_id_put(organization_id, permission_id, body)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_organization_id_permissions_permission_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the workspace | 
 **permission_id** | **int**| ID of the permission to change | 
 **body** | [**ChangePermissionBody**](ChangePermissionBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_id_permissions_post**
> Permission organizations_organization_id_permissions_post(organization_id, body)

Add a new user to a workspace.

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
organization_id = 56 # int | ID of the workspace
body = swagger_client.PermissionInput() # PermissionInput | 

try:
    # Add a new user to a workspace.
    api_response = api_instance.organizations_organization_id_permissions_post(organization_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_organization_id_permissions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the workspace | 
 **body** | [**PermissionInput**](PermissionInput.md)|  | 

### Return type

[**Permission**](Permission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_id_put**
> Workspace organizations_organization_id_put(organization_id, body)

Change a workspace.

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
organization_id = 56 # int | ID of the workspace
body = swagger_client.CreateWorkspaceInput() # CreateWorkspaceInput | 

try:
    # Change a workspace.
    api_response = api_instance.organizations_organization_id_put(organization_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_organization_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the workspace | 
 **body** | [**CreateWorkspaceInput**](CreateWorkspaceInput.md)|  | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_id_users_get**
> Users organizations_organization_id_users_get(organization_id)

Get all users of a workspace

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
organization_id = 56 # int | ID of the workspace

try:
    # Get all users of a workspace
    api_response = api_instance.organizations_organization_id_users_get(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_organization_id_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the workspace | 

### Return type

[**Users**](Users.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_id_users_invite_post**
> InviteUsersResponse organizations_organization_id_users_invite_post(organization_id, body)

Invite users to a workspace.

<br/>ALl invited users will have the same defined permission.<br/>

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
organization_id = 56 # int | ID of the workspace
body = swagger_client.InviteUsersBody() # InviteUsersBody | 

try:
    # Invite users to a workspace.
    api_response = api_instance.organizations_organization_id_users_invite_post(organization_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_organization_id_users_invite_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the workspace | 
 **body** | [**InviteUsersBody**](InviteUsersBody.md)|  | 

### Return type

[**InviteUsersResponse**](InviteUsersResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_id_users_invites_get**
> Invitations organizations_organization_id_users_invites_get(organization_id)

List all pending invitations.

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
organization_id = 56 # int | ID of the workspace

try:
    # List all pending invitations.
    api_response = api_instance.organizations_organization_id_users_invites_get(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_organization_id_users_invites_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| ID of the workspace | 

### Return type

[**Invitations**](Invitations.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_post**
> Workspace organizations_post(body)

Create a new workspace.

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateWorkspaceInput() # CreateWorkspaceInput | 

try:
    # Create a new workspace.
    api_response = api_instance.organizations_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWorkspaceInput**](CreateWorkspaceInput.md)|  | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_users_invite_accept_post**
> organizations_users_invite_accept_post(body)

Accept an invitation.

<br/>The data necessary to create a new user should be sent. If the user is<br/>already a member of Studio, only the membership will be added.<br/> 

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AcceptInvitationInput() # AcceptInvitationInput | 

try:
    # Accept an invitation.
    api_instance.organizations_users_invite_accept_post(body)
except ApiException as e:
    print("Exception when calling WorkspacesApi->organizations_users_invite_accept_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AcceptInvitationInput**](AcceptInvitationInput.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

