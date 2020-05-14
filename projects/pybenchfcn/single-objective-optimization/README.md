---
layout : default
title : "Classical Single-Objective Optimization"
permalink : /projects/pybenchfcn/single-objective-optimization/
mathjax: true
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-MML-AM_CHTML" async="" type="text/javascript"> </script>

# Classical Single-Objective Optimization

- [Classical Single-Objective Optimization](#classical-single-objective-optimization)
  - [f1: Ackley](#f1-ackley)
  - [f2: Ackley N.2](#f2-ackley-n2)
  - [f3: Ackley N.3](#f3-ackley-n3)
  - [f4: Adjiman](#f4-adjiman)
  - [f5: Alpine N.1](#f5-alpine-n1)
  - [f6: Alpine N.2](#f6-alpine-n2)
  - [f7: Bartels Conn](#f7-bartels-conn)
  - [f8: Beale](#f8-beale)
  - [f9: Bird](#f9-bird)
  - [f10: Bohachevsky N.1](#f10-bohachevsky-n1)
  - [f11: Bohachevsky N.2](#f11-bohachevsky-n2)
  - [f12: Booth](#f12-booth)
  - [f13: Brent](#f13-brent)
  - [f14: Brown](#f14-brown)
  - [f15: Bulkin N.6](#f15-bulkin-n6)
  - [f16: Cross-in-Tray](#f16-cross-in-tray)
  - [f17: Deckkers-Aarts](#f17-deckkers-aarts)

## f1: Ackley

$$f(\mathbf{x}) = -20\exp(-0.2\sqrt{\frac{1}{n}\sum_{i=1}^{n}x_i^2})-\exp(\frac{1}{n}\sum_{i=1}^{n}\cos 2\pi x_i)+ 20 + \exp(1)$$

$$x_i\in[-32,32]$$

<p align="center"><a href="./images/f1_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f1_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f2: Ackley N.2

$$f(x, y) = -200e^{-0.2\sqrt{x^2 + y^2}}$$

$$x,y\in[-32,32]$$

<p align="center"><a href="./images/f2_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f2_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       | &#10004; |           |            |        |

## f3: Ackley N.3

$$f(x, y) = -200e^{-0.2\sqrt{x^2 + y^2}} + 5e^{\cos 3x + \sin 3y}$$

$$x,y\in[-32,32]$$

<p align="center"><a href="./images/f3_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f3_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       | &#10004; |           |            |        |

## f4: Adjiman

$$f(x, y)=\cos x\sin y - \frac{x}{y^2+1}$$

$$x\in [-1,2],\ y\in [-1,1]$$

<p align="center"><a href="./images/f4_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f4_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f5: Alpine N.1

$$f(\mathbf{x})=\sum_{i=1}^{n}|x_i \sin x_i+0.1x_i|$$

$$x_i\in[0,10]$$

<p align="center"><a href="./images/f5_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f5_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
|                |          | &#10004;  |            |        |

## f6: Alpine N.2

$$f(\mathbf{x})=\prod_{i=1}^{n}\sqrt{x_i}\sin x_i$$

$$x_i\in[0,10]$$

<p align="center"><a href="./images/f6_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f6_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          | &#10004;  |            |        |

## f7: Bartels Conn

$$f(x,y)=|x^2 + y^2 + xy| + |\sin x| + |\cos y|$$

$$x,y\in[-500,500]$$

<p align="center"><a href="./images/f7_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f7_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
|                |          |           |            |        |

## f8: Beale

$$f(x, y) = (1.5-x+xy)^2+(2.25-x+xy^2)^2+(2.625-x+xy^3)^2$$

$$x,y\in[-4.5,4.5]$$

<p align="center"><a href="./images/f8_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f8_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       | &#10004; |           |            |        |

## f9: Bird

$$f(x, y) = \sin x e^{(1-\cos y)^2}+\cos y e^{(1-\sin x)^2}+(x-y)^2$$

$$x,y\in[-2\pi,2\pi]$$

<p align="center"><a href="./images/f9_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f9_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f10: Bohachevsky N.1

$$f(x, y) = x^2 + 2y^2 -0.3\cos 3\pi x-0.4\cos 4\pi y+0.7$$

$$x,y\in[-100,100]$$

<p align="center"><a href="./images/f10_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f10_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          | &#10004;  |            |        |

## f11: Bohachevsky N.2

$$f(x, y)=x^2 + 2y^2 -0.3\cos 3\pi x\cos 4\pi y+0.3$$

$$x,y\in[-100,100]$$

<p align="center"><a href="./images/f11_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f11_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f12: Booth

$$f(x,y)=(x+2y-7)^2+(2x+y-5)^2$$

$$x,y\in[-10,10]$$

<p align="center"><a href="./images/f12_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f12_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       | &#10004; |           |            |        |

## f13: Brent

$$f(x, y) = (x + 10)^2 + (y + 10)^2 + e^{-x^2 - y^2}$$

$$x,y\in[-20,0]$$

<p align="center"><a href="./images/f13_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f13_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       | &#10004; |           |            |        |

## f14: Brown

$$f(\mathbf{x}) = \sum_{i=1}^{n-1}(x_i^2)^{(x_{i+1}^{2}+1)}+(x_{i+1}^2)^{(x_{i}^{2}+1)}$$

$$x_i\in[-1,4]$$

<p align="center"><a href="./images/f14_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f14_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       | &#10004; |           |            |        |

## f15: Bulkin N.6

$$f(x,y)=100\sqrt{|y-0.01x^2|}+0.01|x+10|$$

$$x\in[-15,-5],\ y\in[-3,3]$$

<p align="center"><a href="./images/f15_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f15_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
|                |          |           |            |        |

## f16: Cross-in-Tray

$$f(x,y)=-0.0001(|\sin x\sin y \exp(|100-\frac{\sqrt{x^2+y^2}}{\pi}|)|+1)^{0.1}$$

$$x,y\in[-10,10]$$

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
|                |          |           |            |        |

## f17: Deckkers-Aarts

$$f(x,y) = 10^5x^2 + y^2 -(x^2 + y^2)^2 + 10^{-5}(x^2 + y^2)^4$$

$$x,y\in[-20,20]$$

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

---

[Home](/) > [Projects](/projects/) > [PyBenchFCN](/projects/pybenchfcn/) > [Classical Single-Objective Optimization](/projects/pybenchfcn/single-objective-optimization/)