# litepolis_client.APIKeysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_usertoken_api_v1_secure_users_renew_put**](APIKeysApi.md#update_usertoken_api_v1_secure_users_renew_put) | **PUT** /api/v1/secure/users/renew | Update Usertoken


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
    api_instance = litepolis_client.APIKeysApi(api_client)

    try:
        # Update Usertoken
        api_response = api_instance.update_usertoken_api_v1_secure_users_renew_put()
        print("The response of APIKeysApi->update_usertoken_api_v1_secure_users_renew_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->update_usertoken_api_v1_secure_users_renew_put: %s\n" % e)
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

