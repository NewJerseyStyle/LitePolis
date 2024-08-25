# ConversationResponseMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**creator_id** | **int** |  | 
**moderation** | **bool** |  | [optional] 

## Example

```python
from litepolis_client.models.conversation_response_message import ConversationResponseMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationResponseMessage from a JSON string
conversation_response_message_instance = ConversationResponseMessage.from_json(json)
# print the JSON string representation of the object
print(ConversationResponseMessage.to_json())

# convert the object into a dict
conversation_response_message_dict = conversation_response_message_instance.to_dict()
# create an instance of ConversationResponseMessage from a dict
conversation_response_message_from_dict = ConversationResponseMessage.from_dict(conversation_response_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


