import configuration
import requests

#создаём нового курьера
def post_new_courier():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_COIRIER,
                         json={ "login": "GEG",
                                "password": "1234",
                                "firstName": "saskef"
                         })

#логинимся курьером
def log_courier():
    return requests.post(configuration.URL_SERVICE + configuration.COURIER_LOGIN,
                         json={
                                "login": "GEG",
                                "password": "1234"
                              }
                         )
#создание нового заказа
def new_order():
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER,
                         json= {
                             "firstName": "ЙЦУК",
                             "lastName": "НЕКУ",
                             "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
                             "metroStation": 1,
                             "phone": "+7 800 355 35 35",
                             "rentTime": 5,
                             "deliveryDate": "2023-06-06",
                             "comment": "Saske, come back to Konoha",
                             "color": [
                                 "BLACK"
                             ]
                               })


def cancel_order():
    return requests.put(configuration.URL_SERVICE + configuration.CANCEL_ORDER,
                        json={
                            "track": 548362
                            })

#не автоматизировано, id вставлять руками
#взять заказ курьером
def get_order_courier():
    return requests.put(configuration.URL_SERVICE + "/api/v1/orders/accept/603452?courierId=213")

#get order number
# ?t=123456
def get_order_number():
   return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_NUMBER + "?t=" + str(track_number))



response_new_order = new_order()
track_number = response_new_order.json()["track"]
response_track_number = get_order_number()

