from src.helpers.api_requests_wrappers import post_request,put_request,delete_request
from src.constants.api_constants import APIconstants 
from src.helpers.utils import common_headers_json,token_creator
from src.helpers.payloadmanger import payload_create_booking,payload_create_token,payload_update_booking
from src.helpers.common_verification import verify_http_status_code,verify_json_key_for_not_null,verify_response_none

import pytest

class Testcreateboking(object):

    @pytest.fixture(scope="class")
    def create_token(self):
        response=post_request(url=APIconstants().url_create_auth(),
        auth=None,headers=common_headers_json(),payload=payload_create_token(),in_json=False)
        token=(response.json()["token"]) 
        print('The Generated Token',token)
        verify_http_status_code(response,200)
        verify_response_none(token)
        return token 
        
    @pytest.fixture(scope="class") 
    def create_booking(self):
        response=post_request(url=APIconstants().url_create_booking(),auth=None,
                                headers=common_headers_json(),payload=payload_create_booking(),in_json=False)
        verify_json_key_for_not_null(response.json()["bookingid"])
        verify_http_status_code(response,200)
        print("The New jason body is \n",response.json())
        print('The reponse is' ,response)
        bookingid= response.json()["bookingid"]
        print('The New bookingid is',bookingid)
        return bookingid

    def test_update_booking(self, create_token, create_booking): # token and booking id from create booking  & token call 
        #bookingid=Testcreateboking().create_booking()
        finalurl=APIconstants().url_PATCH_PUT_DELETE_Booking(create_booking)
        #token=Testcreateboking().create_token()
        response=put_request(url=finalurl,
                            auth=None,headers=token_creator(create_token),
                            payload=payload_update_booking(),in_json=False)
        verify_http_status_code(response,200)
        verify_response_none(create_token)
        print('The updated booking id',create_booking)
        print("The Updated jason body is \n",response.json())
     

    def test_delete_booking(self, create_token, create_booking): # token and booking id from create booking  & token call 
        #bookingid=Testcreateboking().create_booking()
        finalurl=APIconstants().url_PATCH_PUT_DELETE_Booking(create_booking)
        #token=Testcreateboking().create_token()
        response=delete_request(url=finalurl,
                            auth=None,headers=token_creator(create_token),in_json=False)
        print('The deleted booking id',create_booking)
        print('The response code after deletion',response.status_code)

