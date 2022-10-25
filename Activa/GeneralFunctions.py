import numpy as np


class ActivationFunction:

    def __init__(self, default_data=None):
        """
            The parent class for all activation functions: --> The class to be inherited.

            Attributes:
            default_data (int, float): default data used for generating activation functions
            data (int, float, array, pandas series): data supplied by the user
            """

        if default_data is None:
            default_data = np.array([-1, 0, 1])
        self.default_data = default_data

