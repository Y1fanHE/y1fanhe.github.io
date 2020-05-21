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

## Renewal Process

- **Definition**

$$S_0=0,S_n=S_{n-1}+\xi_n$$

$$\xi_1,\xi_2,\cdots,\xi_n > 0\ (i.i.d)$$

$$\mathbb{P}\left\{\xi_1 > 0\right\}=1\Rightarrow F(0)=0$$

$$N_t=\max_k\left\{S_k\leq t\right\}$$

![Renewal Process](./renewal_process.svg)

- Renewal times: \\(S_0, S_1, \cdots\\)
- Interarrival times: \\(\xi_1, \xi_2, \cdots\\)
- Properties:
  - \\(S_n=\xi_1+\xi_2+\cdots+\xi_n\\)
  - \\( \left\\{S_n > t\right\\}=\left\\{N_t < n\right\\} \\)

---

[Home](/) > [Notes](/notes/) > [Stochastic Process](/notes/stochastic-process/) > [Week 1.2](/notes/stochastic-process/week-1.2/)