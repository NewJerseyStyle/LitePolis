# litepolis_client.CommentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comment_api_v1_secure_comments_post**](CommentsApi.md#create_comment_api_v1_secure_comments_post) | **POST** /api/v1/secure/comments/ | Create Comment
[**delete_comment_api_v1_secure_comments_cid_delete**](CommentsApi.md#delete_comment_api_v1_secure_comments_cid_delete) | **DELETE** /api/v1/secure/comments/{cid} | Delete Comment
[**get_comments_api_v1_secure_comments_cid_get**](CommentsApi.md#get_comments_api_v1_secure_comments_cid_get) | **GET** /api/v1/secure/comments/{cid}/ | Get Comments
[**get_comments_for_moderation_api_v1_secure_comments_cid_moderate_get**](CommentsApi.md#get_comments_for_moderation_api_v1_secure_comments_cid_moderate_get) | **GET** /api/v1/secure/comments/{cid}/moderate | Get Comments For Moderation
[**update_comment_api_v1_secure_comments_put**](CommentsApi.md#update_comment_api_v1_secure_comments_put) | **PUT** /api/v1/secure/comments/ | Update Comment


# **create_comment_api_v1_secure_comments_post**
> object create_comment_api_v1_secure_comments_post(comment_model)

Create Comment

Create a new comment.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.comment_model import CommentModel
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
    api_instance = litepolis_client.CommentsApi(api_client)
    comment_model = litepolis_client.CommentModel() # CommentModel | 

    try:
        # Create Comment
        api_response = api_instance.create_comment_api_v1_secure_comments_post(comment_model)
        print("The response of CommentsApi->create_comment_api_v1_secure_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->create_comment_api_v1_secure_comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_model** | [**CommentModel**](CommentModel.md)|  | 

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

# **delete_comment_api_v1_secure_comments_cid_delete**
> object delete_comment_api_v1_secure_comments_cid_delete(cid)

Delete Comment

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
    api_instance = litepolis_client.CommentsApi(api_client)
    cid = 56 # int | 

    try:
        # Delete Comment
        api_response = api_instance.delete_comment_api_v1_secure_comments_cid_delete(cid)
        print("The response of CommentsApi->delete_comment_api_v1_secure_comments_cid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->delete_comment_api_v1_secure_comments_cid_delete: %s\n" % e)
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

# **get_comments_api_v1_secure_comments_cid_get**
> CommentResponse get_comments_api_v1_secure_comments_cid_get(cid, random=random, moderated=moderated)

Get Comments

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.comment_response import CommentResponse
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
    api_instance = litepolis_client.CommentsApi(api_client)
    cid = 56 # int | 
    random = True # bool |  (optional) (default to True)
    moderated = False # bool |  (optional) (default to False)

    try:
        # Get Comments
        api_response = api_instance.get_comments_api_v1_secure_comments_cid_get(cid, random=random, moderated=moderated)
        print("The response of CommentsApi->get_comments_api_v1_secure_comments_cid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->get_comments_api_v1_secure_comments_cid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**|  | 
 **random** | **bool**|  | [optional] [default to True]
 **moderated** | **bool**|  | [optional] [default to False]

### Return type

[**CommentResponse**](CommentResponse.md)

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

# **get_comments_for_moderation_api_v1_secure_comments_cid_moderate_get**
> CommentResponse get_comments_for_moderation_api_v1_secure_comments_cid_moderate_get(cid)

Get Comments For Moderation

Get comments waiting for moderation from a conversation.  Returns ------- dict     A dictionary containing comments waiting for moderation.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.comment_response import CommentResponse
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
    api_instance = litepolis_client.CommentsApi(api_client)
    cid = 56 # int | 

    try:
        # Get Comments For Moderation
        api_response = api_instance.get_comments_for_moderation_api_v1_secure_comments_cid_moderate_get(cid)
        print("The response of CommentsApi->get_comments_for_moderation_api_v1_secure_comments_cid_moderate_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->get_comments_for_moderation_api_v1_secure_comments_cid_moderate_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**|  | 

### Return type

[**CommentResponse**](CommentResponse.md)

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

# **update_comment_api_v1_secure_comments_put**
> object update_comment_api_v1_secure_comments_put(comment_model)

Update Comment

Update a comment.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import litepolis_client
from litepolis_client.models.comment_model import CommentModel
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
    api_instance = litepolis_client.CommentsApi(api_client)
    comment_model = litepolis_client.CommentModel() # CommentModel | 

    try:
        # Update Comment
        api_response = api_instance.update_comment_api_v1_secure_comments_put(comment_model)
        print("The response of CommentsApi->update_comment_api_v1_secure_comments_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->update_comment_api_v1_secure_comments_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_model** | [**CommentModel**](CommentModel.md)|  | 

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

