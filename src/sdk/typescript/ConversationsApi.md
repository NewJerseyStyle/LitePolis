# .ConversationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createConversationApiV1SecureConversationsPost**](ConversationsApi.md#createConversationApiV1SecureConversationsPost) | **POST** /api/v1/secure/conversations | Create Conversation
[**deleteConversationApiV1SecureConversationsCidDelete**](ConversationsApi.md#deleteConversationApiV1SecureConversationsCidDelete) | **DELETE** /api/v1/secure/conversations/{cid} | Delete Conversation
[**getAllConversationsApiV1SecureConversationsAllGet**](ConversationsApi.md#getAllConversationsApiV1SecureConversationsAllGet) | **GET** /api/v1/secure/conversations/all | Get All Conversations
[**getConversationApiV1SecureConversationsCidGet**](ConversationsApi.md#getConversationApiV1SecureConversationsCidGet) | **GET** /api/v1/secure/conversations/{cid} | Get Conversation
[**updateConversationApiV1SecureConversationsPut**](ConversationsApi.md#updateConversationApiV1SecureConversationsPut) | **PUT** /api/v1/secure/conversations | Update Conversation


# **createConversationApiV1SecureConversationsPost**
> any createConversationApiV1SecureConversationsPost(conversationModel)

Create a new conversation.  Parameters ---------- create_conversation : ConversationModel     Conversation information to create. user : dict     Authenticated user information.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .ConversationsApi(configuration);

let body:.ConversationsApiCreateConversationApiV1SecureConversationsPostRequest = {
  // ConversationModel
  conversationModel: {
    id: 1,
    title: "title_example",
    description: "description_example",
  },
};

apiInstance.createConversationApiV1SecureConversationsPost(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversationModel** | **ConversationModel**|  |


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

# **deleteConversationApiV1SecureConversationsCidDelete**
> any deleteConversationApiV1SecureConversationsCidDelete()


### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .ConversationsApi(configuration);

let body:.ConversationsApiDeleteConversationApiV1SecureConversationsCidDeleteRequest = {
  // number
  cid: 1,
};

apiInstance.deleteConversationApiV1SecureConversationsCidDelete(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | [**number**] |  | defaults to undefined


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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **getAllConversationsApiV1SecureConversationsAllGet**
> ConversationResponse getAllConversationsApiV1SecureConversationsAllGet()

Get all conversations for the authenticated user.  Returns ------- dict     A dictionary containing all conversations for the user.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .ConversationsApi(configuration);

let body:any = {};

apiInstance.getAllConversationsApiV1SecureConversationsAllGet(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters
This endpoint does not need any parameter.


### Return type

**ConversationResponse**

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

# **getConversationApiV1SecureConversationsCidGet**
> ResponseMessage getConversationApiV1SecureConversationsCidGet()

Get a conversation by ID.  Returns ------- dict     A dictionary containing the conversation details.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .ConversationsApi(configuration);

let body:.ConversationsApiGetConversationApiV1SecureConversationsCidGetRequest = {
  // number
  cid: 1,
};

apiInstance.getConversationApiV1SecureConversationsCidGet(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | [**number**] |  | defaults to undefined


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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **updateConversationApiV1SecureConversationsPut**
> any updateConversationApiV1SecureConversationsPut(conversationModel)

Update a conversation.  Parameters ---------- update_conversation : ConversationModel     Conversation update information. user : dict     Authenticated user information.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .ConversationsApi(configuration);

let body:.ConversationsApiUpdateConversationApiV1SecureConversationsPutRequest = {
  // ConversationModel
  conversationModel: {
    id: 1,
    title: "title_example",
    description: "description_example",
  },
};

apiInstance.updateConversationApiV1SecureConversationsPut(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversationModel** | **ConversationModel**|  |


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


