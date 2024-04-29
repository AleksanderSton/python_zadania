import matplotlib.pyplot as plt
import random

f1 = lambda x, y: (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6)
f2 = lambda x, y: (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44)
f3 = lambda x, y: (0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6)
f4 = lambda x, y: (0, 0.16 * y)

losuj_transformacje = lambda: random.choices([f1, f2, f3, f4], weights=[85, 7, 7, 1])[0]

x, y = 0, 0

steps = 1000

x_points = []
y_points = []

for _ in range(steps):
    funkcja_transformacji = losuj_transformacje()
    x, y = funkcja_transformacji(x, y)
    x_points.append(x)
    y_points.append(y)

plt.figure(figsize=(8, 8))
plt.scatter(x_points, y_points, s=1, c='g')
plt.title('Paprotka Bransleya')
plt.show()
