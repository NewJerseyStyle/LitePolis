# .UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUserprofileApiV1SecureUsersProfilePost**](UserApi.md#createUserprofileApiV1SecureUsersProfilePost) | **POST** /api/v1/secure/users/profile | Create Userprofile
[**deleteUserprofileApiV1SecureUsersProfileDelete**](UserApi.md#deleteUserprofileApiV1SecureUsersProfileDelete) | **DELETE** /api/v1/secure/users/profile | Delete Userprofile
[**getTestrouteApiV1SecureGet**](UserApi.md#getTestrouteApiV1SecureGet) | **GET** /api/v1/secure/ | Get Testroute
[**getUserauthApiV1SecureUsersAuthPost**](UserApi.md#getUserauthApiV1SecureUsersAuthPost) | **POST** /api/v1/secure/users/auth | Get Userauth
[**getUserprofileApiV1SecureUsersProfileGet**](UserApi.md#getUserprofileApiV1SecureUsersProfileGet) | **GET** /api/v1/secure/users/profile | Get Userprofile
[**getUserroleApiV1SecureUsersRoleGet**](UserApi.md#getUserroleApiV1SecureUsersRoleGet) | **GET** /api/v1/secure/users/role | Get Userrole
[**updateUserprofileApiV1SecureUsersProfilePut**](UserApi.md#updateUserprofileApiV1SecureUsersProfilePut) | **PUT** /api/v1/secure/users/profile | Update Userprofile
[**updateUsertokenApiV1SecureUsersRenewPut**](UserApi.md#updateUsertokenApiV1SecureUsersRenewPut) | **PUT** /api/v1/secure/users/renew | Update Usertoken


# **createUserprofileApiV1SecureUsersProfilePost**
> ResponseMessage createUserprofileApiV1SecureUsersProfilePost(userProfile)

Create a new user profile.  Parameters ---------- user_profile : UserProfile     User profile information. user : dict     Authenticated user information.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .UserApi(configuration);

let body:.UserApiCreateUserprofileApiV1SecureUsersProfilePostRequest = {
  // UserProfile
  userProfile: {
    email: "email_example",
    password: "password_example",
  },
};

apiInstance.createUserprofileApiV1SecureUsersProfilePost(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userProfile** | **UserProfile**|  |


### Return type

**ResponseMessage**

### Authorization

[APIKeyHeader](README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **deleteUserprofileApiV1SecureUsersProfileDelete**
> any deleteUserprofileApiV1SecureUsersProfileDelete()


### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .UserApi(configuration);

let body:any = {};

apiInstance.deleteUserprofileApiV1SecureUsersProfileDelete(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters
This endpoint does not need any parameter.


### Return type

**any**

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

# **getTestrouteApiV1SecureGet**
> ResponseMessage getTestrouteApiV1SecureGet()

This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .UserApi(configuration);

let body:any = {};

apiInstance.getTestrouteApiV1SecureGet(body).then((data:any) => {
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

# **getUserauthApiV1SecureUsersAuthPost**
> ResponseMessage getUserauthApiV1SecureUsersAuthPost(userProfile)


### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .UserApi(configuration);

let body:.UserApiGetUserauthApiV1SecureUsersAuthPostRequest = {
  // UserProfile
  userProfile: {
    email: "email_example",
    password: "password_example",
  },
};

apiInstance.getUserauthApiV1SecureUsersAuthPost(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userProfile** | **UserProfile**|  |


### Return type

**ResponseMessage**

### Authorization

[APIKeyHeader](README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **getUserprofileApiV1SecureUsersProfileGet**
> ResponseMessage getUserprofileApiV1SecureUsersProfileGet()

This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .UserApi(configuration);

let body:any = {};

apiInstance.getUserprofileApiV1SecureUsersProfileGet(body).then((data:any) => {
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

# **getUserroleApiV1SecureUsersRoleGet**
> ResponseMessage getUserroleApiV1SecureUsersRoleGet()

This endpoint returns the role of the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }  Returns ------- ResponseMessage     `detail` string of the user\'s role.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .UserApi(configuration);

let body:any = {};

apiInstance.getUserroleApiV1SecureUsersRoleGet(body).then((data:any) => {
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

# **updateUserprofileApiV1SecureUsersProfilePut**
> any updateUserprofileApiV1SecureUsersProfilePut(userProfile)

Update the authenticated user\'s profile.  Parameters ---------- update_user : UpdateUserProfile     User profile information to update. user : dict     Authenticated user information.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .UserApi(configuration);

let body:.UserApiUpdateUserprofileApiV1SecureUsersProfilePutRequest = {
  // UserProfile
  userProfile: {
    email: "email_example",
    password: "password_example",
  },
};

apiInstance.updateUserprofileApiV1SecureUsersProfilePut(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userProfile** | **UserProfile**|  |


### Return type

**any**

### Authorization

[APIKeyHeader](README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **updateUsertokenApiV1SecureUsersRenewPut**
> ResponseMessage updateUsertokenApiV1SecureUsersRenewPut()

Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .UserApi(configuration);

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


