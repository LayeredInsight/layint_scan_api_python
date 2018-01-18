# PolicyRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sid** | **str** | ID for this rule | [optional] 
**parent_sid** | **str** | ID of owner of this rule | [optional] 
**uri** | **str** |  | [optional] 
**date_created** | **str** | Timestamp representing date scan was run | [optional] 
**date_updated** | **str** | Timestamp representing date this record was updated | [optional] 
**name** | **str** | Name of this rule | [optional] 
**type** | **str** | Specifies if this is a Vulnerability or Package rule | [optional] 
**vulnerability_type** | **str** | For Vulnerability rules, specifies severity | [optional] 
**package** | **str** | For Package rules, specifies package name | [optional] 
**package_version** | **str** | For Package rules, specifies version number to be compared in this rule | [optional] 
**package_version_operator** | **str** | For Package rules, specifies if version of package in image should be less than, equal to, or greater than version in PackageVersion parameter. | [optional] 
**action** | **str** | Action to take if this rule matches | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


