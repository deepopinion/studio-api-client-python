# swagger_client.UsersApi

All URIs are relative to *https://api.deepopinion.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login_post**](UsersApi.md#auth_login_post) | **POST** /auth/login | Log in a user
[**auth_logout_post**](UsersApi.md#auth_logout_post) | **POST** /auth/logout | Log out a user.
[**auth_register_post**](UsersApi.md#auth_register_post) | **POST** /auth/register | Create a new account.
[**auth_status_get**](UsersApi.md#auth_status_get) | **GET** /auth/status | User login status
[**password_email_post**](UsersApi.md#password_email_post) | **POST** /password/email | Request a link to reset the password.
[**password_reset_post**](UsersApi.md#password_reset_post) | **POST** /password/reset | Reset a password.
[**users_email_verify_post**](UsersApi.md#users_email_verify_post) | **POST** /users/email/verify | Confirm an email
[**users_email_verify_resend_post**](UsersApi.md#users_email_verify_resend_post) | **POST** /users/email/verify/resend | Resend verification email
[**users_user_id_delete**](UsersApi.md#users_user_id_delete) | **DELETE** /users/{user_id} | Delete user&#39;s account.
[**users_user_id_get**](UsersApi.md#users_user_id_get) | **GET** /users/{user_id} | Get a user.
[**users_user_id_keys_get**](UsersApi.md#users_user_id_keys_get) | **GET** /users/{user_id}/keys | List all keys associated to a user
[**users_user_id_keys_key_id_delete**](UsersApi.md#users_user_id_keys_key_id_delete) | **DELETE** /users/{user_id}/keys/{key_id} | Delete a key associated to a user
[**users_user_id_keys_post**](UsersApi.md#users_user_id_keys_post) | **POST** /users/{user_id}/keys | Add a product key to a user
[**users_user_id_permissions_get**](UsersApi.md#users_user_id_permissions_get) | **GET** /users/{user_id}/permissions | Get user permissions.
[**users_user_id_permissions_put**](UsersApi.md#users_user_id_permissions_put) | **PUT** /users/{user_id}/permissions | Change user permission.
[**users_user_id_put**](UsersApi.md#users_user_id_put) | **PUT** /users/{user_id} | Change a user.


# **auth_login_post**
> LoginResponse auth_login_post(body)

Log in a user

<br/>Login via email and password. A successful request returns the attribute auth_token that can be used for authenticate the user at other calls.<br/><br/>It's also possible to log in with a \"first time login\". This token is sent to users we manually created through Studio Admin<br/>

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserLogin() # UserLogin | 

try:
    # Log in a user
    api_response = api_instance.auth_login_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->auth_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserLogin**](UserLogin.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_logout_post**
> auth_logout_post()

Log out a user.

<br/>Invalidates the current auth token of the user.<br/>

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Log out a user.
    api_instance.auth_logout_post()
except ApiException as e:
    print("Exception when calling UsersApi->auth_logout_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_register_post**
> RegistrationResponse auth_register_post(body)

Create a new account.

<br/>A successful request returns an `auth_token` that can be used for subsequent calls.<br/><br/>

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.User() # User | 

try:
    # Create a new account.
    api_response = api_instance.auth_register_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->auth_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | 

### Return type

[**RegistrationResponse**](RegistrationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_status_get**
> auth_status_get()

User login status

<br/>Status information about the current user.<br/>

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # User login status
    api_instance.auth_status_get()
except ApiException as e:
    print("Exception when calling UsersApi->auth_status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_email_post**
> password_email_post(body)

Request a link to reset the password.

<br/>Triggers a password reset for a certain email address corresponding to a<br/>    registered user. If email exists, a new reset reset_password_token is<br/>    created and an email is sent to the corresponding user.<br/>

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResetPasswordSendInput() # ResetPasswordSendInput | 

try:
    # Request a link to reset the password.
    api_instance.password_email_post(body)
except ApiException as e:
    print("Exception when calling UsersApi->password_email_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetPasswordSendInput**](ResetPasswordSendInput.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_reset_post**
> password_reset_post(body)

Reset a password.

<br/>Changes a users password by its corresponding unique one-time reset token<br/>the user receives in a password reset email.<br/>

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResetPasswordInput() # ResetPasswordInput | 

try:
    # Reset a password.
    api_instance.password_reset_post(body)
except ApiException as e:
    print("Exception when calling UsersApi->password_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetPasswordInput**](ResetPasswordInput.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_email_verify_post**
> users_email_verify_post(body)

Confirm an email

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConfirmUserEmail() # ConfirmUserEmail | 

try:
    # Confirm an email
    api_instance.users_email_verify_post(body)
except ApiException as e:
    print("Exception when calling UsersApi->users_email_verify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfirmUserEmail**](ConfirmUserEmail.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_email_verify_resend_post**
> users_email_verify_resend_post()

Resend verification email

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Resend verification email
    api_instance.users_email_verify_resend_post()
except ApiException as e:
    print("Exception when calling UsersApi->users_email_verify_resend_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_delete**
> users_user_id_delete(user_id)

Delete user's account.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | ID of the user

try:
    # Delete user's account.
    api_instance.users_user_id_delete(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_get**
> User users_user_id_get(user_id)

Get a user.

<br/>Detailed information about a user. The user ID must be given as route parameter. If not an admin, this route is accessible only for the given and authenticated user.<br/>

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | ID of the user

try:
    # Get a user.
    api_response = api_instance.users_user_id_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_keys_get**
> ProductKeys users_user_id_keys_get(user_id)

List all keys associated to a user

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | ID of the user

try:
    # List all keys associated to a user
    api_response = api_instance.users_user_id_keys_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_keys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user | 

### Return type

[**ProductKeys**](ProductKeys.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_keys_key_id_delete**
> ProductKeys users_user_id_keys_key_id_delete(user_id, key_id)

Delete a key associated to a user

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | ID of the user
key_id = 56 # int | ID of the key

try:
    # Delete a key associated to a user
    api_response = api_instance.users_user_id_keys_key_id_delete(user_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_keys_key_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user | 
 **key_id** | **int**| ID of the key | 

### Return type

[**ProductKeys**](ProductKeys.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_keys_post**
> ProductKey users_user_id_keys_post(user_id)

Add a product key to a user

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | ID of the user

try:
    # Add a product key to a user
    api_response = api_instance.users_user_id_keys_post(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_keys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user | 

### Return type

[**ProductKey**](ProductKey.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_permissions_get**
> User users_user_id_permissions_get(user_id)

Get user permissions.

<br/>Return user attributes including superuser and betauser permission.<br/>

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | ID of the user

try:
    # Get user permissions.
    api_response = api_instance.users_user_id_permissions_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_permissions_put**
> User users_user_id_permissions_put(user_id, body)

Change user permission.

<br/>Use this endpoint to set and revoke superuser and betauser permission.<br/>

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | ID of the user
body = swagger_client.UserPermission() # UserPermission | 

try:
    # Change user permission.
    api_response = api_instance.users_user_id_permissions_put(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_permissions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user | 
 **body** | [**UserPermission**](UserPermission.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_put**
> User users_user_id_put(user_id, body)

Change a user.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | ID of the user
body = swagger_client.User() # User | 

try:
    # Change a user.
    api_response = api_instance.users_user_id_put(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user | 
 **body** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

