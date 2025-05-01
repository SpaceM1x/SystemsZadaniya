import numpy as np

# Исходные данные
supply = [200, 300, 100]  # Мощности поставщиков
demand = [450, 250, 100, 100]  # Спрос потребителей
costs = [
    [6, 4, 4, 5],
    [6, 9, 5, 8],
    [8, 2, 10, 6]
]

# Добавляем фиктивного поставщика для балансировки
total_supply = sum(supply)
total_demand = sum(demand)
if total_supply != total_demand:
    supply.append(total_demand - total_supply)
    costs.append([0] * len(demand))


# Метод северо-западного угла
def northwest_corner(supply, demand):
    alloc = np.zeros((len(supply), len(demand)), dtype=int)
    i = j = 0
    while i < len(supply) and j < len(demand):
        quantity = min(supply[i], demand[j])
        alloc[i][j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity
        if supply[i] == 0:
            i += 1
        else:
            j += 1
    return alloc


# Метод минимального элемента
def minimal_cost(supply, demand, costs):
    alloc = np.zeros((len(supply), len(demand)), dtype=int)
    temp_costs = [row[:] for row in costs]
    temp_supply = supply.copy()
    temp_demand = demand.copy()

    while max(temp_supply) > 0 and max(temp_demand) > 0:
        # Находим минимальную стоимость
        min_val = float('inf')
        for i in range(len(temp_costs)):
            for j in range(len(temp_costs[0])):
                if temp_costs[i][j] < min_val and temp_supply[i] > 0 and temp_demand[j] > 0:
                    min_val = temp_costs[i][j]
                    min_i, min_j = i, j

        # Распределяем ресурсы
        quantity = min(temp_supply[min_i], temp_demand[min_j])
        alloc[min_i][min_j] = quantity
        temp_supply[min_i] -= quantity
        temp_demand[min_j] -= quantity

        # Убираем рассмотренную стоимость
        temp_costs[min_i][min_j] = float('inf')

    return alloc


# Выполнение расчетов
print("Метод северо-западного угла:")
nw_result = northwest_corner(supply.copy(), demand.copy())
print(nw_result)
print("\nМетод минимального элемента:")
mc_result = minimal_cost(supply.copy(), demand.copy(), costs)
print(mc_result)


# Расчет общей стоимости
def calculate_total_cost(alloc, costs):
    total = 0
    for i in range(len(alloc)):
        for j in range(len(alloc[0])):
            total += alloc[i][j] * costs[i][j]
    return total


print("\nОбщая стоимость (северо-запад):", calculate_total_cost(nw_result, costs))
print("Общая стоимость (минимальный элемент):", calculate_total_cost(mc_result, costs))