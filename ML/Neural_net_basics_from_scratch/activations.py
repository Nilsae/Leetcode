import numpy as np
import matplotlib.pyplot as plt


def step_function(x):
    return 1 if x > 0.5 else 0
    
def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))


def tanh_function(x):
    return 2 / (1 + np.exp(-2 * x)) - 1


def ReLU_function(x):
    return x if x > 0 else 0


def softplus_function(x):
    return np.log(1 + np.exp(x))

x = np.linspace(-10, 10, 100)

y = [step_function(i) for i in x]
y_sigmoid = [sigmoid_function(val) for val in x]
y_tanh = [tanh_function(val) for val in x]
y_relu = [ReLU_function(val) for val in x]
y_softplus = [softplus_function(val) for val in x]

plt.plot(x, y)
plt.plot(x, y_sigmoid)
plt.plot(x, y_tanh)
plt.plot(x, y_relu)
plt.plot(x, y_softplus)

plt.legend(['step', 'Sigmoid', 'Tanh', 'ReLU', 'Softplus'])
plt.show()