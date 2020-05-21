---
layout : default
title : "Stochastic Process - Week 1.2"
permalink : /notes/stochastic-process/week-1.2/
mathjax: true
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-MML-AM_CHTML" async="" type="text/javascript"> </script>

# Stochastic Process - Week 1.2 Renewal Process

- [Stochastic Process - Week 1.2 Renewal Process](#stochastic-process---week-12-renewal-process)
  - [Renewal Process](#renewal-process)
  - [Convolution](#convolution)

## Renewal Process

- **Definition**

$$S_0=0,S_n=S_{n-1}+\xi_n$$

$$\xi_1,\xi_2,\cdots,\xi_n\text{ - i.i.d.} > 0$$

$$\mathbb{P}\left\{\xi_1 > 0\right\}=1\Rightarrow F(0)=0$$

$$N_t=\max_k\left\{S_k\leq t\right\}$$

![Renewal Process](./renewal_process.svg)

- **Renewal times:** \\(S_0, S_1, \cdots\\)
- **Interarrival times:** \\(\xi_1, \xi_2, \cdots\\)
- **Properties:**
  - \\(S_n=\xi_1+\xi_2+\cdots+\xi_n\\)
  - \\( \left\\{S_n > t\right\\}=\left\\{N_t < n\right\\} \\)

## Convolution

- **Definition**

$$\text{Assume }X\perp\!\!\!\!\perp Y,$$

$$\forall X\sim F_X,\ Y\sim F_Y: \\F_X \star F_Y=F_{X+Y}(x)=\int_{\mathbb{R}}F_X(x-y)dF_Y(y)$$

$$\forall X\sim P_X,\ Y\sim P_Y: \\P_X \circ P_Y=P_{X+Y}(x)=\int_{\mathbb{R}}P_X(x-y)P_Y(y)dy$$

- **E.g.**

$$X\sim\exp(\lambda),\ Y\sim\exp(\mu)$$

$$P_{X+Y} = ?$$

- **Solution**

$$\forall x>0: P_X(x)=\lambda e^{-\lambda x},\ P_Y(x)=\mu e^{-\mu x}$$

$$
P_{X+Y}(x)=\int_{\mathbb{R}}P_X(x-y)P_Y(y)dy \\
=\begin{cases}
\int_{\mathbb{R}}\lambda e^{-\lambda(x-y)} \mu e^{-\lambda y}dy, & x>y>0 \\
0, & \text{otherwise}
\end{cases} \\
= \lambda\mu e^{-\lambda x} \int_0^x e^{(\lambda-\mu)y}dy = \lambda\mu e^{-\lambda x}\cdot\frac{1}{\lambda-\mu} \cdot e^{(\lambda-\mu)y} \Big\vert_0^x \\
=\frac{\lambda\mu}{\lambda-\mu}(e^{-\mu x} - e^{-\lambda x})
$$

- **Properties of convolution**
  1. \\(F^{n\star}(x) \leq F^n(x),\\) if \\(F(0)=0\\) and \\(\xi_1,\cdots\xi_n\text{ i.i.d. }\sim F\\)
  2. \\(F^{n\star} \geq F^{(n+1)\star},\\) if \\(F(0)=0\\) and \\(\xi_1,\cdots\xi_n\text{ i.i.d. }\sim F\\)
- **Theorems for a renewal process**
  1. \\(U(t)=\sum_{n=1}^\infty F^{n\star}(t)<\infty\\)
  2. \\(\mathbb{E}\left\\{N_t\right\\}=U(t)$\\)

---

[Home](/) > [Notes](/notes/) > [Stochastic Process](/notes/stochastic-process/) > [Week 1.2](/notes/stochastic-process/week-1.2/)