# .APIKeysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateUsertokenApiV1SecureUsersRenewPut**](APIKeysApi.md#updateUsertokenApiV1SecureUsersRenewPut) | **PUT** /api/v1/secure/users/renew | Update Usertoken


# **updateUsertokenApiV1SecureUsersRenewPut**
> ResponseMessage updateUsertokenApiV1SecureUsersRenewPut()

Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .APIKeysApi(configuration);

let body:any = {};

apiInstance.updateUsertokenApiV1SecureUsersRenewPut(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters
This endpoint does not need any parameter.


### Return type

**ResponseMessage**

### Authorization

[APIKeyHeader](README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)


