# layint_scan_api.AuthenticationApi

All URIs are relative to *https://scan-api.layeredinsight.com/V0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthenticationApi.md#login) | **POST** /Login | Processes local login request
[**token_request**](AuthenticationApi.md#token_request) | **POST** /TokenRequest | Returns a session token for a oauth2 token


# **login**
> login(auth_request)

Processes local login request

### Example 
```python
from __future__ import print_function
import time
import layint_scan_api
from layint_scan_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = layint_scan_api.AuthenticationApi()
auth_request = layint_scan_api.LocalAuthRequest() # LocalAuthRequest | 

try: 
    # Processes local login request
    api_instance.login(auth_request)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_request** | [**LocalAuthRequest**](LocalAuthRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_request**
> TokenResponse token_request(token_request)

Returns a session token for a oauth2 token

### Example 
```python
from __future__ import print_function
import time
import layint_scan_api
from layint_scan_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = layint_scan_api.AuthenticationApi()
token_request = layint_scan_api.TokenRequest() # TokenRequest | Token request to convert to a session token

try: 
    # Returns a session token for a oauth2 token
    api_response = api_instance.token_request(token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->token_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request** | [**TokenRequest**](TokenRequest.md)| Token request to convert to a session token | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

