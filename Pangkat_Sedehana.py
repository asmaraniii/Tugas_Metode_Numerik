import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([7, 4, 8, 5, 7, 3, 7, 8, 5, 4])
Y = np.array([91, 65, 45, 36, 66, 61, 63, 42, 61, 69])

# Hitung rata-rata
mean_X = np.mean(X)
mean_Y = np.mean(Y)

# Hitung variasi
Sxx = np.sum((X - mean_X) ** 2)
Syy = np.sum((Y - mean_Y) ** 2)
Sxy = np.sum((X - mean_X) * (Y - mean_Y))

# Hitung koefisien regresi
beta_2 = (Sxy - mean_X * Syy) / (Sxx - mean_X ** 2)
beta_1 = mean_Y - beta_2 * mean_X
beta_0 = mean_Y - beta_1 * mean_X - beta_2 * mean_X ** 2

# Model Regresi Kuadratik
def quadratic_regression(x):
    return beta_0 + beta_1 * x + beta_2 * x ** 2

# Plot titik data
plt.scatter(X, Y, color='blue', label='Data')

# Plot kurva regresi kuadratik
x_values = np.linspace(min(X), max(X), 100)
y_values = quadratic_regression(x_values)
plt.plot(x_values, y_values, color='red', label='Regresi Kuadratik')

# Anotasi
plt.title('Regresi Kuadratik')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# Tampilkan plot
plt.show()

# Menghitung galat RMS
predicted_Y = quadratic_regression(X)
rms_error = np.sqrt(np.mean((Y - predicted_Y)**2))
print("Galat RMS:", rms_error)