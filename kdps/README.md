<!--
 * @Author: He,Yifan
 * @Date: 2022-02-22 05:02:25
 * @LastEditors: He,Yifan
 * @LastEditTime: 2022-03-11 16:27:31
-->

# Knowledge-Driven Program Synthesis

> A Genetic Programming (GP) system that improves itself over time by extracting and storing knowledge from the programming tasks it solved in the past, and using this knowledge in the future programming tasks

## Motivation

GP searches a program based on random initialization, random variation, and a fitness-guided selection. However, a human programmer is different in the following ways.

- A human programmer writes programs based on their knowledge.
- A human programmer becomes more experienced after solving more tasks.
- A human programmer learns knowledge from fields other than programming.
- A human programmer can communicate with other human programmers to help solve the task.

A human programmer applies, learns, and transfers knowledge during programming.

Therefore, this study aims to extend the GP with the ability of applying, learning, and transfering knowledge during programming.

## System Design

The first thing in the system design is to decide the form of knowledge. As the initial step, knowledge in the current study refers to a fragment of solution program (sub-program) of a solved task.

<figure align="center">
<img src="images/system-design.svg" alt="system design" width="480" />
<figcaption>System Design of Knowledge-Driven Program Synthesis</figcaption>
</figure>

The system consists of a GP solver, an online Knowledge Archive (KA), an offline KA, and various tools that interact between the three components.

- The GP solver utilizes the knowledge from online KA during search through an adaptive process that allows the automatic selection or creation of proper knowledge.
- After a solution program is found, knowledge (sub-programs) are extracted from this program and stored in the offline KA along with the metadata of the problem.
- When a new problem is posed to the system, a recommender system will suggest a subset of the offline KA to create the online KA based on the metadata of the problem.
- Additionally, a knowledge management tool (organizer) is applied to the offline KA to organize (e.g., clustering) the stored knowledge.

## Past Studies

### Adaptive Replacement Mutation (ARM)

This work focus on the interaction between GP and the online KA, assuming an extracted online KA. The goal is to automatically select the pieces of knowledge that are helpful to the search of GP from the online KA that usually includes helpful and unhelpful pieces.

The way to use knowledge in the variation process is called Replacement Mutation (RM). RM replaces a random partition of the parent program with a selected piece of knowledge.

The algorithm tends to select helpful knowledge through an adaptive process. The idea is similar as JADE, a well-known self-adaptive evolutionary algorithm that automatically selets proper parameters for its variation operators.

1. If a piece of knowledge improves the program, it will be collected to a working archive since it tends to be helpful.
2. In the later variation steps, the "helpful" pieces of knowledge will be selected from the working archive.

By the above two steps, the pieces of knowledge that improved the programs are more likely to be selected.

<figure align="center">
<img src="images/arm.svg" alt="adaptive replacement mutation" width="369" />
<figcaption>Adaptive Replacement Mutation</figcaption>
</figure>

---

[Home](/)/[Knowledge-Driven Program Synthesis](/kdps/)
