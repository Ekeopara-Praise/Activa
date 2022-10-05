import pandas as pd
from GeneralFunctions import ActivationFunction
from SigmoidFunction import Sigmoid
from ReLUFunction import ReLU
from TanhFunction import Tanh
from SoftplusFunction import Softplus
from GaussianFunction import Gaussian


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

        if self.data is None:
            self.data = self.default_data

    @property
    def show(self):
        """
           Method to compares all activation functions across their actual values.

               Args:
                   None

               Returns:
                   pandas dataframe: actual values vs all activation values.
               """

        s = Sigmoid(self.data)
        r = ReLU(self.data)
        t = Tanh(self.data)
        sp = Softplus(self.data)
        g = Gaussian(self.data)

        dataframe = pd.DataFrame({"actual_values": self.data,
                                  "sigmoid": s.sigmoid_values,
                                  "relu": r.relu_values,
                                  "tanh": t.tanh_values,
                                  "softplus": sp.softplus_values,
                                  "gaussian": g.gaussian_values})
        return dataframe


# # arr = np.linspace(-10, 10, 1000)
# t = Table()
# print(t.show)
