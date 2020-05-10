---
layout : default
title : 'PyBenchFCN'
permalink : /projects/pybenchfcn
---

# PyBenchFCN

PyBenchFCN is a python 3 library which includes a group of optimization benchmarks, as well as convenience tools.

- [Installation](#installation)
- [Usage](#usage)

## Installation

PyBenchFCN can be installed through PyPI with the following command.

```
pip install PyBenchFCN
```

## Usage

### Classical Single-Objective Optimization

There are three ways to initialize a problem with PyBenchFCN. For example, you can create a 10-dimensional Ackley problem using the following code.

```python3
n_var = 10                                      # dimension of problem

# Method 1 #
from PyBenchFCN import SingleObjectiveProblem as SOP
problem = SOP.ackleyfcn(n_var)                  # Ackley problem

# Method 2 #
from PyBenchFCN import Factory
problem = Factory.set_sop("f1", n_var)

# Method 3 #
problem = Factory.set_sop("ackley", n_var)
```

To check the information of the problem, you can try the following code.

```python
print( np.round(problem.optimalF, 5) )          # show rounded optimal value
xl, xu = problem.boundaries                     # bound of problem
```

The solution of a classical single-objective optimization problem is coded as 1-d array.

```python
import numpy as np
x = np.random.uniform(xl, xu, n_var)            # initialize a solution
print( problem.f(x) )                           # show fitness value as scalar
```

You can also create a population of solutions as a matrix.

```python
n_pop = 3                                       # size of population
X = np.random.uniform( xl, xu, (n_pop, n_var) ) # initialize a population
print( problem.F(X) )                           # show fitness values as 1d-array
```
