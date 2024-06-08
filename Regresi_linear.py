import numpy as np
import matplotlib.pyplot as plt

# Data nilai X (Durasi Waktu Belajar) dan nilai Y (Nilai Ujian)
X = np.array([7, 4, 8, 5, 7, 3, 7, 8, 5, 4])
Y = np.array([91, 65, 45, 36, 66, 61, 63, 42, 61, 69])

# Menghitung rata-rata X dan Y
mean_X = np.mean(X)
mean_Y = np.mean(Y)

# Menghitung koefisien regresi
beta_1 = np.sum((X - mean_X) * (Y - mean_Y)) / np.sum((X - mean_X)**2)
beta_0 = mean_Y - beta_1 * mean_X

# Membuat model Regresi
def linear_regression(x):
    return beta_0 + beta_1 * x

# Plot titik data
plt.scatter(X, Y, color='blue', label='Data')

# Plot garis regresi
x_values = np.linspace(min(X), max(X), 100)
y_values = linear_regression(x_values)
plt.plot(x_values, y_values, color='red', label='Regresi Linear')

# Anotasi
plt.title('Regresi Linear')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# Tampilkan plot
plt.show()

# Menghitung galat RMS
predicted_Y = linear_regression(X)
rms_error = np.sqrt(np.mean((Y - predicted_Y)**2))
print("Galat RMS : ", rms_error)