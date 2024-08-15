from src.helpers.api_requests_wrappers import post_request
from src.constants.api_constants import APIconstants 
from src.helpers.utils import common_headers_json
from src.helpers.payloadmanger import payload_create_booking
from src.helpers.common_verification import verify_http_status_code,verify_json_key_for_not_null,verify_response_none

import pytest


class Testcreateboking(object):
    @pytest.mark.positive
    def test_create_booking_tc1(self):
        #url , Headers, payload
        response=post_request(url=APIconstants().url_create_booking()
                              ,auth=None,headers=common_headers_json(),
                              payload=payload_create_booking(),in_json=False)
        verify_json_key_for_not_null(response.json()["bookingid"])
        verify_http_status_code(response,200)
        print(response.json())
        print('The reponse is' ,response)
        bookingid= response.json()["bookingid"]
        print('The bookingid is',bookingid)

        
    @pytest.mark.negative
    def test_create_booking_tc2(self):
        #url , Headers, payload
        response=post_request(url=APIconstants().url_create_booking(),
                              auth=None,headers=common_headers_json(),payload={},in_json=False)
        verify_http_status_code(response,500)
        print('\nThe response is',response)

    
