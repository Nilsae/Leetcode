import numpy as np


# Define the sigmoid activation function
def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


# Sigmoid derivative for backpropagation
def sigmoid_derivative(x):
    return x * (1.0 - x)


# Define the Neural Network class
class NeuralNetwork:
    def __init__(self, x, y, learning_rate=0.3):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 4)
        self.weights2 = np.random.rand(4, 1)
        self.y = y
        self.output = np.zeros(y.shape)
        self.learning_rate = learning_rate

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # TODO: Update the weights using the derivative of the loss function
     
        d_w2 = 2 * ( self.y - self.output) * sigmoid_derivative(self.output)
        self.weights2 += self.learning_rate * self.layer1.T @ d_w2
       
        d_w1 = d_w2 * self.weights2.T * sigmoid_derivative(self.layer1) 
        self.weights1 += self.learning_rate * self.input.T @ d_w1
     
    def train(self, epochs):
        for epoch in range(epochs):
            self.feedforward()
            self.backprop()

    def predict(self, new_input):
        layer1 = sigmoid(np.dot(new_input, self.weights1))
        output = sigmoid(np.dot(layer1, self.weights2))
        return output


X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
Y = np.array([[0],
              [1],
              [1],
              [0]])
nn = NeuralNetwork(X, Y)

nn.train(5000)

print("Predictions after training:")
for single_X, target in zip(X, Y):
    prediction = nn.predict(np.array([single_X]))
    print(f"Input: {single_X} ---> Prediction: {prediction}, Expected: {target}")


