---
layout : default
title : "Single-Objective Optimization"
permalink : /projects/pybenchfcn/single-objective-optimization/
mathjax: true
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-MML-AM_CHTML" async="" type="text/javascript"> </script>

# Classical Single-Objective Optimization

- [Classical Single-Objective Optimization](#classical-single-objective-optimization)
  - [Ackley](#ackley)
  - [Ackley N.2](#ackley-n2)
  - [Ackley N.3](#ackley-n3)
  - [Adjiman](#adjiman)
  - [Alpine N.1](#alpine-n1)
  - [Alpine N.2](#alpine-n2)
  - [Bartels Conn](#bartels-conn)
  - [Beale](#beale)
  - [Bird](#bird)
  - [Bohachevsky N.1](#bohachevsky-n1)
  - [Bohachevsky N.2](#bohachevsky-n2)
  - [Booth](#booth)
  - [Brent](#brent)
  - [Brown](#brown)

## Ackley

$$f(\mathbf{x}) = -20\exp(-0.2\sqrt{\frac{1}{n}\sum_{i=1}^{n}x_i^2})-\exp(\frac{1}{n}\sum_{i=1}^{n}\cos 2\pi x_i)+ 20 + \exp(1)$$

$$[-32,32]$$

## Ackley N.2

$$f(x, y) = -200e^{-0.2\sqrt{x^2 + y^2}}$$

$$[-32,32]$$

## Ackley N.3

$$f(x, y) = -200e^{-0.2\sqrt{x^2 + y^2}} + 5e^{\cos 3x + \sin 3y}$$

$$[-32,32]$$

## Adjiman

$$f(x, y)=\cos x\sin y - \frac{x}{y^2+1}$$

$$x\in [-1,2]\\ y\in [-1,1]$$

## Alpine N.1

$$f(\mathbf{x})=\sum_{i=1}^{n} \mid x_i \sin x_i+0.1x_i\mid$$

$$[0,10]$$

## Alpine N.2

$$f(\mathbf{x})=\prod_{i=1}^{n}\sqrt{x_i}\sin x_i$$

$$[0,10]$$

## Bartels Conn

$$f(x,y)=\mid x^2 + y^2 + xy\mid + \mid\sin x\mid + \mid\cos y\mid$$

$$[-500,500]$$

## Beale

$$f(x, y) = (1.5-x+xy)^2+(2.25-x+xy^2)^2+(2.625-x+xy^3)^2$$

$$[-4.5,4.5]$$

## Bird

$$f(x, y) = \sin x e^{(1-\cos y)^2}+\cos y e^{(1-\sin x)^2}+(x-y)^2$$

$$[-2\pi,2\pi]$$

## Bohachevsky N.1

$$f(x, y) = x^2 + 2y^2 -0.3\cos 3\pi x-0.4\cos 4\pi y+0.7$$

$$[-100,100]$$

## Bohachevsky N.2

$$f(x, y)=x^2 + 2y^2 -0.3\cos 3\pi x\cos 4\pi y+0.3$$

$$[-100,100]$$

## Booth

$$f(x,y)=(x+2y-7)^2+(2x+y-5)^2$$

$$[-10,10]$$

## Brent

$$f(x, y) = (x + 10)^2 + (y + 10)^2 + e^{-x^2 - y^2}$$

$$[-20,0]$$

## Brown

$$f(\textbf{x}) = \sum_{i=1}^{n-1}(x_i^2)^{(x_{i+1}^{2}+1)}+(x_{i+1}^2)^{(x_{i}^{2}+1)}$$

$$[-1,4]$$