from functools import reduce

orders = [
    {"order_id": 1, "customer_id": 101, "amount": 150.0},
    {"order_id": 2, "customer_id": 102, "amount": 200.0},
    {"order_id": 3, "customer_id": 101, "amount": 75.0},
    {"order_id": 4, "customer_id": 103, "amount": 100.0},
    {"order_id": 5, "customer_id": 101, "amount": 50.0},
    {"order_id": 6, "customer_id": 104, "amount": 300.0},
    {"order_id": 7, "customer_id": 102, "amount": 120.0},
    {"order_id": 8, "customer_id": 105, "amount": 80.0},
    {"order_id": 9, "customer_id": 101, "amount": 220.0},
    {"order_id": 10, "customer_id": 103, "amount": 90.0},
    {"order_id": 11, "customer_id": 106, "amount": 400.0},
    {"order_id": 12, "customer_id": 102, "amount": 60.0},
    {"order_id": 13, "customer_id": 104, "amount": 180.0},
    {"order_id": 14, "customer_id": 101, "amount": 110.0},
    {"order_id": 15, "customer_id": 105, "amount": 250.0},
    {"order_id": 16, "customer_id": 106, "amount": 30.0},
    {"order_id": 17, "customer_id": 103, "amount": 140.0},
    {"order_id": 18, "customer_id": 104, "amount": 210.0},
    {"order_id": 19, "customer_id": 102, "amount": 95.0},
    {"order_id": 20, "customer_id": 101, "amount": 330.0}
]

target_customer_id = 101

client_orders = list(filter(lambda o: o["customer_id"] == target_customer_id, orders))
print(f"Количество заказов клиента: {len(client_orders)}")

amounts = list(map(lambda o: o["amount"], client_orders))

total_amount = reduce(lambda x, y: x + y, amounts, 0)
print(f"Общая сумма заказов: {total_amount}")

average_amount = total_amount / len(amounts)
print(f"Средняя стоимость заказа: {average_amount:.2f}")
