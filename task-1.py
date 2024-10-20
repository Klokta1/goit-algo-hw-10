import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

x1 = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

model += x1 + x2, "Total_Production"

model += 2 * x1 + 1 * x2 <= 100, "Water_Limit"         # Обмеження на воду
model += 1 * x1 <= 50, "Sugar_Limit"                   # Обмеження на цукор
model += 1 * x1 <= 30, "LemonJuice_Limit"              # Обмеження на лимонний сік
model += 2 * x2 <= 40, "FruitPuree_Limit"              # Обмеження на фруктове пюре

model.solve()

# Виведення результатів
print(f"Кількість виробленого лимонаду: {x1.varValue}")
print(f"Кількість виробленого фруктового соку: {x2.varValue}")
print(f"Загальна кількість вироблених напоїв: {pulp.value(model.objective)}")
