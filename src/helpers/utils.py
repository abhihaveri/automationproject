# Common headers 

import token


def common_headers_json():
    headers = {
        "Content-Type":"application/json"

    }
    return headers 

def common_headers_xml():
    headers = {
        "Content-Type":"application/xml"

    }
    return headers 

def token_creator(token):
    cookievalue="token="+str(token)
    headers= {"Content-Type":"application/json",
             "Cookie" : cookievalue
             }
    return headers 

#Read data from excel,csv,json,YAML -kepp the funtions in future