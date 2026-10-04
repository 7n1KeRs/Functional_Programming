from functools import reduce

users = [
    {"name": "Alice", "expenses": [100, 50, 75, 200]},
    {"name": "Bob", "expenses": [50, 75, 80, 100]},
    {"name": "Charlie", "expenses": [200, 300, 50, 150]},
    {"name": "David", "expenses": [100, 200, 300, 400]},
    {"name": "Eve", "expenses": [20, 40, 60, 80]},
    {"name": "Frank", "expenses": [500, 100, 50, 20]},
    {"name": "Grace", "expenses": [10, 20, 30, 40]},
    {"name": "Heidi", "expenses": [150, 250, 350, 450]},
    {"name": "Ivan", "expenses": [90, 80, 70, 60]},
    {"name": "Judy", "expenses": [110, 120, 130, 140]},
    {"name": "Mallory", "expenses": [5, 10, 15, 20]},
    {"name": "Niaj", "expenses": [1000, 2000, 1500, 500]},
    {"name": "Olivia", "expenses": [45, 55, 65, 75]},
    {"name": "Peggy", "expenses": [300, 200, 100, 50]},
    {"name": "Rupert", "expenses": [25, 35, 45, 55]},
    {"name": "Sybil", "expenses": [600, 700, 800, 900]},
    {"name": "Trent", "expenses": [12, 24, 36, 48]},
    {"name": "Victor", "expenses": [88, 99, 111, 122]},
    {"name": "Wendy", "expenses": [400, 300, 200, 100]},
    {"name": "Xavier", "expenses": [15, 25, 35, 45]}
]

filtered_users = list(filter(lambda u: any(exp > 500 for exp in u["expenses"]), users))
print(f"Пользователей с расходами > 500: {len(filtered_users)}")

user_sums = list(map(lambda u: sum(u["expenses"]), filtered_users))

total_expenses = reduce(lambda x, y: x + y, user_sums, 0)
print(f"Общая сумма расходов отфильтрованных пользователей: {total_expenses}")
