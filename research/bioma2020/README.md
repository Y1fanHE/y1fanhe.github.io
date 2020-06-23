---
layout : default
title : "Evolving Stability Parameters of Lévy Flight in Cuckoo Search"
permalink : /research/bioma2020/
mathjax: true
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-MML-AM_CHTML" async="" type="text/javascript"> </script>

# Evolving Stability Parameters of Lévy Flight in Cuckoo Search

Yifan He (1), Claus Aranha (2), Tetsuya Sakurai (3) @ University of Tsukuba

1. he.yifan.xs@alumni.tsukuba.ac.jp
2. caranha@cs.tsukuba.ac.jp
3. sakurai@cs.tsukuba.ac.jp

- [Evolving Stability Parameters of Lévy Flight in Cuckoo Search](#evolving-stability-parameters-of-lévy-flight-in-cuckoo-search)
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

- \\(F_1\\): [Sphere](../../projects/pybenchfcn/single-objective-optimization/README.md#f52-sphere)
- \\(F_2\\): [Sum Squares](../../projects/pybenchfcn/single-objective-optimization/README.md#f54-sum-squares)
- \\(F_3\\): [Rosenbrock](../../projects/pybenchfcn/single-objective-optimization/README.md#f41-rosenbrock)
- \\(F_4\\): [Zakharov](../../projects/pybenchfcn/single-objective-optimization/README.md#f61-zakharov)
- \\(F_5\\): [Ackley](../../projects/pybenchfcn/single-objective-optimization/README.md#f1-ackley)
- \\(F_6\\): [Alpine N.1](../../projects/pybenchfcn/single-objective-optimization/README.md#f5-alpine-n1)
- \\(F_7\\): [Periodic](../../projects/pybenchfcn/single-objective-optimization/README.md#f34-periodic)
- \\(F_8\\): [Styblinski-Tank](../../projects/pybenchfcn/single-objective-optimization/README.md#f53-styblinski-tank)
- \\(F_9\\): [Rastrigin](../../projects/pybenchfcn/single-objective-optimization/README.md#f39-rastrigin)
- \\(F_{10}\\): [Griewank](../../projects/pybenchfcn/single-objective-optimization/README.md#f25-griewank)
- \\(F_{11}\\): [Schwefel](../../projects/pybenchfcn/single-objective-optimization/README.md#f51-schwefel)
- \\(F_{12}\\): [Salomon](../../projects/pybenchfcn/single-objective-optimization/README.md#f42-salomon)
- \\(F_{13}\\): [Xin-She Yang's N.2](../../projects/pybenchfcn/single-objective-optimization/README.md#f58-xin-she-yangs-n2)
- \\(F_{14}\\): [Xin-She Yang's N.4](../../projects/pybenchfcn/single-objective-optimization/README.md#f60-xin-she-yangs-n4)

### Tolerance

- For CS-based algorithms

| Benchmark | Tolerance | Benchmark | Tolerance |
| :-------: | :-------: | :-------: | :-------: |
| F1        | 8E-12     | F8        | 2E-09     |
| F2        | 3E-10     | F9        | 4E-08     |
| F3        | 2E+01     | F10       | 2E-02     |
| F4        | 2E-03     | F11       | 2E-06     |
| F5        | 4E-06     | F12       | 7E-01     |
| F6        | 2E-07     | F13       | 4E-12     |
| F7        | 2E-01     | F14       | 1E+00     |

- For DE-based algorithms

| Benchmark | Tolerance | Benchmark | Tolerance |
| :-------: | :-------: | :-------: | :-------: |
| F1        | 1E-12     | F8        | 0E+00     |
| F2        | 1E-12     | F9        | 0E+00     |
| F3        | 0E+00     | F10       | 0E+00     |
| F4        | 1E-12     | F11       | 0E+00     |
| F5        | 1E-12     | F12       | 1E-01     |
| F6        | 1E-12     | F13       | 4E-12     |
| F7        | 2E-01     | F14       | 1E+00     |

### Figures

## Other Information

- Paper
- Code

---

[Home](/) > [Research](/research/) > [Evolving Stability Parameters of Lévy Flight in Cuckoo Search](/research/bioma2020/)