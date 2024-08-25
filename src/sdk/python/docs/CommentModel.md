# CommentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_id** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**conversation_id** | **int** |  | [optional] 
**task** | **str** |  | [optional] 
**vote** | **int** |  | [optional] 

## Example

```python
from litepolis_client.models.comment_model import CommentModel

# TODO update the JSON string below
json = "{}"
# create an instance of CommentModel from a JSON string
comment_model_instance = CommentModel.from_json(json)
# print the JSON string representation of the object
print(CommentModel.to_json())

# convert the object into a dict
comment_model_dict = comment_model_instance.to_dict()
# create an instance of CommentModel from a dict
comment_model_from_dict = CommentModel.from_dict(comment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


