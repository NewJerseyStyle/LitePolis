# litepolis_client.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_userprofile_api_v1_secure_users_profile_post**](UserApi.md#create_userprofile_api_v1_secure_users_profile_post) | **POST** /api/v1/secure/users/profile | Create Userprofile
[**delete_userprofile_api_v1_secure_users_profile_delete**](UserApi.md#delete_userprofile_api_v1_secure_users_profile_delete) | **DELETE** /api/v1/secure/users/profile | Delete Userprofile
[**get_testroute_api_v1_secure_get**](UserApi.md#get_testroute_api_v1_secure_get) | **GET** /api/v1/secure/ | Get Testroute
[**get_userauth_api_v1_secure_users_auth_post**](UserApi.md#get_userauth_api_v1_secure_users_auth_post) | **POST** /api/v1/secure/users/auth | Get Userauth
[**get_userprofile_api_v1_secure_users_profile_get**](UserApi.md#get_userprofile_api_v1_secure_users_profile_get) | **GET** /api/v1/secure/users/profile | Get Userprofile
[**get_userrole_api_v1_secure_users_role_get**](UserApi.md#get_userrole_api_v1_secure_users_role_get) | **GET** /api/v1/secure/users/role | Get Userrole
[**update_userprofile_api_v1_secure_users_profile_put**](UserApi.md#update_userprofile_api_v1_secure_users_profile_put) | **PUT** /api/v1/secure/users/profile | Update Userprofile
[**update_usertoken_api_v1_secure_users_renew_put**](UserApi.md#update_usertoken_api_v1_secure_users_renew_put) | **PUT** /api/v1/secure/users/renew | Update Usertoken


# **create_userprofile_api_v1_secure_users_profile_post**
> ResponseMessage create_userprofile_api_v1_secure_users_profile_post(user_profile)

Create Userprofile

Create a new user profile.  Parameters ---------- user_profile : UserProfile     User profile information. user : dict     Authenticated user information.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.response_message import ResponseMessage
from litepolis_client.models.user_profile import UserProfile
from litepolis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = litepolis_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with litepolis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = litepolis_client.UserApi(api_client)
    user_profile = litepolis_client.UserProfile() # UserProfile | 

    try:
        # Create Userprofile
        api_response = api_instance.create_userprofile_api_v1_secure_users_profile_post(user_profile)
        print("The response of UserApi->create_userprofile_api_v1_secure_users_profile_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_userprofile_api_v1_secure_users_profile_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_profile** | [**UserProfile**](UserProfile.md)|  | 

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_userprofile_api_v1_secure_users_profile_delete**
> object delete_userprofile_api_v1_secure_users_profile_delete()

Delete Userprofile

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = litepolis_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with litepolis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = litepolis_client.UserApi(api_client)

    try:
        # Delete Userprofile
        api_response = api_instance.delete_userprofile_api_v1_secure_users_profile_delete()
        print("The response of UserApi->delete_userprofile_api_v1_secure_users_profile_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_userprofile_api_v1_secure_users_profile_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_testroute_api_v1_secure_get**
> ResponseMessage get_testroute_api_v1_secure_get()

Get Testroute

This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         'id': <user_id>,         'email': <user_email>,         'role': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user's id, email, and role.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.response_message import ResponseMessage
from litepolis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = litepolis_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with litepolis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = litepolis_client.UserApi(api_client)

    try:
        # Get Testroute
        api_response = api_instance.get_testroute_api_v1_secure_get()
        print("The response of UserApi->get_testroute_api_v1_secure_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_testroute_api_v1_secure_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_userauth_api_v1_secure_users_auth_post**
> ResponseMessage get_userauth_api_v1_secure_users_auth_post(user_profile)

Get Userauth

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.response_message import ResponseMessage
from litepolis_client.models.user_profile import UserProfile
from litepolis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = litepolis_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with litepolis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = litepolis_client.UserApi(api_client)
    user_profile = litepolis_client.UserProfile() # UserProfile | 

    try:
        # Get Userauth
        api_response = api_instance.get_userauth_api_v1_secure_users_auth_post(user_profile)
        print("The response of UserApi->get_userauth_api_v1_secure_users_auth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_userauth_api_v1_secure_users_auth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_profile** | [**UserProfile**](UserProfile.md)|  | 

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_userprofile_api_v1_secure_users_profile_get**
> ResponseMessage get_userprofile_api_v1_secure_users_profile_get()

Get Userprofile

This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         'id': <user_id>,         'email': <user_email>,         'role': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user's id, email, and role.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.response_message import ResponseMessage
from litepolis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = litepolis_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with litepolis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = litepolis_client.UserApi(api_client)

    try:
        # Get Userprofile
        api_response = api_instance.get_userprofile_api_v1_secure_users_profile_get()
        print("The response of UserApi->get_userprofile_api_v1_secure_users_profile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_userprofile_api_v1_secure_users_profile_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_userrole_api_v1_secure_users_role_get**
> ResponseMessage get_userrole_api_v1_secure_users_role_get()

Get Userrole

This endpoint returns the role of the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         'id': <user_id>,         'email': <user_email>,         'role': <user_role>     }  Returns ------- ResponseMessage     `detail` string of the user's role.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.response_message import ResponseMessage
from litepolis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = litepolis_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with litepolis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = litepolis_client.UserApi(api_client)

    try:
        # Get Userrole
        api_response = api_instance.get_userrole_api_v1_secure_users_role_get()
        print("The response of UserApi->get_userrole_api_v1_secure_users_role_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_userrole_api_v1_secure_users_role_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_userprofile_api_v1_secure_users_profile_put**
> object update_userprofile_api_v1_secure_users_profile_put(user_profile)

Update Userprofile

Update the authenticated user's profile.  Parameters ---------- update_user : UpdateUserProfile     User profile information to update. user : dict     Authenticated user information.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.user_profile import UserProfile
from litepolis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = litepolis_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with litepolis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = litepolis_client.UserApi(api_client)
    user_profile = litepolis_client.UserProfile() # UserProfile | 

    try:
        # Update Userprofile
        api_response = api_instance.update_userprofile_api_v1_secure_users_profile_put(user_profile)
        print("The response of UserApi->update_userprofile_api_v1_secure_users_profile_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_userprofile_api_v1_secure_users_profile_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_profile** | [**UserProfile**](UserProfile.md)|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_usertoken_api_v1_secure_users_renew_put**
> ResponseMessage update_usertoken_api_v1_secure_users_renew_put()

Update Usertoken

Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         'id': <user_id>,         'email': <user_email>,         'role': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.response_message import ResponseMessage
from litepolis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = litepolis_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with litepolis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = litepolis_client.UserApi(api_client)

    try:
        # Update Usertoken
        api_response = api_instance.update_usertoken_api_v1_secure_users_renew_put()
        print("The response of UserApi->update_usertoken_api_v1_secure_users_renew_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_usertoken_api_v1_secure_users_renew_put: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

