# .CommentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCommentApiV1SecureCommentsPost**](CommentsApi.md#createCommentApiV1SecureCommentsPost) | **POST** /api/v1/secure/comments/ | Create Comment
[**deleteCommentApiV1SecureCommentsCidDelete**](CommentsApi.md#deleteCommentApiV1SecureCommentsCidDelete) | **DELETE** /api/v1/secure/comments/{cid} | Delete Comment
[**getCommentsApiV1SecureCommentsCidGet**](CommentsApi.md#getCommentsApiV1SecureCommentsCidGet) | **GET** /api/v1/secure/comments/{cid}/ | Get Comments
[**getCommentsForModerationApiV1SecureCommentsCidModerateGet**](CommentsApi.md#getCommentsForModerationApiV1SecureCommentsCidModerateGet) | **GET** /api/v1/secure/comments/{cid}/moderate | Get Comments For Moderation
[**updateCommentApiV1SecureCommentsPut**](CommentsApi.md#updateCommentApiV1SecureCommentsPut) | **PUT** /api/v1/secure/comments/ | Update Comment


# **createCommentApiV1SecureCommentsPost**
> any createCommentApiV1SecureCommentsPost(commentModel)

Create a new comment.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .CommentsApi(configuration);

let body:.CommentsApiCreateCommentApiV1SecureCommentsPostRequest = {
  // CommentModel
  commentModel: {
    commentId: 1,
    comment: "comment_example",
    userId: 1,
    conversationId: 1,
    task: "task_example",
    vote: 1,
  },
};

apiInstance.createCommentApiV1SecureCommentsPost(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commentModel** | **CommentModel**|  |


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

# **deleteCommentApiV1SecureCommentsCidDelete**
> any deleteCommentApiV1SecureCommentsCidDelete()


### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .CommentsApi(configuration);

let body:.CommentsApiDeleteCommentApiV1SecureCommentsCidDeleteRequest = {
  // number
  cid: 1,
};

apiInstance.deleteCommentApiV1SecureCommentsCidDelete(body).then((data:any) => {
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

# **getCommentsApiV1SecureCommentsCidGet**
> CommentResponse getCommentsApiV1SecureCommentsCidGet()


### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .CommentsApi(configuration);

let body:.CommentsApiGetCommentsApiV1SecureCommentsCidGetRequest = {
  // number
  cid: 1,
  // boolean (optional)
  random: true,
  // boolean (optional)
  moderated: false,
};

apiInstance.getCommentsApiV1SecureCommentsCidGet(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | [**number**] |  | defaults to undefined
 **random** | [**boolean**] |  | (optional) defaults to true
 **moderated** | [**boolean**] |  | (optional) defaults to false


### Return type

**CommentResponse**

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

# **getCommentsForModerationApiV1SecureCommentsCidModerateGet**
> CommentResponse getCommentsForModerationApiV1SecureCommentsCidModerateGet()

Get comments waiting for moderation from a conversation.  Returns ------- dict     A dictionary containing comments waiting for moderation.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .CommentsApi(configuration);

let body:.CommentsApiGetCommentsForModerationApiV1SecureCommentsCidModerateGetRequest = {
  // number
  cid: 1,
};

apiInstance.getCommentsForModerationApiV1SecureCommentsCidModerateGet(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | [**number**] |  | defaults to undefined


### Return type

**CommentResponse**

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

# **updateCommentApiV1SecureCommentsPut**
> any updateCommentApiV1SecureCommentsPut(commentModel)

Update a comment.

### Example


```typescript
import {  } from '';
import * as fs from 'fs';

const configuration = .createConfiguration();
const apiInstance = new .CommentsApi(configuration);

let body:.CommentsApiUpdateCommentApiV1SecureCommentsPutRequest = {
  // CommentModel
  commentModel: {
    commentId: 1,
    comment: "comment_example",
    userId: 1,
    conversationId: 1,
    task: "task_example",
    vote: 1,
  },
};

apiInstance.updateCommentApiV1SecureCommentsPut(body).then((data:any) => {
  console.log('API called successfully. Returned data: ' + data);
}).catch((error:any) => console.error(error));
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commentModel** | **CommentModel**|  |


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


