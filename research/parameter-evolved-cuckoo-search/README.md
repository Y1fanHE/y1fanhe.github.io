---
layout : default
title : "Evolving Stability Parameters of Lévy Flight in Cuckoo Search"
permalink : /projects/research/parameter-evolved-cuckoo-search/
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
    - [Parameter Evolved Self-Adaption (PESA)](#parameter-evolved-self-adaption-pesa)
    - [JADE-like Self-Adaption (JASA)](#jade-like-self-adaption-jasa)
  - [Experiments](#experiments)
    - [Testing Benchmarks](#testing-benchmarks)
    - [Experimental Settings](#experimental-settings)
    - [Experimental Results](#experimental-results)
  - [Other Information](#other-information)

## Algorithms

### Parameter Evolved Self-Adaption (PESA)

- **General Framework of PESA**

1. Initialize solution population \\(\left\{ x_1,\dots,x_N \right\}\\);
2. Initialize parameter population \\(\left\{ p_1,\dots,p_N \right\}\\);
3. Evaluate fitness of solutions \\(\left\{ f_1,\dots,f_N \right\}\\);
4. **WHILE** termination criteria is not satisfied **DO**
    1. **FOR** \\(t\\)-th generation in continuous \\(n_{step}\\) generations **DO**
        1. **FOR** \\(x_i\\) in solution population **DO**
            1. Evolve \\(x_i\\) to get offspring \\(x_i'\\) with \\(p_i\\);
            1. Record \\(x_i^{(t)}\\), \\(x_i'^{(t)}\\), \\(f_i^{(t)}\\), \\(f_i'^{(t)}\\);
        1. **END FOR**
    1. **END FOR**
    2. Compute fitness of parameters \\(I_i = g \left\{ x_{1\dots N}^{(\dots)}, x_{1\dots N}'^{(\dots)}, f_{1\dots N}^{(\dots)}, f_{1\dots N}'^{(\dots)} \right\}\\);
    1. Evolve \\(p_i\\) based on another EA;
5. **END WHILE**

- **Parameter Evolved Cuckoo Search (PECS)**

- **Parameter Evolved Differential Evolution (PEDE)**

### JADE-like Self-Adaption (JASA)

- **General Framework of JASA**

- **JADE-like Cuckoo Seach (JACS)**

- **JADE**

## Experiments

### Testing Benchmarks

### Experimental Settings

### Experimental Results

## Other Information

- Paper
- Code

---

[Home](/) > [Research](/research/) > [Evolving Stability Parameters of Lévy Flight in Cuckoo Search](/projects/research/parameter-evolved-cuckoo-search/)