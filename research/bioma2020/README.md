---
layout : default
title : "Parameter Evolution Self-Adaptive Strategy and its Application in Cuckoo Search"
permalink : /research/bioma2020/
mathjax: true
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-MML-AM_CHTML" async="" type="text/javascript"> </script>

# Parameter Evolution Self-Adaptive Strategy and its Application in Cuckoo Search

Yifan He (1), Claus Aranha (2), Tetsuya Sakurai (3) @ University of Tsukuba

1. [he.yifan.xs@alumni.tsukuba.ac.jp](mailto:he.yifan.xs@alumni.tsukuba.ac.jp)
2. [caranha@cs.tsukuba.ac.jp](mailto:he.yifan.xs@alumni.tsukuba.ac.jp)
3. [sakurai@cs.tsukuba.ac.jp](mailto:he.yifan.xs@alumni.tsukuba.ac.jp)

This webpage contains details and supplement of algorithms, experimental settings, figures, and code for manuscript "Parameter Evolution Self-Adaptive Strategy and its Application in Cuckoo Search".

- [Parameter Evolution Self-Adaptive Strategy and its Application in Cuckoo Search](#parameter-evolution-self-adaptive-strategy-and-its-application-in-cuckoo-search)
  - [Algorithms](#algorithms)
    - [PESA](#pesa)
    - [PECS](#pecs)
    - [PEDE](#pede)
    - [JASA](#jasa)
    - [JACS](#jacs)
    - [JADE](#jade)
  - [Experiments](#experiments)
    - [Benchmarks](#benchmarks)
    - [Tolerance](#tolerance)
    - [Figures](#figures)
  - [Other Information](#other-information)

## Algorithms


### PESA 

![PESA](images/algorithms/pesa.svg)

### PECS

![PECS](images/algorithms/pecs.svg)

### PEDE

![PEDE](images/algorithms/pede.svg)

### JASA

![JASA](images/algorithms/jasa.svg)

### JACS

![JACS](images/algorithms/jacs.svg)

### JADE

![JADE](images/algorithms/jade.svg)

## Experiments

### Benchmarks

- \\(F_1\\): [Sphere](/projects/pybenchfcn/single-objective-optimization/README.md#f52-sphere)
- \\(F_2\\): [Sum Squares](/projects/pybenchfcn/single-objective-optimization/README.md#f54-sum-squares)
- \\(F_3\\): [Rosenbrock](/projects/pybenchfcn/single-objective-optimization/README.md#f41-rosenbrock)
- \\(F_4\\): [Zakharov](/projects/pybenchfcn/single-objective-optimization/README.md#f61-zakharov)
- \\(F_5\\): [Ackley](/projects/pybenchfcn/single-objective-optimization/README.md#f1-ackley)
- \\(F_6\\): [Alpine N.1](/projects/pybenchfcn/single-objective-optimization/README.md#f5-alpine-n1)
- \\(F_7\\): [Periodic](/projects/pybenchfcn/single-objective-optimization/README.md#f34-periodic)
- \\(F_8\\): [Styblinski-Tank](/projects/pybenchfcn/single-objective-optimization/README.md#f53-styblinski-tank)
- \\(F_9\\): [Rastrigin](/projects/pybenchfcn/single-objective-optimization/README.md#f39-rastrigin)
- \\(F_{10}\\): [Griewank](/projects/pybenchfcn/single-objective-optimization/README.md#f25-griewank)
- \\(F_{11}\\): [Schwefel](/projects/pybenchfcn/single-objective-optimization/README.md#f51-schwefel)
- \\(F_{12}\\): [Salomon](/projects/pybenchfcn/single-objective-optimization/README.md#f42-salomon)
- \\(F_{13}\\): [Xin-She Yang's N.2](/projects/pybenchfcn/single-objective-optimization/README.md#f58-xin-she-yangs-n2)
- \\(F_{14}\\): [Xin-She Yang's N.4](/projects/pybenchfcn/single-objective-optimization/README.md#f60-xin-she-yangs-n4)

### Tolerance

- **For CS-based algorithms**

| Benchmark | Tolerance   | Benchmark     | Tolerance   |
| :-------: | :---------: | :-----------: | :---------: |
| \\(F_1\\)  | \\(8e-12\\) | \\(F_8 \\)   | \\(2e-09\\) |
| \\(F_2\\)  | \\(3e-10\\) | \\(F_9 \\)   | \\(4e-08\\) |
| \\(F_3\\)  | \\(2e+01\\) | \\(F_{10}\\) | \\(2e-02\\) |
| \\(F_4\\)  | \\(2e-03\\) | \\(F_{11}\\) | \\(2e-06\\) |
| \\(F_5\\)  | \\(4e-06\\) | \\(F_{12}\\) | \\(7e-01\\) |
| \\(F_6\\)  | \\(2e-07\\) | \\(F_{13}\\) | \\(4e-12\\) |
| \\(F_7\\)  | \\(2e-01\\) | \\(F_{14}\\) | \\(1e+00\\) |

- **For DE-based algorithms**

| Benchmark | Tolerance   | Benchmark     | Tolerance   |
| :-------: | :---------: | :-----------: | :---------: |
| \\(F_1\\)  | \\(1e-12\\) | \\(F_8\\)    | \\(0e+00\\) |
| \\(F_2\\)  | \\(1e-12\\) | \\(F_9\\)    | \\(0e+00\\) |
| \\(F_3\\)  | \\(0e+00\\) | \\(F_{10}\\) | \\(0e+00\\) |
| \\(F_4\\)  | \\(1e-12\\) | \\(F_{11}\\) | \\(0e+00\\) |
| \\(F_5\\)  | \\(1e-12\\) | \\(F_{12}\\) | \\(1e-01\\) |
| \\(F_6\\)  | \\(1e-12\\) | \\(F_{13}\\) | \\(4e-12\\) |
| \\(F_7\\)  | \\(2e-01\\) | \\(F_{14}\\) | \\(1e+00\\) |

### Figures

- **\\(F_1\\): Sphere**
  - PECS vs. JACS [<a href="images/results/sacs/sphere.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/sphere.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/sphere.svg" target="_blank">SVG</a>]
- **\\(F_2\\): Sum Squares**
  - PECS vs. JACS [<a href="images/results/sacs/sumsquares.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/sumsquares.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/sumsquares.svg" target="_blank">SVG</a>]
- **\\(F_3\\): Rosenbrock**
  - PECS vs. JACS [<a href="images/results/sacs/rosenbrock.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/rosenbrock.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/rosenbrock.svg" target="_blank">SVG</a>]
- **\\(F_4\\): Zakharov**
  - PECS vs. JACS [<a href="images/results/sacs/zakharov.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/zakharov.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/zakharov.svg" target="_blank">SVG</a>]
- **\\(F_5\\): Ackley**
  - PECS vs. JACS [<a href="images/results/sacs/ackley.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/ackley.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/ackley.svg" target="_blank">SVG</a>]
- **\\(F_6\\): Alpine N.1**
  - PECS vs. JACS [<a href="images/results/sacs/alpinen1.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/alpinen1.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/alpinen1.svg" target="_blank">SVG</a>]
- **\\(F_7\\): Periodic**
  - PECS vs. JACS [<a href="images/results/sacs/periodic.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/periodic.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/periodic.svg" target="_blank">SVG</a>]
- **\\(F_8\\): Styblinski-Tank**
  - PECS vs. JACS [<a href="images/results/sacs/styblinskitank.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/styblinskitank.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/styblinskitank.svg" target="_blank">SVG</a>]
- **\\(F_9\\): Rastrigin**
  - PECS vs. JACS [<a href="images/results/sacs/rastrigin.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/rastrigin.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/rastrigin.svg" target="_blank">SVG</a>]
- **\\(F_{10}\\): Griewank**
  - PECS vs. JACS [<a href="images/results/sacs/griewank.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/griewank.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/griewank.svg" target="_blank">SVG</a>]
- **\\(F_{11}\\): Schwefel**
  - PECS vs. JACS [<a href="images/results/sacs/schwefel.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/schwefel.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/schwefel.svg" target="_blank">SVG</a>]
- **\\(F_{12}\\): Salomon**
  - PECS vs. JACS [<a href="images/results/sacs/salomon.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/salomon.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/salomon.svg" target="_blank">SVG</a>]
- **\\(F_{13}\\): Xin-She Yang's N.2**
  - PECS vs. JACS [<a href="images/results/sacs/xinsheyangn2.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/xinsheyangn2.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/xinsheyangn2.svg" target="_blank">SVG</a>]
- **\\(F_{14}\\): Xin-She Yang's N.4**
  - PECS vs. JACS [<a href="images/results/sacs/xinsheyangn4.svg" target="_blank">SVG</a>]
  - PEDE vs. JADE [<a href="images/results/sade/xinsheyangn4.svg" target="_blank">SVG</a>]
  - PECS with different \\(n_{step}\\) [<a href="images/results/pecs/xinsheyangn4.svg" target="_blank">SVG</a>]

## Other Information

- Paper
- Code [<a href="https://github.com/Y1fanHE/bioma2020" target="_blank">GitHub</a>]

---

[Home](/) > [Research](/research/) > [Parameter Evolution Self-Adaptive Strategy and its Application in Cuckoo Search](/research/bioma2020/)