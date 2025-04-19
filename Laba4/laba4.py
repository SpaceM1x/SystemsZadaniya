import numpy as np

# Исходные данные
attendances = [4000, 4500, 5000, 5500, 6000]
probabilities = [0.1, 0.3, 0.3, 0.2, 0.1]
demand = [att * 0.4 for att in attendances]  # Спрос на программки (40% от посещаемости)
order_options = [1600, 1800, 2000, 2200, 2400]  # Возможные варианты заказа

# Функция расчета прибыли
def calculate_profit(Q, D, ad_income=300):
    cost = 200 + 0.3 * Q  # Стоимость заказа
    sales = 0.6 * min(Q, D)  # Доход от продаж
    return sales + ad_income - cost

# Построение матрицы прибыли
profit_matrix = []
for Q in order_options:
    row = []
    for D in demand:
        profit = calculate_profit(Q, D)
        row.append(profit)
    profit_matrix.append(row)

# ----------------------
# 1. Решение для исходных условий
# ----------------------
# Критерий Вальда (максимин)
wald = [min(row) for row in profit_matrix]
best_wald = order_options[np.argmax(wald)]

# Критерий Сэвиджа (минимаксное сожаление)
max_profit_per_demand = [max(col) for col in zip(*profit_matrix)]
regret_matrix = []
for row in profit_matrix:
    regret_row = [max_profit_per_demand[i] - row[i] for i in range(len(row))]
    regret_matrix.append(regret_row)
savage = [max(row) for row in regret_matrix]
best_savage = order_options[np.argmin(savage)]

# Критерий Гурвица (α=0.5)
alpha = 0.5
hurwicz = [alpha * max(row) + (1 - alpha) * min(row) for row in profit_matrix]
best_hurwicz = order_options[np.argmax(hurwicz)]

# ----------------------
# 2. Решение для измененных условий
# ----------------------
# Новые параметры: реклама 400, посещаемость >5250, спрос удовлетворен полностью
new_probabilities = [0.0, 0.0, 0.0, 0.5, 0.5]  # Гипотетическое распределение
new_demand = [att * 0.4 for att in [5500, 6000]]  # Только 5500 и 6000
new_order_options = [2200, 2400]

# Обновленная матрица прибыли
new_profit_matrix = []
for Q in new_order_options:
    row = []
    for D in new_demand:
        # Учитываем полное удовлетворение спроса (Q >= D)
        sales = 0.6 * D if Q >= D else 0.6 * Q
        cost = 200 + 0.3 * Q
        profit = sales + 400 - cost  # Новый доход от рекламы
        row.append(profit)
    new_profit_matrix.append(row)

# Пересчет критериев
# Вальд
new_wald = [min(row) for row in new_profit_matrix]
new_best_wald = new_order_options[np.argmax(new_wald)]

# ----------------------
# Вывод результатов
# ----------------------
print("Часть 1:")
print(f"Критерий Вальда: заказать {best_wald} программок")
print(f"Критерий Сэвиджа: заказать {best_savage} программок")
print(f"Критерий Гурвица: заказать {best_hurwicz} программок\n")

print("Часть 2 (при новых условиях):")
print(f"Критерий Вальда: заказать {new_best_wald} программок")
print("Рекомендации сместятся в сторону большего заказа из-за увеличения рекламы и гарантированного спроса.")