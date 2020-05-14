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
  - [f18: Drop-Wave](#f18-drop-wave)
  - [f19: Easom](#f19-easom)
  - [f20: Egg Crate](#f20-egg-crate)
  - [f21: Eggholder](#f21-eggholder)
  - [f22: Exponential](#f22-exponential)
  - [f23: Goldstein-Price](#f23-goldstein-price)
  - [f24: Gramacy & Lee](#f24-gramacy--lee)
  - [f25: Griewank](#f25-griewank)
  - [f26: Happy Cat](#f26-happy-cat)
  - [f27: Himmelblau](#f27-himmelblau)
  - [f28: Holder-Table](#f28-holder-table)
  - [f29: Keane](#f29-keane)
  - [f30: Leon](#f30-leon)
  - [f31: Levy N.13](#f31-levy-n13)
  - [f32: Matyas](#f32-matyas)
  - [f33: McCormick](#f33-mccormick)
  - [f34: Periodic](#f34-periodic)

## f1: Ackley

$$f(\mathbf{x}) = -20\exp\left(-0.2\sqrt{\frac{1}{n}\sum_{i=1}^{n}x_i^2}\right)-\exp\left(\frac{1}{n}\sum_{i=1}^{n}\cos 2\pi x_i\right)+ 20 + \exp(1)$$

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

$$f(x,y)=-0.0001\left(\left|\sin x\sin y \exp\left|100-\frac{\sqrt{x^2+y^2}}{\pi}\right|\right|+1\right)^{0.1}$$

$$x,y\in[-10,10]$$

<p align="center"><a href="./images/f16_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f16_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
|                |          |           |            |        |

## f17: Deckkers-Aarts

$$f(x,y) = 10^5x^2 + y^2 -(x^2 + y^2)^2 + 10^{-5}(x^2 + y^2)^4$$

$$x,y\in[-20,20]$$

<p align="center"><a href="./images/f17_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f17_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f18: Drop-Wave

$$f(x,y) = - \frac{1 + \cos(12\sqrt{x^{2} + y^{2}})}{0.5(x^{2} + y^{2}) + 2}$$

$$x,y\in[-5.2,5.2]$$

<p align="center"><a href="./images/f18_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f18_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f19: Easom

$$f(x,y)=−\cos x_1\cos x_2 \exp(−(x − \pi)^2−(y − \pi)^2)$$

$$x,y\in[-100,100]$$

<p align="center"><a href="./images/f19_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f19_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          | &#10004;  |            |        |

## f20: Egg Crate

$$f(x,y)=x^2 + y^2 + 25(\sin^2 x + \sin^2 y)$$

$$x,y\in[-5,5]$$

<p align="center"><a href="./images/f20_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f20_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          | &#10004;  |            |        |

## f21: Eggholder

$$f(x,y)=-(y+47)\sin\sqrt{\left|y+\frac{x}{2}+47\right|}-x\sin\sqrt{|x-(y+47)|}$$

$$x,y\in[-512,512]$$

<p align="center"><a href="./images/f21_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f21_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f22: Exponential

$$f(\mathbf{x})=-\exp\left(-0.5\sum_{i=1}^n{x_i^2}\right)$$

$$x_i\in[-1,1]$$

<p align="center"><a href="./images/f22_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f22_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f23: Goldstein-Price

$$f(x,y)=[1 + (x + y + 1)^2(19 − 14x+3x^2− 14y + 6xy + 3y^2)]\cdot\\
[30 + (2x − 3y)^2(18 − 32x + 12x^2 + 4y − 36xy + 27y^2)]$$

$$x,y\in[-2,2]$$

<p align="center"><a href="./images/f23_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f23_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f24: Gramacy & Lee

$$f(x)=\frac{\sin10\pi x}{2x}+(x-1)^4$$

$$x\in[-0.5,2.5]$$

<p align="center">Surface Plot | Contour Plot</p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          | &#10004;  |            |        |

## f25: Griewank

$$f(\mathbf{x})=1+\sum_{i=1}^n\frac{x_i^2}{4000}-\prod_{i=1}^{n}\cos\frac{x_i}{\sqrt{i}}$$

$$x_i\in[-600,600]$$

<p align="center"><a href="./images/f25_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f25_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f26: Happy Cat

$$f(\mathbf{x})=\left[\left(||\textbf{x}||^2 - n\right)^2\right]^\alpha + \frac{1}{n}\left(\frac{1}{2}||\textbf{x}||^2+\sum_{i=1}^{n}x_i\right)+\frac{1}{2}$$

$$x_i\in[-2,2]$$

<p align="center"><a href="./images/f26_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f26_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           | &#10004;   |        |

## f27: Himmelblau

$$f(x,y)=(x^{2}+y-11)^{2}+(x+y^{2}-7)^{2}$$

$$x,y\in[-6,6]$$

<p align="center"><a href="./images/f27_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f27_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f28: Holder-Table

$$f(x,y)=-\left|\sin x\cos y\exp\left|1-\frac{\sqrt{x^2+y^2}}{\pi}\right|\right|$$

$$x,y\in[-10,10]$$

<p align="center"><a href="./images/f28_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f28_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
|                |          |           |            |        |

## f29: Keane

$$f(x,y)=-\frac{\sin^2(x-y)\sin^2(x+y)}{\sqrt{x^2+y^2}}$$

$$x,y\in[0,10]$$

<p align="center"><a href="./images/f29_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f29_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f30: Leon

$$f(x,y)=100(y−x^3)^2+(1−x)^2$$

$$x,y\in[0,10]$$

<p align="center"><a href="./images/f30_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f30_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       | &#10004; |           |            |        |

## f31: Levy N.13

$$f(x, y)=\sin^2 3\pi x+(x-1)^2(1+\sin^2 3\pi y)+(y-1)^2(1+\sin^2 2\pi y)$$

$$x,y\in[-10, 10]$$

<p align="center"><a href="./images/f31_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f31_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f32: Matyas

$$f(x,y)=0.26(x^2+y^2)-0.48xy$$

$$x,y\in[-10,10]$$

<p align="center"><a href="./images/f32_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f32_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       | &#10004; |           |            |        |

## f33: McCormick

$$f(x,y)=sin(x+y)+(x-y)^2-1.5x+2.5y+1$$

$$x\in[-1.5,4],\ y\in[-3,3]$$

<p align="center"><a href="./images/f33_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f33_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

## f34: Periodic

$$f(\mathbf{x})=1+\sum_{i=1}^n{sin^2 x_i}-0.1e^{\sum_{i=1}^{n}x_i^2}$$

$$x_i\in[-10,10]$$

<p align="center"><a href="./images/f34_surf.svg" target="_blank">Surface Plot</a> | <a href="./images/f34_cont.svg" target="_blank">Contour Plot</a></p>

| Differentiable | Unimodal | Separable | Parametric | Random |
| :------------: | :------: | :-------: | :--------: | :----: |
| &#10004;       |          |           |            |        |

---

[Home](/) > [Projects](/projects/) > [PyBenchFCN](/projects/pybenchfcn/) > [Classical Single-Objective Optimization](/projects/pybenchfcn/single-objective-optimization/)