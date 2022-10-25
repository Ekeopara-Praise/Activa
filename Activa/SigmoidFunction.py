import math
import matplotlib.pyplot as plt
import numpy as np
from .GeneralFunctions import ActivationFunction


class Sigmoid(ActivationFunction):
    """
    Sigmoid class that calculates the Sigmoid of input data \
    and visualizes the distribution.

    Arg:
        data (numpy array): user defined data
        derivative (bool): plot derivative function if True and don't plot if False.
    """

    def __init__(self, data=None):

        ActivationFunction.__init__(self, default_data=None)
        self.data = data

        if self.data is None:
            self.data = self.default_data

    @property
    def sigmoid_values(self):

        """
        Method to calculate the sigmoid values of the data set.

            Args:
                None

            Returns:
                numpy array: sigmoid values of the data set
        """

        return np.array([(1 / (1 + math.exp(-x))) for x in self.data])

    def sigmoid_plot(self, derivative=False):

        """
        Method to calculate the sigmoid values of the data set.

            Args:
                derivative (bool): plot derivative function if True and don't plot if False

            Returns:
                image : visualization of the sigmoid values and its derivative if 'True'
        """

        if derivative is not True:
            plt.plot(self.data, self.sigmoid_values)
            plt.title("Sigmoid fxn")
            plt.legend(["Sigmoid"])
            plt.style.use('ggplot')
            plt.xlabel("Sigmoid values")
            plt.ylabel("Value points")
            plt.show()

        else:
            derivative_val = np.array([(math.exp(x) / ((1 + math.exp(x)) ** 2)) for x in self.data])

            plt.plot(self.data, derivative_val)
            plt.plot(self.data, self.sigmoid_values)
            plt.title("Sigmoid fxn")
            plt.legend(["Derivative", "Sigmoid"])
            plt.style.use('ggplot')
            plt.xlabel("Sigmoid values")
            plt.ylabel("Value points")
            plt.show()

