import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([2.56, 3.12, 4.15, 5.58, 7.1, 8.53, 9.969, 11.53, 13.16])

r = np.corrcoef(x, y)[0, 1]

degree = 3  
coefficients = np.polyfit(x, y, degree)
polynomial = np.poly1d(coefficients)

y_predicted = polynomial(x)

polynomial_terms = [f"{coeff:.4f}x^{i}" if i > 0 else f"{coeff:.4f}" 
                    for i, coeff in enumerate(reversed(coefficients))]
polynomial_equation = " + ".join(polynomial_terms).replace("x^1", "x")
print("Actual Polynomial Equation:")
print(f"y = {polynomial_equation}")

print("\nActual Curve Values:")
for i, (xi, yi, ypi) in enumerate(zip(x, y, y_predicted), 1):
    print(f"x[{i}] = {xi}, y[{i}] (original) = {yi}, y[{i}] (predicted) = {ypi:.3f}")

x_curve = np.linspace(min(x), max(x), 100)
y_curve = polynomial(x_curve)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', marker='o', label='Data Points')
plt.plot(x_curve, y_curve, color='red', label=f'{degree}-Degree Best-Fit Curve\n(n=900, r={r:.4f})')

plt.title(f'Average Analytic Upper Bound Rank vs. Number of Digits\n{degree}-Degree Best-Fit Curve')
plt.xlabel('Number of Digits')
plt.ylabel('Average Analytic Upper Bound Rank')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.show()
