# Image

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** | name of container image | [optional] 
**image_url** | **str** | URL to registry store location of image | [optional] 
**uri** | **str** | Relative URI to this image within the Scan API | [optional] 
**sid** | **str** | Unique ID of image in Scan | [optional] 
**parent_sid** | **str** | User id of owner of this object | [optional] 
**registry** | **str** | registry hostname | [optional] 
**status** | **str** | Current status of the scan of this image | [optional] 
**events** | **list[str]** | a list of events that have occurred on this image. Could be considered a log of the scan process. | [optional] 
**sha_sum** | **str** | Sha256 checksum for the image | [optional] 
**layers** | **list[str]** | A list of checksums for each discovered layer in the image | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


