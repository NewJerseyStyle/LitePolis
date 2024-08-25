# UserResponseMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**email** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from litepolis_client.models.user_response_message import UserResponseMessage

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponseMessage from a JSON string
user_response_message_instance = UserResponseMessage.from_json(json)
# print the JSON string representation of the object
print(UserResponseMessage.to_json())

# convert the object into a dict
user_response_message_dict = user_response_message_instance.to_dict()
# create an instance of UserResponseMessage from a dict
user_response_message_from_dict = UserResponseMessage.from_dict(user_response_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


