import numpy as np
from itertools import combinations
from scipy.optimize import linear_sum_assignment

# Исходные данные
scientists = ['Адаме', 'Браун', 'Карр', 'Дай', 'Иване']
data = [
    [80, 120, 60, 104],    # Адаме
    [72, 144, 48, 110],    # Браун
    [96, 148, 72, 120],    # Карр
    [60, 108, 52, 92],     # Дай
    [64, 140, 60, 96]      # Иване
]

min_total = float('inf')
best_assignments = []
best_scientists = []

# Перебор комбинаций из 4 ученых
for indices in combinations(range(5), 4):
    submatrix = np.array([data[i] for i in indices])
    row_ind, col_ind = linear_sum_assignment(submatrix)
    total = submatrix[row_ind, col_ind].sum()
    if total < min_total:
        min_total = total
        best_assignments = list(zip(row_ind, col_ind))
        best_scientists = indices

# Сбор всех оптимальных вариантов
all_best = []
for indices in combinations(range(5), 4):
    submatrix = np.array([data[i] for i in indices])
    row_ind, col_ind = linear_sum_assignment(submatrix)
    total = submatrix[row_ind, col_ind].sum()
    if total == min_total:
        assignments = []
        for sci_sub_idx, proj_idx in zip(row_ind, col_ind):
            scientist_idx = indices[sci_sub_idx]
            project_num = proj_idx + 1
            assignments.append((scientists[scientist_idx], project_num, data[scientist_idx][proj_idx]))
        all_best.append(assignments)

# Проверка предпочтений
reasonable = []
for variant in all_best:
    valid = True
    for a in variant:
        scientist, project, _ = a
        if scientist in ['Браун', 'Карр', 'Дай'] and project not in [2, 3]:
            valid = False
        elif scientist in ['Адаме', 'Иване'] and project not in [1, 4]:
            valid = False
    if valid:
        reasonable.append(variant)

# Вывод результатов
print("Минимальное общее время:", min_total)
print("\nПример оптимального назначения:")
for a in all_best[0]:
    print(f"{a[0]} -> Проект {a[1]} ({a[2]} дней)")

if reasonable:
    print("\nНаиболее разумный вариант с учетом предпочтений:")
    for a in reasonable[0]:
        print(f"{a[0]} -> Проект {a[1]}")
else:
    print("\nОптимальные варианты, частично соответствующие предпочтениям:")
    for a in all_best[0]:
        pref = ""
        scientist, project, _ = a
        if scientist in ['Браун', 'Карр', 'Дай'] and project in [2, 3]:
            pref = "(соответствует предпочтению)"
        elif scientist in ['Адаме', 'Иване'] and project in [1, 4]:
            pref = "(соответствует предпочтению)"
        print(f"{a[0]} -> Проект {a[1]} {pref}")