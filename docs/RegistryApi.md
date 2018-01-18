# layint_scan_api.RegistryApi

All URIs are relative to *https://scan-api.layeredinsight.com/V0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_registry**](RegistryApi.md#add_registry) | **POST** /Registry | Add a new registry
[**delete_registry**](RegistryApi.md#delete_registry) | **DELETE** /Registry/{registryId} | Deletes a registry
[**get_registries**](RegistryApi.md#get_registries) | **GET** /Registry | List all registries available to the user
[**get_registry_by_id**](RegistryApi.md#get_registry_by_id) | **GET** /Registry/{registryId} | Find registry by ID
[**update_registry**](RegistryApi.md#update_registry) | **POST** /Registry/{registryId} | Updates a registry with form data


# **add_registry**
> Registry add_registry(registry)

Add a new registry

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
api_instance = layint_scan_api.RegistryApi()
registry = layint_scan_api.Registry() # Registry | Registry object to be added

try: 
    # Add a new registry
    api_response = api_instance.add_registry(registry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->add_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | [**Registry**](Registry.md)| Registry object to be added | 

### Return type

[**Registry**](Registry.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registry**
> delete_registry(registry_id)

Deletes a registry

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
api_instance = layint_scan_api.RegistryApi()
registry_id = 789 # int | Registry id to delete

try: 
    # Deletes a registry
    api_instance.delete_registry(registry_id)
except ApiException as e:
    print("Exception when calling RegistryApi->delete_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**| Registry id to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registries**
> Registries get_registries()

List all registries available to the user

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
api_instance = layint_scan_api.RegistryApi()

try: 
    # List all registries available to the user
    api_response = api_instance.get_registries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_registries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Registries**](Registries.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry_by_id**
> Registry get_registry_by_id(registry_id)

Find registry by ID

Returns a single registry

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
api_instance = layint_scan_api.RegistryApi()
registry_id = 789 # int | ID of registry to return

try: 
    # Find registry by ID
    api_response = api_instance.get_registry_by_id(registry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_registry_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**| ID of registry to return | 

### Return type

[**Registry**](Registry.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_registry**
> Registry update_registry(registry_id, name=name, url=url)

Updates a registry with form data

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
api_instance = layint_scan_api.RegistryApi()
registry_id = 789 # int | ID of registry that needs to be updated
name = 'name_example' # str | Updated name of the registry (optional)
url = 'url_example' # str | Updated URL for the registry (optional)

try: 
    # Updates a registry with form data
    api_response = api_instance.update_registry(registry_id, name=name, url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->update_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**| ID of registry that needs to be updated | 
 **name** | **str**| Updated name of the registry | [optional] 
 **url** | **str**| Updated URL for the registry | [optional] 

### Return type

[**Registry**](Registry.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

