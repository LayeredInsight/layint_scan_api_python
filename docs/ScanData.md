# ScanData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sid** | **str** | Internal ID of this scan | [optional] 
**parent_sid** | **str** | Internal ID of image that was scanned | [optional] 
**user_sid** | **str** | ID of image owner | [optional] 
**uri** | **str** | a | [optional] 
**image_id** | **str** | Docker image ID | [optional] 
**date_created** | **str** | Timestamp representing date scan was run | [optional] 
**date_updated** | **str** | Timestamp representing date this record was updated | [optional] 
**status** | **str** | Status of scan | [optional] 
**events** | **list[str]** | Log of events that occurred (or are occurring) during scan | [optional] 
**clair** | [**list[ClairData]**](ClairData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


