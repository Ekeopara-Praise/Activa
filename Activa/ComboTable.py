import pandas as pd
import numpy as np
from GeneralFunctions import ActivationFunction
from SigmoidFunction import Sigmoid
from ReLUFunction import ReLU


class Table(ActivationFunction):
    """
        Table class that displays the actual input data and their \
        respective activation function values.

        Arg:
            data (numpy array): user defined data
        """

    def __init__(self, data=None):

        ActivationFunction.__init__(self, default_data=None)
        self.data = data

    @property
    def show(self):
        """
           Method to compares all activation functions across their actual values.

               Args:
                   None

               Returns:
                   pandas dataframe: actual values vs all activation values.
               """

        if self.data is None:
            self.data = self.default_data

        s = Sigmoid(self.data)
        r = ReLU(self.data)
        dataframe = pd.DataFrame({"actual_values": self.data,
                                  "sigmoid": s.sigmoid_values,
                                  "relu": r.relu_values})
        return dataframe


arr = np.linspace(-10, 10, 1000)
t = Table(arr)
print(t.show.head(5))
