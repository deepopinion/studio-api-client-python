# DetailedModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** | the name of the model used to create the modal that&#39;s being changed | [optional] 
**classes** | **list[str]** | All classes that belong to the project | [optional] 
**created** | **datetime** | creation date | [optional] 
**demoset** | [**list[LabelledDocument]**](LabelledDocument.md) | A list of documents to be used to demo a model | [optional] 
**display_name** | **str** | a friendly name. | [optional] 
**id** | **int** | The ID of the model | [optional] 
**labels** | **list[str]** | All labels that belong to the project | [optional] 
**language** | **str** | Language of the model | [optional] 
**long_description** | **str** | a longer description which proper describes the model | [optional] 
**metrics** | **object** | The metrics associated to the model | [optional] 
**name** | **str** | internal name. It should be unique for a workspace | [optional] 
**owner** | **str** |  | [optional] 
**progress** | **float** |  | [optional] 
**project_id** | **int** | The ID of the project | [optional] 
**score** | **float** | model score. As this is a result of a training session, this value shouldn&#39;t be touched | [optional] 
**short_description** | **str** | a short description to help users quickly identify the model | [optional] 
**status** | **str** | the model status | [optional] 
**type** | **str** | model type (1: BASE, 2: ABSA, 3: LABEL, 4: CLASS, 5: CLASSLABEL)) | [optional] 
**uuid** | **str** | model unique identifier. Should be a UUID value | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


