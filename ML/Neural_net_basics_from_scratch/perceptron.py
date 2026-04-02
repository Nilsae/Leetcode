import numpy as np

class Perceptron:
    def __init__(self, no_of_inputs, max_iterations=10, learning_rate=0.1):
        self.max_iterations = max_iterations
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)
    
    def predict(self, inputs):
        out = self.weights[0] + np.dot(inputs, self.weights[1:])
        return 1 if out > 0.5 else 0
        
    
    def train(self, training_inputs, labels):
        for _ in range(self.max_iterations):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)

# Test the perceptron after you've added your prediction logic
perceptron = Perceptron(2)
training_inputs = [np.array([1, 1]), np.array([1, 0]), np.array([0, 1]), np.array([0, 0])]
labels = np.array([1, 0, 0, 0])

perceptron.train(training_inputs, labels)

inputs = np.array([1, 1])
print(perceptron.predict(inputs))  # Expected Output: 1

inputs = np.array([0, 1])
print(perceptron.predict(inputs))  # Expected Output: 0