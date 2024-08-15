# Python API Automation Framework 

 Hybrid custom Framework to test the REST APIs

### Tech Stack
1.Python 3.12.1
2.Request -HTTP Requests
3.Pytest- testing Framework
4.Reporting-Allure Report, Pytest HTML
5.Test Data- CSV, Excel,JSON
6.Parallel Execution -x distribute 

### How to install Packages 
''pip install pytest pytest-html faker allure-pytest jsonschema requests
'' 

### To Freeze your packages version
pip freeze > requirements.txt

### secure username and password 
pip install python-dotenv

### To install Freezed  packages version
pip install -r requirements.txt

## To run the Allure 
pytest C:\Users\abhis\Desktop\Automationproject\test_create_booking.py -s -v --alluredir=./reports
allure serve reports

## Install parallel running in pytest
pip install pytest-xdist
pytest -n auto ### C:\Users\abhis\Desktop\Automationproject\test_parallel.py # select

## To open the excel files
pip install openpyxl

## To work with jsonschema 
pip install jsonschema