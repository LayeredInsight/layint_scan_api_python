# layint_scan_api.ImagesApi

All URIs are relative to *https://scan-api.layeredinsight.com/V0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_image**](ImagesApi.md#add_image) | **POST** /Images | Submit an image name for scanning
[**delete_image**](ImagesApi.md#delete_image) | **DELETE** /Images/{imageID} | Delete specified image
[**get_image**](ImagesApi.md#get_image) | **GET** /Images/{imageID} | Get image details
[**get_image_compliance**](ImagesApi.md#get_image_compliance) | **GET** /Images/{imageID}/Compliance | Get compliance report for specified image
[**get_image_scan**](ImagesApi.md#get_image_scan) | **GET** /Images/{imageID}/Scans/{scanID} | Get scan data for specific scan for specified image
[**get_image_scans**](ImagesApi.md#get_image_scans) | **GET** /Images/{imageID}/Scans | Get all scan data for specified image
[**get_images**](ImagesApi.md#get_images) | **GET** /Images | Get list of scanned images
[**is_image_compliant**](ImagesApi.md#is_image_compliant) | **GET** /Images/{imageID}/IsCompliant | Determines if specified image is in compliance with policies applied to image


# **add_image**
> Image add_image(image_name)

Submit an image name for scanning

### Example 
```python
from __future__ import print_function
import time
import layint_scan_api
from layint_scan_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_scan_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_scan_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_scan_api.ImagesApi()
image_name = layint_scan_api.ImageName() # ImageName | 

try: 
    # Submit an image name for scanning
    api_response = api_instance.add_image(image_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->add_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_name** | [**ImageName**](ImageName.md)|  | 

### Return type

[**Image**](Image.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image**
> delete_image(image_id)

Delete specified image

### Example 
```python
from __future__ import print_function
import time
import layint_scan_api
from layint_scan_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_scan_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_scan_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_scan_api.ImagesApi()
image_id = 'image_id_example' # str | ImageID to delete

try: 
    # Delete specified image
    api_instance.delete_image(image_id)
except ApiException as e:
    print("Exception when calling ImagesApi->delete_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| ImageID to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image**
> Image get_image(image_id)

Get image details

### Example 
```python
from __future__ import print_function
import time
import layint_scan_api
from layint_scan_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_scan_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_scan_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_scan_api.ImagesApi()
image_id = 'image_id_example' # str | ImageID to get details for

try: 
    # Get image details
    api_response = api_instance.get_image(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| ImageID to get details for | 

### Return type

[**Image**](Image.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_compliance**
> Compliances get_image_compliance(image_id, run=run, policies=policies)

Get compliance report for specified image

### Example 
```python
from __future__ import print_function
import time
import layint_scan_api
from layint_scan_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_scan_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_scan_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_scan_api.ImagesApi()
image_id = 'image_id_example' # str | ImageID to get license data for
run = false # bool | If true, requests running compliance policies specified in \"policies\" parameter (optional) (default to false)
policies = 'policies_example' # str | Comma-separated list of compliance policies to run for this image (optional)

try: 
    # Get compliance report for specified image
    api_response = api_instance.get_image_compliance(image_id, run=run, policies=policies)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_compliance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| ImageID to get license data for | 
 **run** | **bool**| If true, requests running compliance policies specified in \&quot;policies\&quot; parameter | [optional] [default to false]
 **policies** | **str**| Comma-separated list of compliance policies to run for this image | [optional] 

### Return type

[**Compliances**](Compliances.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_scan**
> ScanData get_image_scan(image_id, scan_id)

Get scan data for specific scan for specified image

### Example 
```python
from __future__ import print_function
import time
import layint_scan_api
from layint_scan_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_scan_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_scan_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_scan_api.ImagesApi()
image_id = 'image_id_example' # str | ImageID to get scan data for
scan_id = 'scan_id_example' # str | ID of scan to get data for

try: 
    # Get scan data for specific scan for specified image
    api_response = api_instance.get_image_scan(image_id, scan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| ImageID to get scan data for | 
 **scan_id** | **str**| ID of scan to get data for | 

### Return type

[**ScanData**](ScanData.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_scans**
> ScanDatas get_image_scans(image_id)

Get all scan data for specified image

### Example 
```python
from __future__ import print_function
import time
import layint_scan_api
from layint_scan_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_scan_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_scan_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_scan_api.ImagesApi()
image_id = 'image_id_example' # str | ImageID to get scan data for

try: 
    # Get all scan data for specified image
    api_response = api_instance.get_image_scans(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_scans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| ImageID to get scan data for | 

### Return type

[**ScanDatas**](ScanDatas.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> Images get_images(tags=tags)

Get list of scanned images

### Example 
```python
from __future__ import print_function
import time
import layint_scan_api
from layint_scan_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_scan_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_scan_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_scan_api.ImagesApi()
tags = layint_scan_api.TagNames() # TagNames | Tag name(s) to filter results (optional)

try: 
    # Get list of scanned images
    api_response = api_instance.get_images(tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**TagNames**](TagNames.md)| Tag name(s) to filter results | [optional] 

### Return type

[**Images**](Images.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_image_compliant**
> ComplianceResult is_image_compliant(image_id)

Determines if specified image is in compliance with policies applied to image

### Example 
```python
from __future__ import print_function
import time
import layint_scan_api
from layint_scan_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_scan_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_scan_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_scan_api.ImagesApi()
image_id = 'image_id_example' # str | ImageID to check compliance of

try: 
    # Determines if specified image is in compliance with policies applied to image
    api_response = api_instance.is_image_compliant(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->is_image_compliant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| ImageID to check compliance of | 

### Return type

[**ComplianceResult**](ComplianceResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

