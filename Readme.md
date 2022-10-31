Activa is a Python package that calculates the activation functions of a set of input 
numerical values while outputting clear visualization of these values for further analysis.

## Features of Activa
- Calculates activation functions (ReLU, Sigmoid, Tanh, Softplus, Gaussian)
- Provides visual displays of each function against it's derivatives
- Outputs a comparison table for each values across all activation functions available

## Quick Start
First, install the library:

```
$ pip install Activa
```

## Example 1 - Terminal
For the example, we will be using the default data in the package, data = [-1, 0, 1]

To import libraries
```
>> from Activa import ReLU, Sigmoid, Gaussian, Table
```

1. Implementing the **ReLU** activation function
```
>> relu = ReLU()
>> relu.relu_values
array([0, 0, 1])
```

2. Implementing the **Sigmoid** activation function

```
>> sig = Sigmoid()
>> sig.sigmoid_values
array([0.26894142, 0.5       , 0.73105858])
```
3. Implementing the **Gaussian** activation function
```
>> gs = Gaussian()
>> gs.gaussian_values
array([0.36787944, 1.        , 0.36787944])
```

4. Implementing the **comparison table** for all activation functions
```
>> tb = Table()
>> tb.show
   actual_values   sigmoid  relu      tanh  softplus  gaussian
0             -1  0.268941     0 -0.761594  0.313262  0.367879
1              0  0.500000     0  0.000000  0.693147  1.000000
2              1  0.731059     1  0.761594  1.313262  0.367879

```
## Example 2 - Jupyter notebook
We start by importing the necessary libraries
![image.png](https://github.com/Ekeopara-Praise/Personal_Lessons/blob/master/Object%20Oriented%20Programming%20in%20Python/Unit_Testing/Activa%20-%20Pictures/imports.PNG)

Lets load our data for the example
![image.png](https://github.com/Ekeopara-Praise/Personal_Lessons/blob/master/Object%20Oriented%20Programming%20in%20Python/Unit_Testing/Activa%20-%20Pictures/data.PNG)

### [ReLU](https://github.com/Ekeopara-Praise/Activa/blob/master/Activa/ReLUFunction.py)
Next, we can now calculate the **ReLU values** for the data
![image.png](https://github.com/Ekeopara-Praise/Personal_Lessons/blob/master/Object%20Oriented%20Programming%20in%20Python/Unit_Testing/Activa%20-%20Pictures/ReLU%20values.PNG)

Also, we can make visualizations for both the ReLU function and its derivatives
![image.png](https://github.com/Ekeopara-Praise/Personal_Lessons/blob/master/Object%20Oriented%20Programming%20in%20Python/Unit_Testing/Activa%20-%20Pictures/RELUplots.PNG)

### [Sigmoid](https://github.com/Ekeopara-Praise/Activa/blob/master/Activa/SigmoidFunction.py)
For the Sigmoid activation function, we can now also calculate the **Sigmoid values** for the data
![image.png](https://github.com/Ekeopara-Praise/Personal_Lessons/blob/master/Object%20Oriented%20Programming%20in%20Python/Unit_Testing/Activa%20-%20Pictures/SIgmoid.PNG)

Also, we can make visualizations for both the Sigmoid function and its derivatives
![image.png](https://github.com/Ekeopara-Praise/Personal_Lessons/blob/master/Object%20Oriented%20Programming%20in%20Python/Unit_Testing/Activa%20-%20Pictures/Sigmoidplots.PNG)

### [Comparison Table](https://github.com/Ekeopara-Praise/Activa/blob/master/Activa/ComboTable.py)
We can also view the comparison table for all of the available activation functions across their actual values.
![image.png](https://github.com/Ekeopara-Praise/Personal_Lessons/blob/master/Object%20Oriented%20Programming%20in%20Python/Unit_Testing/Activa%20-%20Pictures/table.PNG)

## Activa Updates
Kindly checkout the [Package](https://pypi.org/project/Activa/) for more updates
