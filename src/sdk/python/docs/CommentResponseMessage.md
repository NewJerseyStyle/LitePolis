# CommentResponseMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**create_date** | **str** |  | 
**comment** | **str** |  | 
**user_id** | **int** |  | 
**conversation_id** | **int** |  | 
**moderated** | **bool** |  | [optional] [default to False]
**approved** | **bool** |  | [optional] [default to False]

## Example

```python
from litepolis_client.models.comment_response_message import CommentResponseMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CommentResponseMessage from a JSON string
comment_response_message_instance = CommentResponseMessage.from_json(json)
# print the JSON string representation of the object
print(CommentResponseMessage.to_json())

# convert the object into a dict
comment_response_message_dict = comment_response_message_instance.to_dict()
# create an instance of CommentResponseMessage from a dict
comment_response_message_from_dict = CommentResponseMessage.from_dict(comment_response_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


