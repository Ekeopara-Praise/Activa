import math
import matplotlib.pyplot as plt
from .GeneralFunctions import ActivationFunction


class Sigmoid(ActivationFunction):
    """
    Sigmoid class that calculates the Sigmoid of input data \
    and visualizes the distribution.

    Arg:
        data (int, float): user defined data
        derivative (bool): plot derivative function if True and don't plot if False.
    """

    def __init__(self, default_data=None):

        ActivationFunction.__init__(self, default_data=None)

    def sigmoid_values(self, data=None):
        """
        TODO -- Write documentation
        """
        assert isinstance(data, str)

        if data is None:
            self.data = self.default_data
        else:
            self.data = data

        # TODO: Write the equation for ReLU function

    def sigmoid_plot(self, derivative=False):
        """
        TODO -- Write documentation
        """

        # TODO: Write codes for visualizing the distribution
