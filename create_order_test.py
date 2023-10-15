import sender_stand_request

def test_get_order_track_number():

    assert sender_stand_request.response_track_number.status_code == 200



