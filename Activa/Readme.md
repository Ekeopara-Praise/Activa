# Activa Python Package

Activa is a Python package that calculates the activation functions of a set of input 
numerical values while outputting clear visualization of these values for further analysis.

## Features of Activa
- Calculates activation functions (ReLU, Sigmoid, Logistic, Softplus, Gaussian)
- Provides visual displays of each function against it's derivatives
- Outputs a comparison table for each values across all activation functions available

## Quick Start
First, install the library:

```
$ pip install Activa
```

## Example
For the example, we will be using the default data in the package, data = [-1, 0, 1]
```
>> from Activa import ReLU, Sigmoid, Gaussian, Table

>> relu = ReLU()
>> relu.relu_values
array([0, 0, 1])

>> sig = Sigmoid()
>> sig.sigmoid_values
array([0.26894142, 0.5       , 0.73105858])

>> gs = Gaussian()
>> gs.gaussian_values
array([0.36787944, 1.        , 0.36787944])

>> tb = Table()
>> tb.show
   actual_values   sigmoid  relu      tanh  softplus  gaussian
0             -1  0.268941     0 -0.761594  0.313262  0.367879
1              0  0.500000     0  0.000000  0.693147  1.000000
2              1  0.731059     1  0.761594  1.313262  0.367879

```

## More information
Kindly checkout the [github repo](https://github.com/Ekeopara-Praise/Activa) for more updates
