# Yandex_QA_Final
Автотест по финальной работе

configuration - переменные в которых записан путь до адреса и ручек пользователя и набора

create_order_test - тестовая функция

sender_stand_request - функции для создания заказа, получения номера заказа и запроса заказа по номеру

Для запуска тестов

    распаковать папку

    запустить стенд

    в файле configuration.py перезадать корректный URL-адрес стенда

    открыть эту распакованную папку в терминале

    выполнить pytest -v

Работа теста: 
new_order() - функция создания нового заказа

track_number - получаем в переменную номер трека заказа

get_order_number() - функция получения заказа по номеру трека


в тестовой функции просто проверяем, что статус равен 200



_______________________________________________________
ЗАДАНИЯ ПО SQL ЗАПРОСАМ.

Couriers = id / login / passwordHash / firstName / createdAt / updateAt

Orders = id / courierId / firstName / lastName / address / metroStation / phone / rentTime
/ deliveryDate / track / inDelivery / color / comment / cancelled / finished / createdAt / updatedAt


1.
выведи список логинов курьеров с 
количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

SELECT co.login, COUNT(or.id) AS quantity

FROM "Couriers" AS co

INNER JOIN "Orders" AS or

ON co.id = or.courierId

WHERE or.inDelivery = true

GROUP BY co.login;




2. Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:

Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.


SELECT track, status AS status

CASE

	WHEN 'finished' = true THEN status = 2
 
	
	WHEN 'cancelled' = true THEN status = -1
 

	WHEN 'inDelivery' = true THEN status = 1
 
END

FROM "Couriers";
