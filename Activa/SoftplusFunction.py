from .GeneralFunctions import ActivationFunction
import matplotlib.pyplot as plt
import numpy as np
import math


class Softplus(ActivationFunction):
    """
        Tanh class that calculates the Tanh of input data \
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
    def softplus_values(self):
        """
        Method to calculate the tanh values of the data set.

            Args:
                None

            Returns:
                numpy array: tanh values of the data set
        """

        return np.array([math.log(1 + math.exp(x)) for x in self.data])

    def softplus_plot(self, derivative=False):
        """
        Method to visualize the softplus values of the data set.

            Args:
                derivative (bool): plot derivative function if True and don't plot if False

            Returns:
                image : visualization of the softplus values and its derivative if 'True'
        """

        if derivative is not True:
            plt.plot(self.data, self.softplus_values)
            plt.title("Softplus Distribution")
            plt.legend(["Softplus"])
            plt.style.use('ggplot')
            plt.xlabel("Softplus values")
            plt.ylabel("Value points")
            plt.show()

        else:
            derivative_val = np.array([(1 / (1 + math.exp(-x))) for x in self.data])

            plt.plot(self.data, derivative_val)
            plt.plot(self.data, self.softplus_values)
            plt.title("Softplus Distribution")
            plt.legend(["Derivative", "Softplus"])
            plt.style.use('ggplot')
            plt.xlabel("Softplus values")
            plt.ylabel("Value points")
            plt.show()
