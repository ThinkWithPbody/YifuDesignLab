---
excalidraw-plugin: parsed
excalidraw-open-md: true
tags:
  - note_atomic
title: 2025-03-18_Assignment 10
description: 
date: 2025-03-18
name: Assignment 10
slug: 2025-03-18_Assignment 10
people: 
location: 
weekday: 
time: 
share: true
hide: true
---
%%[parents:: [ARC2046H](/docs/Courses/2025/ARC2046H/ARC2046H-Structures_2.md)]%%
### Assignment 10

![2025-03-18_Assignment 10.svg](Periodic%20Notes/Atomic/2025/2025-03/2025-03-18_Assignment%2010/2025-03-18_Assignment%2010.svg)

#### This is for determining the answers to Questions 1 to 14

We have a column supporting Pf=800kN and an Mf=11.2kNm and we need to determine the longitudinal reinforcing required if the column is 200x200. We are using concrete with f'c=30MPa, there is 25mm cover, and 10M ties. Assume 20M bars with an equal number of bars on each face.

#### Question 1

What is b (mm)?

200

#### Question 2

What is h (mm)?

200

#### Question 3

What is the value of f'c (MPa)?

30

#### Question 4

What is the cover (mm)?

25

#### Question 5

What is the diameter of the ties (mm)?

10

#### Question 6

What is the diameter of the main reinforcing (mm)?

20

#### Question 7

What is the dimension $\gamma$h (mm)?

- $\gamma h=h - 2\times(Cover + \unicode{x2300}Ties + \frac{1}{2}\unicode{x2300}Bars)$### Interaction Diagram

![2025-03-19_Interaction Diagram.svg](Periodic%20Notes/Atomic/2025/2025-03/2025-03-19_Interaction%20Diagram/2025-03-19_Interaction%20Diagram.svg)



---



$\gamma h=200 - 2\times(25 + 10 + \frac{1}{2}20)=110$

#### Question 8

What is the ratio of bar distance to h?

Write your answer to 2 decimal places (X.XX)

$\gamma = \gamma h \div h$
$\gamma = 110/200=0.55$

#### Question 9

What is Ag of the column?

Write the answer in mm²

$A_g(mm^2)=b \times h=40,000$

#### Question 10

Remembering we need a column with Pr of at least Pf, what is Pr/Ag (N/mm² or MPa)? (Pay attention to units)

$P_r/A_g(MPa)=P_F(N) \div A_g(mm^2)=800,000N \div 40,000mm^2=20MPa$

#### Question 11

Remembering we need a column with Mr of at least Mf, what is Mr/Agh (N/mm² or MPa)? (Pay attention to units)

Write your answer to 1 decimal place (X.X)

$M_r/A_{gh}(MPa)=M_F(Nmm) \div (A_g \times h)=11,200,000Nmm \div (40,000 \times 200)=1.4MPa$

#### Question 12

Using the Concrete Column Interaction Diagrams for the appropriate f'c and for a column with equal reinforcement on all sides, what is the required reinforcement ratio for the column?

Write your answer to 2 decimal places (X.XX)

$P_r/A_g(MPa)=20$
$M_r/A_{gh}(MPa)=1.4$
### Interaction Diagram

![2025-03-19_Interaction Diagram.svg](Periodic%20Notes/Atomic/2025/2025-03/2025-03-19_Interaction%20Diagram/2025-03-19_Interaction%20Diagram.svg)



---


$P_g=0.03$

#### Question 13

Using the answer from the previous question, what is the required reinforcement area (mm²)?

Write your answer with no decimal places.

$A_s{req}=e \times A_g=P_g \times A_g=0.03 \times 40,000=1,200mm^2$

#### Question 14

What reinforcement do we need to meet our strength requirements for the reinforced concrete column?

- ✔️4-20M
- 4-10M
- 6-20M
- 8-20M
- 6-15M

$N_{Bars}=A_s{req} \div A_{Bars}=1200/300=4$

#### Question 15

Which of the following is an appropriate stress block (stress profile) of an idealized under-reinforced concrete beam?

![2025-03-18_Assignment 10-Stress Profile](/docs/assets/img/2025-03-18_Assignment%2010-Stress%20Profile.webp)


- ✔️Orange
- Pink
- Green
- Blue
- Yellow

#### For Questions 16 to 24, use the following diagram

![2025-03-18_Assignment 10-Concrete Beam](/docs/assets/img/2025-03-18_Assignment%2010-Concrete%20Beam.webp)

#### Question 16

What is the Area (mm²) of the tension steel?

Write your answer to zero decimal places.

$3 \times 200 = 600$

#### Question 17

What is the Tension capacity (kN) of the tension steel?

Write your answer to zero decimal places.

$T(N)=\phi_S \times A_S \times f_y=0.85 \times 600 \times 400=204,000$

#### Question 18

This question depends on previous answers. Pay attention to units.

What is **$\beta 1c$ (mm)** for the beam?

Write your answer to 2 decimal places.

$\beta_1c(mm)= T/ (\alpha_1 \times \phi_c \times f’_c \times b)= 204,000/ (0.8 \times 0.65 \times 30 \times 300)=43.59$

#### Question 19

What is the effective depth, d (mm), of the concrete beam above?

Write your answer to 1 decimal place.

$d=500-30-10-15/2=452.5$

#### Question 20

This question depends on previous answers.

What is the Moment Capacity, Mr (kNm), of the concrete beam?

Write your answers in kNm to 1 decimal place. Pay attention to units.

$M_r(Nmm) = T \times (d-(\beta_1c)/2)= 204,000 \times (452.5-(43.59)/2)=87,863,820Nmm=87.9kNm$

#### Question 21

What is the area of shear steel, Av (mm²)?

Write your answer to zero decimal places.

$A_v=2 \times 100=200$

#### Question 22

What is the shear resistance, Vc (kN), of the concrete?

Write your answer to 1 decimal place.

$V_c(N) = 0.2 \times \lambda \times \phi_c \times \sqrt{f’_c} \times b_w \times d= 0.2 \times 1.0 \times 0.65 \times \sqrt{30} \times 300 \times 452.5=96659N=96.7kN$

#### Question 23

What is the shear resistance, Vs (kN), of the steel?

Write your answer to 1 decimal place.

$V_s(N) = \phi_s \times A_v \times f_y \times d \div s= 0.85 \times 200 \times 400 \times 452.5 \div 300=102,566.66N=102.6kN$

#### Question 24

What is the total shear resistance, Vr (kN), of the reinforced concrete beam?

Write your answer to 1 decimal place.

$V_r(N) = V_c + V_s=199.3$


---

# Excalidraw Data

## Text Elements
%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebQA2bQAOGjoghH0EDihmbgBtcDBQMBKIEm4IAHlneIBFSoBHAGsGgGEAVQaAKwARdopNAGZamDYYVJLIWEQK3FJSNip+Usxu

ZwBGJIAGbUGAFgBOLZ4DgFY99a310/i+QshxtA34naTrrb2t06SkwYB2JIHZaQCgkdTcHiDQYJA57H6nHinQZHW6nYFSBCEZTSbgHRJ/eJ7HhJHik+I3RHo6zKYLcLbo5hQBZNBCtNj4NikCoAYnWCD5fImpU0uGwTWUCyEHGIbI5XIkTOszDgcyyUCFkAAZoR8PgAMqwWkSQQeDUQRnMhAAdTBkghDKZbBZBpgRvQJvK6Ml2I44VyaHp9wgbBV2

DUj1Ql0DkwgEuEcAAksR/ag8gBddGa8iZJPcDhCXXowjSrCzLZmyXS33MFP5wtBsIIYgQqF7eLrSHrdGMFjsLhoE7dpisTgAOU4Ym4f2Rg1Jg3WQKDhGYPXSUCb3CZQgQ6M0wmlAFFgplsrWC/h0UI4MRcOvm2h1tO24N4Qdrnt0UQOE08+fP2wxQ3NBNQIMJ0TgNhixyfJ7jAApJhKaMEK2WCM1g+CEMhaF4lheFEWRLZUWBEo8W0AkiRJMkKVO

VD7jQmN8FCKA2X0fQ1DvAAFSDsl/esY0ZOYoAAIWLRwOGUXiLyDLJiBE6ViwktA6yk/iolIKAAEF5kWSQQnvVBlPRGStIWChdNwfSIDmUyzSCPcKCA1AQPwMJCgAX2WYpSnKCQDySABpehSEGABxAAtJIABUwogzUtmwABNVp6AS/yzWmcR0ECbAonE2l0VWJ4eC+bQjlhc59lOP4tnnO4YwjZxZwOGF2z+NseGuEkavRUFiHBNBBiubQeD2ac/n

OH5iQ7NEg10rEcQHIa2r2Ub4nnX5TgOF8qTyzKkIER0WVlTkeQFfkkF3UVxUrGV2ROhVyA4ZVVR4zMdX1Q1MvNdlPQbQ7rVte0/stF03W+00vWEH0/TpdEQ1FcNuCjdE4yvJMU3TTNswQXMlL/JcS0K9BcHWCt92Iaszz40pG309ZrjxS5ARmmMexHfteCSIdezHCdMuKl5TmOGquyXFc10crcdyDPcpWII8MjVKmVNKK8bzvJGnzWn4kj2QY1s/

Ysfzx6nIA5QD9Oc1ySjc8B6KsuA4ANW9Mq86BdMyCoiGxdVlgYQgEAoISrtR6VjvldBuU1aOY6FCBsBEQJsgTdd9ANS1w9O87BT9hP5jVFOMmDsVQ9uuUKkVJ6VST33CnjxOC9TgAxd7Qa+j1m1zhvk9T9OnQBvq7QHLv857jI++dT6Kg7uO85rwv9AAJShyRKdhuu58bjJKlDRGHy2JD69HqAF6bzgoCb3A2PwCMuY37uT+b8+9UIIx+cPzex/0

SKsE072OYgMETUtdSif0fuPNSmltJmT0pJEe89U4HmlCZHSsCJDWUWLPB+C8UEUEivAdukg5hwDjswbACxdQAA1uCEiSNoQi1V1jxBeNcIidcyEUPwAlGhj5kja0GjcQkhE6qQCMGwAw3AvKQHoAQbcSN3LwK3kvcma9jRENICQv2EoSAvzfhCQ+2jiAGgQCQtALNICGIALJsGIAgJBuBNDBEtqBaWpRDGZzQFIiAQl2SWVIMoEUAAKDqfxqC8Ef

GEkJYSdinAAJRmkXggZQBY5gVH8UEyE9JeCDUiTk1AMT4kKPvsfCeCAd5QD7MrP2WYr4IESSWUgClJHSQ4A4pxm5SDbnRNgIgpjUBS3RK0z2aABlBmEFAL8mUpZFNKHYLoCAcrMD1K0uA1jbH2McY5K2rjICigqYwSK4j8DNJjBlae6Qcp9jNAnRkBh8EzBNirM2AEWTOJcjss2TENKXIOUcyS7lwAeToNqYIKZgC2zckAA=
```
%%