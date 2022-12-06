# Knowledge-Driven Program Synthesis

Program Synthesis (PS) requires an intelligent agent to compose computer programs with minimal human efforts. My studies focus on a group of search algorithms called Genetic Programming (GP). GP uses the idea of natural evolution. It starts with a random population of programs, selects the better subsets and updates them until the target program is found.

However, the conventional GPs cannot obtain knowledge from the problem that it has solved. I believe that enhancing GPs with the ability to learn from its experiences can help GPs to generate more complex computer programs.

Therefore, I focus on **how can a GP solves problems, extracts knowledge, and uses the knowledge in later problems**. I call this problem the Knowledge-Driven Program Synthesis (KDPS) problem.

The figure below shows an intuition of the KDPS problem. At the beginning, "Problem 1" is posed to the "Solver" and the "Solver" returns the target solution "Program 1". This "Program 1" is then used to extract "Knowledge Archive 1" with an "Extractor". After that, the "Solver" will use "Kwowledge Archive 1" to solve the "Problem 2".

![Knowledge-Driven Program Synthesis](kdps.svg)

To study the KDPS problem, there are several sub-problems to start with.

- What could be used as "knowledge"?
- How can we extract knowledge from a program?
- How can we use the extracted knowledge to solve a new problem?
- How can we manage the knowledge archive with an increasing size?

Please also check the following presentation for more details. This presentation is done at IEEE SSCI 2022 conference.

![slide of presentation at ssci 2022](ssci2022/slide-1.png)

![slide of presentation at ssci 2022](ssci2022/slide-2.png)

![slide of presentation at ssci 2022](ssci2022/slide-3.png)

![slide of presentation at ssci 2022](ssci2022/slide-4.png)

![slide of presentation at ssci 2022](ssci2022/slide-5.png)

![slide of presentation at ssci 2022](ssci2022/slide-6.png)

![slide of presentation at ssci 2022](ssci2022/slide-7.png)

![slide of presentation at ssci 2022](ssci2022/slide-8.png)

![slide of presentation at ssci 2022](ssci2022/slide-9.png)

![slide of presentation at ssci 2022](ssci2022/slide-10.png)

![slide of presentation at ssci 2022](ssci2022/slide-11.png)

![slide of presentation at ssci 2022](ssci2022/slide-12.png)

![slide of presentation at ssci 2022](ssci2022/slide-13.png)

![slide of presentation at ssci 2022](ssci2022/slide-14.png)

![slide of presentation at ssci 2022](ssci2022/slide-15.png)

![slide of presentation at ssci 2022](ssci2022/slide-16.png)

![slide of presentation at ssci 2022](ssci2022/slide-17.png)

![slide of presentation at ssci 2022](ssci2022/slide-18.png)

![slide of presentation at ssci 2022](ssci2022/slide-19.png)

![slide of presentation at ssci 2022](ssci2022/slide-20.png)

![slide of presentation at ssci 2022](ssci2022/slide-21.png)

![slide of presentation at ssci 2022](ssci2022/slide-22.png)

![slide of presentation at ssci 2022](ssci2022/slide-23.png)

![slide of presentation at ssci 2022](ssci2022/slide-24.png)

![slide of presentation at ssci 2022](ssci2022/slide-25.png)

![slide of presentation at ssci 2022](ssci2022/slide-26.png)

![slide of presentation at ssci 2022](ssci2022/slide-27.png)
