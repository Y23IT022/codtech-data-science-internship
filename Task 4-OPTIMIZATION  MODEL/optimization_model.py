import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Objective Function
# Maximize 50A + 40B
# Convert to minimization

c = [-50, -40]

# Constraints
A = [
    [2, 1],
    [1, 1]
]

b = [100, 80]

# Bounds
x_bounds = (0, None)
y_bounds = (0, None)

# Solve
result = linprog(
    c,
    A_ub=A,
    b_ub=b,
    bounds=[x_bounds, y_bounds],
    method='highs'
)

A_opt = result.x[0]
B_opt = result.x[1]

max_profit = -result.fun

print("Optimal Production")
print("Product A =", round(A_opt))
print("Product B =", round(B_opt))
print("Maximum Profit = ₹", round(max_profit))

# Graph
products = ['Product A', 'Product B']
values = [A_opt, B_opt]

plt.bar(products, values)

plt.title("Optimal Production Quantities")
plt.ylabel("Units Produced")

plt.savefig("optimization_graph.png")
plt.show()
