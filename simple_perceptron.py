import numpy as np


np.random.seed(1)


# Dataset 01
inputs_01 = np.array([
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1],
])

outputs_01 = np.array([
    [0],
    [1],
    [1],
    [0],
])


# Dataset 02
inputs_02 = np.array([
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1],
])

outputs_02 = np.array([
    [0],
    [1],
    [0],
    [1],
])


# Dataset 03
inputs_03 = np.array([
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1],
])

outputs_03 = np.array([
    [0, 1],
    [1, 0],
    [0, 1],
    [1, 0],
])


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class SimplePerceptron:
    """
    3 input neurons
    1 output neuron
    """

    def __init__(self, synaptic_weights=None, input_neurons=3, output_neurons=1):
        if synaptic_weights is not None:
            self.synaptic_weights = synaptic_weights
        else:
            self.synaptic_weights = 2 * np.random.random((input_neurons, output_neurons)) - 1

    def execute(self, input_layer, rounded=False):
        doted_outputs = np.dot(input_layer, self.synaptic_weights)
        result_outputs = sigmoid(doted_outputs)
        if rounded:
            result_outputs = np.round(result_outputs).astype(int)
        return result_outputs

    def training(self, training_inputs, training_outputs, iterations=20000):
        input_layer = training_inputs

        for i in range(iterations):
            result_outputs = self.execute(training_inputs, rounded=False)

            error_delta = training_outputs - result_outputs
            adjustments = np.dot(input_layer.T, error_delta * (result_outputs * (1 - result_outputs)))
            self.synaptic_weights += adjustments
