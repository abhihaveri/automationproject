## HTTP status code verification

def verify_http_status_code(responsne_data,expect_data):
    assert responsne_data.status_code == expect_data,"Expected HTTP Status code is "+str(expect_data)

def verify_json_key_for_not_null(key):
    assert key !=0, "key should be non empty"+str(key)
    assert key>0,"key is should be greater than zero"+str(key)

def verify_response_none(key):
    assert key is not None

def verify_response_time():
    pass


# Common Verification 
# HTTP Status Code
# Headers
# Data verification 
# JSON schema
