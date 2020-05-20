---
layout : default
title : "Stochastic Process - Week 1"
permalink : /notes/stochastic-process/week-1/
mathjax: true
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-MML-AM_CHTML" async="" type="text/javascript"> </script>

# Stochastic Process - Week 1

- [Stochastic Process - Week 1](#stochastic-process---week-1)
  - [Deterministic and Stochastic World](#deterministic-and-stochastic-world)
  - [Stochastics](#stochastics)
    - [Probability Theory](#probability-theory)
    - [Mathematical Statistics](#mathematical-statistics)
    - [Stochastic Process](#stochastic-process)
  - [Probability Space](#probability-space)
  - [Stochastic Function](#stochastic-function)
  - [Trajectories and Finite Dimensional Distribution](#trajectories-and-finite-dimensional-distribution)

## Deterministic and Stochastic World

- **Single variable**
  - Deterministic: \\(\mathbb{R}\\)
    - E.g. temperature of a sick man: \\(T=39\\)
  - Stochastic: random variable
    - E.g. temperature of a sick man: \\( E(T)=38.5,\ Var(T)=0.8 \\)
- **Variable changing over time**
  - Deterministic: \\(\mathbb{R}_{+}\rightarrow\mathbb{R}\\)
    - E.g. temperature of a sick man: \\( T(1)=39, T(2)=38.5, \cdots \\)
  - Stochastic: stochastic process

## Stochastics 

Consider an example of fish pound,

### Probability Theory

\\(N\\) - number of fishes

- \\(E\\), \\(Var\\), limit law, ...

### Mathematical Statistics

\\(N\\) fishes in total

- Take \\(M\\) fishes, label them and put back. Now, we have \\(M\\) labeled fishes and \\(N-M\\) unlabeled fishes.
- Take \\(n\\) fishes agian from the same pound. Assume we have \\(m\\) labeled fishes and \\(n-m\\) unlabeled fishes.
- Probability of having \\(m\\) labeled fishes can be calculated as follows.

$$\mathbb{P}_m=\mathbb{P}\left\{\text{number of labeled}=m\right\}=\frac{C_M^m C_{N-M}^{n-m}}{C_N^M}$$

- Repeat Step 2 and 3 for \\(q\\) times. Then, we have \\(\mathbb{P}_{m_i},\ (i=1,\cdots,q)\\).
- Estimate \\(N\\) based on maximum log-likelihood as follows.

$$\max_{N} \sum_{i=1}^q \ln\left\{\mathbb{P}_{m_i}\right\}$$

### Stochastic Process

This topic will be introduced in the following weeks.

## Probability Space

A common notation is \\( (\Omega,\mathcal{F},\mathbb{P}) \\).

- **Bernouli scheme:** 1 - success; 0 - failure
  - Results of \\(n\\) repetition experiment: \\(\\{a_1,\cdots,a_n\\}, a_i\in\\{0,1\\}\\)
- **Samle space** \\(\Omega\\)
  - E.g. of Bernouli scheme: \\({\\{0,1\\}}^n\\)
  - size of \\(\Omega\\): \\(2^n\\)
- \\(\sigma\\)**-algebra** \\(\mathcal{F}\\)
  - Mathematical definition
    1. \\(\Omega\in\mathcal{F}\\)
    2. \\(A\in\mathcal{F}\Rightarrow\Omega\setminus A\in\mathcal{F}\\)
    3. \\(A_1,\cdots,A_n,\cdots\in\mathcal{F}\Rightarrow\bigcup_{i=1}^{\infty}A_i\in\mathcal{F}\\)
  - E.g. of Bernouli scheme: power set
  - size of \\(\mathcal{F}\\): \\(2^{2^n}\\)
- **Probability measure** \\(\mathbb{P}\\)
  - Mathematical definition
    1. \\(\mathbb{P}:\mathcal{F}\rightarrow[0,1]\\)
    2. \\(\mathbb{P}\\{\Omega\\}=1\\)
    3. \\(A_1,\cdots,A_n,\cdots\in\mathcal{F}\Rightarrow\mathbb{P}\\{\bigcup A_i\\}=\sum\mathbb{P}\\{A_i\\}\\)

## Stochastic Function

- **Random variable:** measurable function
  - \\(\xi:\Omega\rightarrow\mathbb{R}\\)
- **Random (Stochastic) function**
  - \\(X:T\times\Omega\rightarrow\mathbb{R}\\) is a stochastic function if \\(\forall t\in T\\), \\(X(t)\\) is a random variable in \\((\Omega,\mathcal{F},\mathbb{P})\\), where \\(T\\) is time.
  - \\(T=\mathbb{R}_{+}\\): stochastic process
    - \\(T=\mathbb{N}\ \text{or}\ \mathbb{Z}\\): stochastic process with discrete time
    - \\(T=\mathbb{R}_{+}\ \text{or}\ \mathbb{R}\\): stochastic process with continuous time
  - \\(T=\mathbb{R}_{+}^n\\): random field

## Trajectories and Finite Dimensional Distribution

- Trajectory (path): \\(T\rightarrow\mathbb{R}\\), \\(X(t)\\) with a fixed $\omega$
- Finite dimensional distribution: distribution of random vector \\((X(t_1), X(t_2),\cdots,X(t_n))\\), where \\(t_1,t_2,\cdots,t_n\in\mathbb{R}\\)
- E.g.

$$X(t)=\xi\cdot t$$

$$
\xi=\begin{cases}
1, & p=0.5 \\
2, & p=0.5
\end{cases}
$$

$$\mathbb{P}\left\{X(t_1)\leq x_1, X(t_2)\leq x_2\right\}=?$$

- Solution

$$\mathbb{P}\left\{X(t_1)\leq x_1, X(t_2)\leq x_2\right\}=\mathbb{P}\left\{\xi\leq\frac{x_1}{t_1}, \xi\leq\frac{x_2}{t_2}\right\}$$

The valid values of \\(\frac{x_1}{t_1}\\) and \\(\frac{x_2}{t_2}\\) are listed in 9 situations as follows. (None: either 1 or 2 is not valid, 1: only 1 is valid, All: both 1 and 2 are valid)

|            | [-inf,1) | [1,2) | [2,inf) |
| ---------- | :---: | :---: | :-----: |
|**[-inf,1)**| None  | None  | None    |
|**[1,2)**   | None  | 1     | 1       |
|**[2,inf)** | None  | 1     | All     |

Therefore, it is clear that

$$
\mathbb{P}\left\{X(t_1)\leq x_1, X(t_2)\leq x_2\right\}=\begin{cases}
0, & \min\left\{\frac{x_1}{t_1}, \frac{x_2}{t_2}\right\} \in [-\infty,1) \\
0.5, & \min\left\{\frac{x_1}{t_1}, \frac{x_2}{t_2}\right\} \in [1,2) \\
1, & \min\left\{\frac{x_1}{t_1}, \frac{x_2}{t_2}\right\} \in [2,\infty)
\end{cases}
$$

---

[Home](/) > [Notes](/notes/) > [Stochastic Process](/notes/stochastic-process/) > [Week 1](/notes/stochastic-process/week-1/)