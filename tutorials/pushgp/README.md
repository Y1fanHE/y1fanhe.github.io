# PushGP

[*>> 用中文查看此页面*](/cn/tutorials/pushgp/)

In this article, we are going to learn about a variant of [Genetic Programming (GP)](/tutorials/gp/) algorithm called PushGP. PushGP is able to generate computer programs with multiple data types and control flows.

## Introduction

## Push Language

Push is a family of programming languages for generating programs with GP. Push supports multiple data types and various control flows such as condition and loops.

### Rules to Run Push Programs

A Push program consists of a list of Push instructions. These instructions are run with multiple stacks in the Push interpreter based on the following rules.

- Load the program into EXEC stack at the beginning
- Pop the top instruction $p_i$ from the EXEC stack
- Check whether the stacks contain enough arguments for the instruction $p_i$
- Pop the arguments required by the instruction $p_i$ from corresponding stacks
- Push the results to corresponsing stacks
- Take the top item of specified stacks as program outputs

### An Example of Running A Push Program

![push](push.svg)

## Procedure of PushGP

The procedure of original PushGP algorithm[^1] is similar to the traditional GP ([see the previous tutorial](/tutorials/gp/)), including initialization, selection, crossover, and mutation. In this article, we introduce a improved variant of PushGP. This variant employs **lexicase selection**[^2] and **Uniform Mutation by Addition and Deletion (UMAD)**[^3].

### Encoding

### Initialization

### Lexicase Selection

### Uniform Mutation by Addition and Deletion

## Resources

## References

[^1]:
[^2]:
[^3]:
