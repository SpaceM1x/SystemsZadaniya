# Расчет вероятностей и ожидаемых значений с учетом исследования

# Исходные данные
survey_cost = 5  # Стоимость исследования в млн руб.

# Вероятности без исследования (равные)
p_favorable_no_survey = 0.5
p_unfavorable_no_survey = 0.5

# Вероятности с исследованием
p_survey_positive = 0.6154
p_survey_negative = 0.3846
p_favorable_positive = 0.9
p_favorable_negative = 0.12

# Ожидаемая стоимостная ценность для каждого варианта
def calculate_emv(prob_favorable, profit_favorable, loss_unfavorable):
    return prob_favorable * profit_favorable + (1 - prob_favorable) * loss_unfavorable

# Сценарий БЕЗ исследования
emv_big_no_survey = calculate_emv(p_favorable_no_survey, 60, -40)
emv_small_no_survey = calculate_emv(p_favorable_no_survey, 30, -10)
best_emv_no_survey = max(emv_big_no_survey, emv_small_no_survey)

# Сценарий С исследованием
# Для положительного заключения
emv_big_positive = calculate_emv(p_favorable_positive, 60, -40)
emv_small_positive = calculate_emv(p_favorable_positive, 30, -10)
best_emv_positive = max(emv_big_positive, emv_small_positive)

# Для отрицательного заключения
emv_big_negative = calculate_emv(p_favorable_negative, 60, -40)
emv_small_negative = calculate_emv(p_favorable_negative, 30, -10)
best_emv_negative = max(emv_big_negative, emv_small_negative)

# Общий EMV с исследованием
emv_with_survey = p_survey_positive * best_emv_positive + p_survey_negative * best_emv_negative - survey_cost

# Сравнение вариантов
print("=== Результаты анализа ===")
print(f"EMV без исследования: {best_emv_no_survey:.2f} млн руб.")
print(f"EMV с исследованием: {emv_with_survey:.2f} млн руб.")

# Рекомендации
recommend_survey = "ДА" if emv_with_survey > best_emv_no_survey else "НЕТ"
recommend_big = "ДА" if (emv_big_positive > emv_small_positive) or (emv_big_negative > emv_small_negative) else "НЕТ"

print("\nРекомендации:")
print(f"1. Следует заказать исследование? {recommend_survey}")
print(f"2. Следует открыть большой магазин? {recommend_big}")
print(f"3. Ожидаемая ценность наилучшего решения: {max(emv_with_survey, best_emv_no_survey):.2f} млн руб.")