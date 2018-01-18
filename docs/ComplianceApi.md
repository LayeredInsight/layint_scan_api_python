# layint_scan_api.ComplianceApi

All URIs are relative to *https://scan-api.layeredinsight.com/V0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_policy**](ComplianceApi.md#add_policy) | **POST** /Policies | Add a new policy
[**add_policy_rule**](ComplianceApi.md#add_policy_rule) | **POST** /Rules | Add a new policy rule
[**delete_policy**](ComplianceApi.md#delete_policy) | **DELETE** /Policies/{policyID} | Delete compliance policy
[**delete_policy_rule**](ComplianceApi.md#delete_policy_rule) | **DELETE** /Rules/{ruleID} | Delete compliance policy rule
[**get_policies**](ComplianceApi.md#get_policies) | **GET** /Policies | List all compliance policies available to the user
[**get_policy**](ComplianceApi.md#get_policy) | **GET** /Policies/{policyID} | Get compliance policy
[**get_policy_rule**](ComplianceApi.md#get_policy_rule) | **GET** /Rules/{ruleID} | Get compliance policy rule
[**get_policy_rules**](ComplianceApi.md#get_policy_rules) | **GET** /Rules | List all compliance rules available to the user
[**update_policy**](ComplianceApi.md#update_policy) | **POST** /Policies/{policyID} | Update policy
[**update_policy_rule**](ComplianceApi.md#update_policy_rule) | **POST** /Rules/{ruleID} | Update policy rule


# **add_policy**
> Policies add_policy(policy)

Add a new policy

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
api_instance = layint_scan_api.ComplianceApi()
policy = layint_scan_api.Policies() # Policies | One or more policies to be added

try: 
    # Add a new policy
    api_response = api_instance.add_policy(policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->add_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**Policies**](Policies.md)| One or more policies to be added | 

### Return type

[**Policies**](Policies.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_policy_rule**
> PolicyRules add_policy_rule(policy_rules)

Add a new policy rule

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
api_instance = layint_scan_api.ComplianceApi()
policy_rules = layint_scan_api.PolicyRules() # PolicyRules | One or more policy rules to be added

try: 
    # Add a new policy rule
    api_response = api_instance.add_policy_rule(policy_rules)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->add_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_rules** | [**PolicyRules**](PolicyRules.md)| One or more policy rules to be added | 

### Return type

[**PolicyRules**](PolicyRules.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(policy_id)

Delete compliance policy

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
api_instance = layint_scan_api.ComplianceApi()
policy_id = 'policy_id_example' # str | ID of policy to delete

try: 
    # Delete compliance policy
    api_instance.delete_policy(policy_id)
except ApiException as e:
    print("Exception when calling ComplianceApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| ID of policy to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_rule**
> delete_policy_rule(rule_id)

Delete compliance policy rule

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
api_instance = layint_scan_api.ComplianceApi()
rule_id = 'rule_id_example' # str | ID of policy rule to delete

try: 
    # Delete compliance policy rule
    api_instance.delete_policy_rule(rule_id)
except ApiException as e:
    print("Exception when calling ComplianceApi->delete_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| ID of policy rule to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies**
> Policies get_policies()

List all compliance policies available to the user

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
api_instance = layint_scan_api.ComplianceApi()

try: 
    # List all compliance policies available to the user
    api_response = api_instance.get_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->get_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Policies**](Policies.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> Policy get_policy(policy_id)

Get compliance policy

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
api_instance = layint_scan_api.ComplianceApi()
policy_id = 'policy_id_example' # str | ID of policy to get

try: 
    # Get compliance policy
    api_response = api_instance.get_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| ID of policy to get | 

### Return type

[**Policy**](Policy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_rule**
> PolicyRule get_policy_rule(rule_id)

Get compliance policy rule

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
api_instance = layint_scan_api.ComplianceApi()
rule_id = 'rule_id_example' # str | ID of policy rule to get

try: 
    # Get compliance policy rule
    api_response = api_instance.get_policy_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->get_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| ID of policy rule to get | 

### Return type

[**PolicyRule**](PolicyRule.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_rules**
> PolicyRules get_policy_rules()

List all compliance rules available to the user

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
api_instance = layint_scan_api.ComplianceApi()

try: 
    # List all compliance rules available to the user
    api_response = api_instance.get_policy_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->get_policy_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PolicyRules**](PolicyRules.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> Policy update_policy(policy_id, policy)

Update policy

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
api_instance = layint_scan_api.ComplianceApi()
policy_id = 'policy_id_example' # str | ID of policy to get
policy = layint_scan_api.Policy() # Policy | Data to update policy with

try: 
    # Update policy
    api_response = api_instance.update_policy(policy_id, policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| ID of policy to get | 
 **policy** | [**Policy**](Policy.md)| Data to update policy with | 

### Return type

[**Policy**](Policy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_rule**
> PolicyRule update_policy_rule(rule_id, policy_rule)

Update policy rule

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
api_instance = layint_scan_api.ComplianceApi()
rule_id = 'rule_id_example' # str | ID of policy rule to update
policy_rule = layint_scan_api.PolicyRule() # PolicyRule | Data to update policy rule with

try: 
    # Update policy rule
    api_response = api_instance.update_policy_rule(rule_id, policy_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->update_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| ID of policy rule to update | 
 **policy_rule** | [**PolicyRule**](PolicyRule.md)| Data to update policy rule with | 

### Return type

[**PolicyRule**](PolicyRule.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

