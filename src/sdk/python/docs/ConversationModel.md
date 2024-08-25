# ConversationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from litepolis_client.models.conversation_model import ConversationModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationModel from a JSON string
conversation_model_instance = ConversationModel.from_json(json)
# print the JSON string representation of the object
print(ConversationModel.to_json())

# convert the object into a dict
conversation_model_dict = conversation_model_instance.to_dict()
# create an instance of ConversationModel from a dict
conversation_model_from_dict = ConversationModel.from_dict(conversation_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


