import math
import matplotlib.pyplot as plt
import numpy as np
from GeneralFunctions import ActivationFunction


class ReLU(ActivationFunction):
    """
    ReLU (Rectified Linear Unit Function) class that calculates the ReLU of input data \
    and visualizes the distribution.

    Arg:
        data (numpy array): user defined data
        derivative (bool): plot derivative function if True and don't plot if False.
    """

    def __init__(self, data=None):

        ActivationFunction.__init__(self, default_data=None)
        self.data = data

    @property
    def relu_values(self):
        """
        Method to calculate the ReLU values of the data set.

            Args:
                None

            Returns:
                numpy array: ReLU values of the data set
        """
        if self.data is None:
            self.data = self.default_data

        return np.maximum(0, self.data)

    def relu_plot(self, derivative=False):
        """
        Method to calculate the ReLU values of the data set.

            Args:
                derivative (bool): plot derivative function if True and don't plot if False

            Returns:
                image : visualization of the ReLU values and its derivative if 'True'
        """

        if derivative is not True:
            plt.plot(self.data, self.relu_values)
            plt.title("ReLU Distribution")
            plt.legend(["ReLU"])
            plt.style.use('ggplot')
            plt.xlabel("ReLU values")
            plt.ylabel("Value points")
            plt.show()

        else:
            derivative_val = np.array([0 if x <= 0 else 1 for x in self.data])

            plt.plot(self.data, derivative_val)
            plt.plot(self.data, self.relu_values)
            plt.title("ReLU Distribution")
            plt.legend(["Derivative", "ReLU"])
            plt.style.use('ggplot')
            plt.xlabel("ReLU values")
            plt.ylabel("Value points")
            plt.show()


arr = np.linspace(-10, 10, 1000)
relu = ReLU(arr)
print(relu.relu_plot(derivative=True))
