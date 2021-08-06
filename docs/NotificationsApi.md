# swagger_client.NotificationsApi

All URIs are relative to *https://api.deepopinion.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_user_id_notifications_get**](NotificationsApi.md#users_user_id_notifications_get) | **GET** /users/{user_id}/notifications | Get all user&#39;s notification
[**users_user_id_notifications_notification_id_get**](NotificationsApi.md#users_user_id_notifications_notification_id_get) | **GET** /users/{user_id}/notifications/{notification_id} | Get a notification
[**users_user_id_notifications_notification_id_put**](NotificationsApi.md#users_user_id_notifications_notification_id_put) | **PUT** /users/{user_id}/notifications/{notification_id} | Change a notification


# **users_user_id_notifications_get**
> Notifications users_user_id_notifications_get(user_id, offset=offset, limit=limit)

Get all user's notification

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
api_instance = swagger_client.NotificationsApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | ID of the user
offset = 56 # int | An offset is simply the number of records you wish to skip before selecting records. (optional)
limit = 56 # int | Limit of entries that should be returned. (optional)

try:
    # Get all user's notification
    api_response = api_instance.users_user_id_notifications_get(user_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->users_user_id_notifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user | 
 **offset** | **int**| An offset is simply the number of records you wish to skip before selecting records. | [optional] 
 **limit** | **int**| Limit of entries that should be returned. | [optional] 

### Return type

[**Notifications**](Notifications.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_notifications_notification_id_get**
> Notification users_user_id_notifications_notification_id_get(user_id, notification_id)

Get a notification

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
api_instance = swagger_client.NotificationsApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | ID of the user
notification_id = 56 # int | ID of the notification

try:
    # Get a notification
    api_response = api_instance.users_user_id_notifications_notification_id_get(user_id, notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->users_user_id_notifications_notification_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user | 
 **notification_id** | **int**| ID of the notification | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_notifications_notification_id_put**
> Notification users_user_id_notifications_notification_id_put(user_id, notification_id, body)

Change a notification

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
api_instance = swagger_client.NotificationsApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | ID of the user
notification_id = 56 # int | ID of the notification
body = swagger_client.NotificationInput() # NotificationInput | Data to be changed

try:
    # Change a notification
    api_response = api_instance.users_user_id_notifications_notification_id_put(user_id, notification_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->users_user_id_notifications_notification_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user | 
 **notification_id** | **int**| ID of the notification | 
 **body** | [**NotificationInput**](NotificationInput.md)| Data to be changed | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

