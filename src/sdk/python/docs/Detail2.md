# Detail2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**email** | **str** |  | 
**role** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**creator_id** | **int** |  | 
**moderation** | **bool** |  | [optional] 
**create_date** | **str** |  | 
**comment** | **str** |  | 
**user_id** | **int** |  | 
**conversation_id** | **int** |  | 
**moderated** | **bool** |  | [optional] [default to False]
**approved** | **bool** |  | [optional] [default to False]

## Example

```python
from litepolis_client.models.detail2 import Detail2

# TODO update the JSON string below
json = "{}"
# create an instance of Detail2 from a JSON string
detail2_instance = Detail2.from_json(json)
# print the JSON string representation of the object
print(Detail2.to_json())

# convert the object into a dict
detail2_dict = detail2_instance.to_dict()
# create an instance of Detail2 from a dict
detail2_from_dict = Detail2.from_dict(detail2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


