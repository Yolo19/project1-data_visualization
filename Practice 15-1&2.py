import matplotlib.pyplot as plt


x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]
plt.figure(1)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.summer, edgecolor='none', s=30)

plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

plt.tick_params(axis="both", which="major", labelsize=14)


x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.figure(2)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.summer, edgecolor='none', s=20)

plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()