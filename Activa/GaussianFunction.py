import matplotlib.pyplot as plt
import numpy as np
import math
from .GeneralFunctions import ActivationFunction


class Gaussian(ActivationFunction):
    """
    Gaussian class that calculates the Gaussian distribution of input data \
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
    def gaussian_values(self):
        """
        Method to calculate the gaussian values of the data set.

            Args:
                None

            Returns:
                numpy array: gaussian values of the data set
        """

        return np.array([math.exp(-x ** 2) for x in self.data])

    def gaussian_plot(self, derivative=False):
        """
        Method to visualize the gaussian values of the data set.

            Args:
                derivative (bool): plot derivative function if True and don't plot if False

            Returns:
                image : visualization of the gaussian values and its derivative if 'True'
        """

        if derivative is not True:
            plt.plot(self.data, self.gaussian_values)
            plt.title("Gaussian Distribution")
            plt.legend(["Gaussian"])
            plt.style.use('ggplot')
            plt.xlabel("Gaussian values")
            plt.ylabel("Value points")
            plt.show()

        else:
            derivative_val = np.array([(-2 * x * math.exp(- x ** 2)) for x in self.data])

            plt.plot(self.data, derivative_val)
            plt.plot(self.data, self.gaussian_values)
            plt.title("Gaussian Distribution")
            plt.legend(["Derivative", "Gaussian"])
            plt.style.use('ggplot')
            plt.xlabel("Gaussian values")
            plt.ylabel("Value points")
            plt.show()
