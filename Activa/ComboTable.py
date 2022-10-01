import pandas as pd
import numpy as np
from GeneralFunctions import ActivationFunction
from SigmoidFunction import Sigmoid


class Table(ActivationFunction):

    def __init__(self, data=None):

        ActivationFunction.__init__(self, default_data=None)
        self.data = data

    @property
    def show(self):
        if self.data is None:
            self.data = self.default_data

        s = Sigmoid(self.data)
        dataframe = pd.DataFrame({"actual_values": self.data, "sigmoid": s.sigmoid_values})
        return dataframe


arr = np.linspace(-10, 10, 1000)
t = Table(arr)
print(t.show.head(5))
