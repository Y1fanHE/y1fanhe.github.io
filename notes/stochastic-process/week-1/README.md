---
layout : default
title : "Stochastic Process - Week 1"
permalink : /notes/stochastic-process/week-1/
mathjax: true
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-MML-AM_CHTML" async="" type="text/javascript"> </script>

# Stochastic Process - Week 1

- [Stochastic Process - Week 1](#stochastic-process---week-1)
  - [Difference between Deterministic and Stochastic World](#difference-between-deterministic-and-stochastic-world)
  - [Stochastics (with an Example of Fish Pound)](#stochastics-with-an-example-of-fish-pound)
    - [Probability Theory](#probability-theory)
    - [Mathematical Statistics](#mathematical-statistics)
    - [Stochastic Process](#stochastic-process)

## Difference between Deterministic and Stochastic World

- **Single variable**
  - Deterministic: \\(\mathbb{R}\\)
    - E.g. temperature of a sick man: \\(T=39\\)
  - Stochastic: random variable
    - E.g. temperature of a sick man: \\( E(T)=38.5,\ Var(T)=0.8 \\)
- **Variable changing over time**
  - Deterministic: \\(\mathbb{R}_{+}\rightarrow\mathbb{R}\\)
    - E.g. temperature of a sick man: \\( T(1)=39, T(2)=38.5, \cdots \\)
  - Stochastic: stochastic process

## Stochastics (with an Example of Fish Pound)

### Probability Theory

\\(N\\) - number of fishes, \\(E\\), \\(Var\\), limit law, ...

### Mathematical Statistics

\\(N\\) fishes in total

1. Take \\(M\\) fishes, label them and put back. Now, we have \\(M\\) labeled fishes and \\(N-M\\) unlabeled fishes.
2. Take \\(n\\) fishes agian from the same pound. Assume we have \\(m\\) labeled fishes and \\(n-m\\) unlabeled fishes.
3. Probability of having \\(m\\) labeled fishes can be calculated as follows.

$$\mathbb{P}_m=\mathbb{P}(\text{number of labeled}=m)=\frac{C_M^m C_{N-M}^{n-m}}{C_N^M}$$

4. Repeat Step 2 and 3 \\(q\\) times. Then, we have \\(\mathbb{P}_{m_i}, i=1,\cdots,q\\).
5. Estimate \\(N\\) based on maximum likelihood.

### Stochastic Process


---

[Home](/) > [Notes](/notes/) > [Stochastic Process](/notes/stochastic-process/) > [Week 1](/notes/stochastic-process/week-1/)