# .DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTestrouteApiV1PublicGet**](DefaultApi.md#getTestrouteApiV1PublicGet) | **GET** /api/v1/public/ | Get Testroute


# **getTestrouteApiV1PublicGet**
> any getTestrouteApiV1PublicGet()

This endpoint is used to check if the database connection is healthy.  Returns ------- dict     A dictionary containing the status of the database connection.     - If the connection is healthy, the dictionary will contain     {\"detail\": \"OK\"}.     - If the connection is not healthy, the dictionary will contain     {\"detail\": \"DB conn failed\"}.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .DefaultApi(configuration);

let body:any = {};

apiInstance.getTestrouteApiV1PublicGet(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters
This endpoint does not need any parameter.


### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)


