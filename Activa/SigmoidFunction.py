import math
import matplotlib.pyplot as plt
import numpy as np
from GeneralFunctions import ActivationFunction


class Sigmoid(ActivationFunction):
    """
    Sigmoid class that calculates the Sigmoid of input data \
    and visualizes the distribution.

    Arg:
        data (int, float): user defined data
        derivative (bool): plot derivative function if True and don't plot if False.
    """

    def __init__(self, data=None):
        ActivationFunction.__init__(self, default_data=None)
        self.data = data

    @property
    def sigmoid_values(self):
        """
        TODO -- Write documentation
        """
        if self.data is None:
            self.data = self.default_data

        return np.array([(1 / (1 + math.exp(-x))) for x in self.data])

    def sigmoid_plot(self, derivative=False):
        """
        TODO -- Write documentation
        """

        # TODO: Write codes for visualizing the distribution
        plt.plot(self.data, self.sigmoid_values)
        plt.title("Sigmoid fxn")
        plt.legend(["Sigmoid"])
        plt.style.use('ggplot')
        plt.xlabel("Sigmoid values")
        plt.ylabel("Value points")
        plt.show()


arr = np.linspace(-10, 10, 1000)
sig = Sigmoid(arr)
print(sig.sigmoid_values)
