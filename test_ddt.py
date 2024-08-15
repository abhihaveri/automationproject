# read the csv or excel file
# create a function create token which can take values from the excel file
# verify the Expected results

import pytest
import requests
from src.constants.api_constants import APIconstants
from src.helpers.utils import common_headers_json
# Read the Excel file ::
import openpyxl 



# step 1 Read the file and put the content into a set/dict

def read_credentials_from_excel(file_path):
    credentials=[]
    workbook = openpyxl.load_workbook(file_path)
    sheet=workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password =row
        credentials.append({
    "username" : username,
    "password" : password
    })
    print(credentials)   
    return credentials


def make_request_auth(username,password):
    payloadtoken = {
    "username" : username,
    "password" : password
    }
    response = requests.post(url=APIconstants().url_create_auth()
                            ,headers=common_headers_json(),json=payloadtoken)
    return response

def test_post_create_token():
    #make requests auth -> Run the func ,Row that we have in excel 
    file_path="testdata_ddt.xlsx"
    credentials= read_credentials_from_excel( file_path=file_path)

    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username,password)
        response =make_request_auth(username,password)
        print(response)
        # Here we can write logic for negative and positive
        assert response.status_code ==200,"wrong status code"
        #assert response.json()["token"] is True,"Wrong username or password"


read_credentials_from_excel("testdata_ddt.xlsx")
test_post_create_token()
