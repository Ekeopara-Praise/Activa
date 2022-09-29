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
            default_data = np.array([-3, -2, -1, 0, 1, 2, 3])
        self.default_data = default_data


    # def read_data_file(self, file_name):
    #
    #     """
    #     Arg:
    #         file_name (string): name of the file to read data from
    #
    #     Return:
    #         None
    #     """
    #     with open(file_name) as file:
    #         data_list = []
    #         line = file.readline()
    #         while line:
    #             data_list.append(int(line))
    #             line = file.readline()
    #     file.close()
    #
    #     self.data = data_list

af = ActivationFunction()
print(type(af.default_data))