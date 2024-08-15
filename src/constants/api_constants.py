
class APIconstants(object):
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_auth(self):
        return "https://restful-booker.herokuapp.com/auth"


    # update ,PUT,PATCH,DELETE -bookingid

    def url_PATCH_PUT_DELETE_Booking(self,booking_id):
        url="https://restful-booker.herokuapp.com/booking/"+ str(booking_id)
        return url
    

