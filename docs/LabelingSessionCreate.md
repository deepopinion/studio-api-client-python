# LabelingSessionCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto** | **bool** | If auto is set to true, the documents will be analyzed if they contain attributes that match with tags. If this is the case, they are automatically inferred and annotated by the system | [optional] 
**classes** | **list[str]** | Classes contained in that session. If not given, project classes will be used | [optional] 
**document_ids** | **list[int]** | IDs of already available documents that should be annotated | [optional] 
**documents** | [**list[LabelledDocument]**](LabelledDocument.md) | The documents that should be used for this annotation session | [optional] 
**labels** | **list[str]** | Labels contained in that session. If not given, project labels will be used | [optional] 
**name** | **str** | Name of the labeling session | [optional] 
**sample_size** | **int** | Sample size | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


