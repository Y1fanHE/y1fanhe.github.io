---
layout : default
title : "Program Synthesis"
permalink : /research/program-synthesis/
mathjax: true
---

# Adaptive Knowledge-Driven Program Synthesis

## Program Synthesis

*Program synthesis* (PS), also known as the automatic programming, refers to a computer program that holds the ability to write programs without human effort. A computer program holds the following two charasteristics.

1. A program is a sequence of basic instructions.
2. A program can perform a specific task.

In terms of optimization, the first charasteristic defines the domain of the search space (i.e., all feasible programs). The basic instructions are the instructions that cannot be divided anymore (or the user don't want to divide). As an example, I show a Lisp-like program below.

```clojure
1 2 + 3 * 4 max
```

This program contains 7 basic instructions, `1`, `2`, `3`, `+`, `*`, and `max`. The programs performs as $\max[(1+2)\times{3}, 4]=9$.

The second one defines the objective function. However, this objective function is not defined as straightly as the search space.

In this study, we are going to do example-based program synthesis. The sentence "perform a specific task" is the same as passing a set of given I/O data. For example, a program to perform sorting should pass the following I/O data.

- input=[2,0,3,1,4], output=[0,1,2,3,4]
- input=[0,1,2,3], output=[0,1,2,3]
- input=[0,0,2,1,4], output=[0,0,1,2,4]
- ...

Indeed, we cannot give all possible examples, as they are infinite. So we usually give a subset of example I/O data. Therefore, the ovjective function can be computed as the sum of finite errors between actual output of the generated programs and the expected output of the correct programs, under the same set of inputs. For the above example, we can calculate the error with hamming distance.

- actual=[2,2,1,3,4], expected=[0,1,2,3,4]
- actual=[0,1,2,3], expected=[0,1,2,3]
- actual=[0,2,1,4,0], expected=[0,0,1,2,4]

The error is $3+0+4=7$.

**The mathematical formulation of PS is defined as follows.**

Given a set of basic instructions $\mathbb{B}$, I/O data $\{(x_k,y_k)\}_{k=1,\dots,M}$, solve the following optimization problem.

$$
p^* = \arg\min_{p\in{P_{\mathbb{B}}}} \Sigma_{i}^{i=M} || p(x_i) - y_i ||
$$

$p$: program $\quad$ $p^*$: optimal program
$P_{\mathbb{B}}$: all feasible program based on instruction set $\mathbb{B}$
$x_i$: $i$-th input $\quad$ $y_i$: $i$-th output

## Genetic Programming


