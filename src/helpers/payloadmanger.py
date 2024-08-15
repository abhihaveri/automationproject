from faker import Faker
import json

Faker=Faker()

print(Faker.first_name())

def payload_create_booking():
    payload = {
    "firstname" : Faker.first_name(),
    "lastname" : Faker.last_name(),
    "totalprice" : Faker.random_int(min=100,max=1000),
    "depositpaid" : Faker.boolean(),
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : Faker.random_element(elements=("Breakfast","Parking","Wifi"))
}
    print(payload)
    return payload
payload_create_booking()

def payload_create_token():
    payloadtoken = {
    "username" : "admin",
    "password" : "password123"
}
    return payloadtoken


def payload_update_booking():
    payload = {
    "firstname" : "Abhi",
    "lastname" : "Indian",
    "totalprice" : 555,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    return payload

