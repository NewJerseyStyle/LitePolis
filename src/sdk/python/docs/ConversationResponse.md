# ConversationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**Detail1**](Detail1.md) |  | 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] [default to 200]

## Example

```python
from litepolis_client.models.conversation_response import ConversationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationResponse from a JSON string
conversation_response_instance = ConversationResponse.from_json(json)
# print the JSON string representation of the object
print(ConversationResponse.to_json())

# convert the object into a dict
conversation_response_dict = conversation_response_instance.to_dict()
# create an instance of ConversationResponse from a dict
conversation_response_from_dict = ConversationResponse.from_dict(conversation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


