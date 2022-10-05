from ReLUFunction import ReLU
from SigmoidFunction import Sigmoid
from TanhFunction import Tanh
from GaussianFunction import Gaussian
from SoftplusFunction import Softplus


import unittest


class TestReLU(unittest.TestCase):

    def testvalues_ReLU(self):
        self.assertEqual(list(ReLU().relu_values), [0, 0, 1], "Correct!")


class TestSoftplus(unittest.TestCase):

    def testvalues_Softplus(self):
        self.assertEqual(list(Softplus().softplus_values), [0.31326168751822286, 0.6931471805599453,
                                                            1.3132616875182228], "Correct!")


class TestSigmoid(unittest.TestCase):

    def testvalues_Sigmoid(self):
        self.assertEqual(list(Sigmoid().sigmoid_values), [0.2689414213699951, 0.5,
                                                          0.7310585786300049], "Correct!")


class TestGaussian(unittest.TestCase):

    def testvalues_Gaussian(self):
        self.assertEqual(list(Gaussian().gaussian_values), [0.36787944117144233, 1.0,
                                                            0.36787944117144233], "Correct!")


class TestTanh(unittest.TestCase):

    def testvalues_Tanh(self):
        self.assertEqual(list(Tanh().tanh_values), [-0.7615941559557649, 0.0, 0.7615941559557649], "Correct!")


if __name__ == "__main__":
    unittest.main()
