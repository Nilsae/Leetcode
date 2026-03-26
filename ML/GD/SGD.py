import numpy as np
import matplotlib.pyplot as plt

# Data representing housing sizes (in 1000 sqft) and prices (in $1000s)
X = np.array([0.7, 1.5, 2.1, 2.9, 3.3, 4.5])
Y = np.array([150, 300, 320, 360, 400, 480])

# Model initialization with random values for slope (m) and intercept (b)
m = np.random.randn()
b = np.random.randn()

learning_rate = 0.01  # Learning rate for the optimization
epochs = 10000  # Number of iterations to perform

# SGD to optimize the slope and intercept
for _ in range(epochs):
    random_index = np.random.randint(len(X))  # Pick a random data point
    x_i = X[random_index]
    y_i = Y[random_index]
    pred = m * x_i + b  # Predicted price
    # Gradients for slope and intercept adjusted with negative sign
    grad_m = 2 * x_i * (pred - y_i)
    grad_b = 2 * (pred - y_i)
    m -= learning_rate * grad_m  # Update slope
    b -= learning_rate * grad_b  # Update intercept

print(f"The line equation is y={round(m, 2)}x + {round(b, 2)}")

# Scatter plot of actual data points
plt.scatter(X, Y, color="blue", marker="o", label="Actual Prices")

# Line representing our model's predictions
y_pred = m * X + b
plt.plot(X, y_pred, color="red", label="Predicted Prices")

# Adding labels and legend to the plot
plt.xlabel('Housing Size (1000 sqft)')
plt.ylabel('Price ($1000s)')
plt.legend()

# Display the plot
plt.show()