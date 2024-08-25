# litepolis_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_testroute_api_v1_public_get**](DefaultApi.md#get_testroute_api_v1_public_get) | **GET** /api/v1/public/ | Get Testroute


# **get_testroute_api_v1_public_get**
> object get_testroute_api_v1_public_get()

Get Testroute

This endpoint is used to check if the database connection is healthy.  Returns ------- dict     A dictionary containing the status of the database connection.     - If the connection is healthy, the dictionary will contain     {\"detail\": \"OK\"}.     - If the connection is not healthy, the dictionary will contain     {\"detail\": \"DB conn failed\"}.

### Example


```python
import litepolis_client
from litepolis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = litepolis_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with litepolis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = litepolis_client.DefaultApi(api_client)

    try:
        # Get Testroute
        api_response = api_instance.get_testroute_api_v1_public_get()
        print("The response of DefaultApi->get_testroute_api_v1_public_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_testroute_api_v1_public_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

