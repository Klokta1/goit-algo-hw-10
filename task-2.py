import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції f(x) = x^2
def f(x):
    return x ** 2

# Метод Монте-Карло для обчислення визначеного інтегралу
def monte_carlo_integration(f, a, b, num_points=10000):
    # Генеруємо випадкові точки
    x_random = np.random.uniform(a, b, num_points)
    y_random = np.random.uniform(0, b ** 2, num_points)

    # Обчислюємо кількість точок, що знаходяться під кривою
    under_curve = y_random < f(x_random)

    # Площа прямокутника: (b - a) * (максимальне значення функції на цьому інтервалі)
    area_of_rectangle = (b - a) * (b ** 2)

    # Обчислюємо площу під кривою
    estimated_area = area_of_rectangle * np.sum(under_curve) / num_points

    return estimated_area

# Аналітичне обчислення інтегралу за допомогою функції quad
def analytical_integration(f, a, b):
    result, error = spi.quad(f, a, b)
    return result

# Межі інтегрування
a = 0
b = 2

# Обчислення за допомогою методу Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b)

# Обчислення аналітичного результату за допомогою quad
quad_result = analytical_integration(f, a, b)

# Виведення результатів
print(f"Метод Монте-Карло: {monte_carlo_result}")
print(f"Аналітичне обчислення (quad): {quad_result}")

# Візуалізація результатів
x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
