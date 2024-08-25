# litepolis_client.ConversationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_conversation_api_v1_secure_conversations_post**](ConversationsApi.md#create_conversation_api_v1_secure_conversations_post) | **POST** /api/v1/secure/conversations | Create Conversation
[**delete_conversation_api_v1_secure_conversations_cid_delete**](ConversationsApi.md#delete_conversation_api_v1_secure_conversations_cid_delete) | **DELETE** /api/v1/secure/conversations/{cid} | Delete Conversation
[**get_all_conversations_api_v1_secure_conversations_all_get**](ConversationsApi.md#get_all_conversations_api_v1_secure_conversations_all_get) | **GET** /api/v1/secure/conversations/all | Get All Conversations
[**get_conversation_api_v1_secure_conversations_cid_get**](ConversationsApi.md#get_conversation_api_v1_secure_conversations_cid_get) | **GET** /api/v1/secure/conversations/{cid} | Get Conversation
[**update_conversation_api_v1_secure_conversations_put**](ConversationsApi.md#update_conversation_api_v1_secure_conversations_put) | **PUT** /api/v1/secure/conversations | Update Conversation


# **create_conversation_api_v1_secure_conversations_post**
> object create_conversation_api_v1_secure_conversations_post(conversation_model)

Create Conversation

Create a new conversation.  Parameters ---------- create_conversation : ConversationModel     Conversation information to create. user : dict     Authenticated user information.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.conversation_model import ConversationModel
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
    api_instance = litepolis_client.ConversationsApi(api_client)
    conversation_model = litepolis_client.ConversationModel() # ConversationModel | 

    try:
        # Create Conversation
        api_response = api_instance.create_conversation_api_v1_secure_conversations_post(conversation_model)
        print("The response of ConversationsApi->create_conversation_api_v1_secure_conversations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->create_conversation_api_v1_secure_conversations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_model** | [**ConversationModel**](ConversationModel.md)|  | 

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

# **delete_conversation_api_v1_secure_conversations_cid_delete**
> object delete_conversation_api_v1_secure_conversations_cid_delete(cid)

Delete Conversation

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
    api_instance = litepolis_client.ConversationsApi(api_client)
    cid = 56 # int | 

    try:
        # Delete Conversation
        api_response = api_instance.delete_conversation_api_v1_secure_conversations_cid_delete(cid)
        print("The response of ConversationsApi->delete_conversation_api_v1_secure_conversations_cid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->delete_conversation_api_v1_secure_conversations_cid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_conversations_api_v1_secure_conversations_all_get**
> ConversationResponse get_all_conversations_api_v1_secure_conversations_all_get()

Get All Conversations

Get all conversations for the authenticated user.  Returns ------- dict     A dictionary containing all conversations for the user.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.conversation_response import ConversationResponse
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
    api_instance = litepolis_client.ConversationsApi(api_client)

    try:
        # Get All Conversations
        api_response = api_instance.get_all_conversations_api_v1_secure_conversations_all_get()
        print("The response of ConversationsApi->get_all_conversations_api_v1_secure_conversations_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->get_all_conversations_api_v1_secure_conversations_all_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ConversationResponse**](ConversationResponse.md)

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

# **get_conversation_api_v1_secure_conversations_cid_get**
> ResponseMessage get_conversation_api_v1_secure_conversations_cid_get(cid)

Get Conversation

Get a conversation by ID.  Returns ------- dict     A dictionary containing the conversation details.

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
    api_instance = litepolis_client.ConversationsApi(api_client)
    cid = 56 # int | 

    try:
        # Get Conversation
        api_response = api_instance.get_conversation_api_v1_secure_conversations_cid_get(cid)
        print("The response of ConversationsApi->get_conversation_api_v1_secure_conversations_cid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->get_conversation_api_v1_secure_conversations_cid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_conversation_api_v1_secure_conversations_put**
> object update_conversation_api_v1_secure_conversations_put(conversation_model)

Update Conversation

Update a conversation.  Parameters ---------- update_conversation : ConversationModel     Conversation update information. user : dict     Authenticated user information.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.conversation_model import ConversationModel
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
    api_instance = litepolis_client.ConversationsApi(api_client)
    conversation_model = litepolis_client.ConversationModel() # ConversationModel | 

    try:
        # Update Conversation
        api_response = api_instance.update_conversation_api_v1_secure_conversations_put(conversation_model)
        print("The response of ConversationsApi->update_conversation_api_v1_secure_conversations_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->update_conversation_api_v1_secure_conversations_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_model** | [**ConversationModel**](ConversationModel.md)|  | 

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

