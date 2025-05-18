---
excalidraw-plugin: parsed
excalidraw-open-md: true
tags:
  - note_atomic
title: 2025-03-05_Assignment 08
description: 
date: 2025-03-05
name: Assignment 08
slug: 2025-03-05_Assignment 08
people: 
location: 
weekday: 
time: 
share: true
hide: true
---
%%[parents:: [[../2025-03-05_Module 08 Wood - Beam Design/index|2025-03-05_Module 08 Wood - Beam Design]]]%%
# Assignment 08

![[Periodic Notes/Atomic/2025/2025-03-05_Assignment 08/2025-03-05_Assignment 08.svg|Periodic Notes/Atomic/2025/2025-03-05_Assignment 08/2025-03-05_Assignment 08.svg]]

### Questions 1 to 8 make use of the following information:

We are trying to design a 5.4m long beam inside with a uniformly distributed line load of wd=5kN/m and wl=8kN/m. What D.Fir-L No.1 sawn timber size would be the best choice? Use L/240 for dead+live deflection criteria and L/360 for live deflection criteria.

## Question 1

What is the factored line load wf (kN/m) on the beam? Write your answer to two decimal places (XX.XX). Do not write the units.

$w_f=1.25\times 5 + 1.5\times8=18.25(kN/m)$

## Question 2

What is the Dead+Live serviceability line load wd+l (kN/m) on the beam? Write your answer to two decimal places (XX.XX). Do not write the units.

$w_{d+l}=1\times 5 + 1\times8=13(kN/m)$

## Question 3

What is the Live serviceability line load wl (kN/m) on the beam? Write your answer to two decimal places (X.XX). Do not write the units.

$w_{l}=1\times8=8(kN/m)$

## Question 4

What is the maximum factored moment Mf (kNm) on the beam. You do NOT need to do Method of Sections. Write your answer to two decimal places (XX.XX). Do not write the units.

Refer to [[../../../../../assets/img/BEAM LOADING DIAGRAMS.pdf|BEAM LOADING DIAGRAMS]]

$M_{MAX}=\frac{wl^2}{8}=\frac{18.25\times5.4^2}{8}=66.52(kNm)$

## Question 5

What is the maximum factored shear Vf (kNm) on the beam. You do NOT need to do Method of Sections. Write your answer to two decimal places (XX.XX). Do not write the units.

$V_{MAX}=w(\frac{l}{2}-x)=18.25(\frac{5.4}{2}-0)=49.28(kNm)$

## Question 6

What is the minimum EsI the beam requires to meet serviceability requirements?

$$\Delta_{MAX_{UniformLoad}}=\frac{5wl^4}{384EI}$$
$\Delta_{MAX_{D+L|L}}=\frac{5\times13|8\times5400^4}{384\times E_{s}I}=5400/240|5400/360=22.5|15$
$E_sI_{D+L|L}=6.397e12|5.905e12$

- 22.5 mm
- 5905x10^9 Nmm²
- 15 mm
- ✔️6397x10^9 Nmm²

## Question 7

From the Beam Tables for Wood members, what is the most efficient D.Fir-L No.1 beam that meets all our structural criteria?

- ✔️241x343
- 241x292
- 241x241
- 241x394

## Question 8

Try to do the Mr, Vr and EsI calculations by hand. See if they match what you found as published values.

- YES I did the Calculation

### The remaining questions make use of the following information:

The bedroom of a modern summer house is cantilevered out over the patio. Since they are not insulating the floor, the architect wants to leave the floor joists exposed to the outside from below as a feature. Note that the major beams cantilever, not the basic members we are designing). She is proposing using 2x8 Cedar SS. Assume normal house live loads and that the assembly is vinyl flooring on 3/4" plywood spanning between the joists (assume typical house construction nailing patterns). You should assume 0.05kPa for mech/elec dead loads. Use deflection criteria of L/240 for D+L and L/360 for L. If the joists are 16" c/c, can they span 3.2m?

## Question 9

Assuming you add up the dead loads (you can do this... all the info is there) and you get a floor Dead Load of 0.32kPa, and you noted that the joists are at 16" c/c, what is the factored line load wf (kN/m) on the joist? Write your answer to two decimal places (X.XX). Do not write the units.

Refer to [[../../../../../assets/img/DEAD LOADS.pdf|DEAD LOADS]]
$16in*25.4mm/in=406.4mm=0.4064m$
$q_{UD}=1.4\times0.32=0.448kPa$
$q_{UDL}=1.25\times0.32+1.5\times1.9=3.25kPa$
$w_f=3.25kPa\times0.4064m=1.32kN/m$

## Question 10

What is the Dead+Live serviceability line load wd+l (kN/m) on the joist? (Dead load in question above, joists still at 16" c/c) Write your answer to three decimal places (X.XXX). Do not write the units.

$S_{DL}=0.32+1.9=2.22kPa$
$w_{D+L}=2.22\times0.4064=0.902kN/m$

## Question 11 

What is the Live serviceability line load wl (kN/m) on the joist? Write your answer to three decimal places (X.XXX). Do not write the units.

$S_{L}=1.9kPa$
$w_{L}=1.9\times0.4064=0.772kN/m$

## Question 12

What is the maximum factored moment Mf (kNm) on the joist. You do NOT need to do Method of Sections. Write your answer to two decimal places (X.XX). Do not write the units.

$M_{MAX}=\frac{wl^2}{8}=\frac{1.32\times3.2^2}{8}=1.69(kNm)$

## Question 13

What is the maximum factored shear Vf (kNm) on the joist. You do NOT need to do Method of Sections. Write your answer to two decimal places (X.XX). Do not write the units.

$V_{MAX}=w(\frac{l}{2}-x)=1.32(\frac{3.2}{2}-0)=2.11(kNm)$

## Question 14

What is the minimum EsI the joist requires to meet serviceability requirements?

$$\Delta_{MAX_{UniformLoad}}=\frac{5wl^4}{384EI}$$
$\Delta_{MAX_{D+L|L}}(Nmm^2)=\frac{5\times0.902|0.772\times3200^4}{384\times E_{s}I}=3200/240|360=13.333|8.889$
$E_sI_{D+L|L}=92.36e9|118.58e9$


- 8.89 mm
- 92.3x10^9 Nmm²
- ✔️118.4x10^9 Nmm²
- 139x10^9 Nmm²

## Question 15

What Grading Category is the member?

- Structural Light Framing
- Post and timber
- ✔️Structural Joist or Plank
- Beam and stringer

## Question 16

What is Kd (load duration factor)? (this isn't a trick question)

1.0

## Question 17

Khb = (X.X) Khv = (X.X)

1.4
1.4

## Question 18

Ksb = (X.XX) Ksv = (X.XX) Kse = (X.XX)

0.84
0.96
0.94

## Question 19

Kt = (X.X)

1.0

## Question 20

Kzb = (X.X) Kzv = (X.X)

1.2
1.2

## Question 21

KL = (X.X)

1.0

## Question 22

What is Mr (kNm) of the joist? Write your answer to two decimal places (X.XX) Do not write the units.

Cedar SS
$f_b=10.6$
$f_v=1.3$
$E=7500$
$E_{05}=5500$
$F_b = f_b \times (K_D \times K_{Hb} \times K_{Sb} \times K_T)=12.465N/mm^2$
$S=\frac{bd^2}{6}=\frac{(25.4*1.5)\times(25.4*7.25)^2}{6}=215336 mm^3$
$M_{r}(Nmm)=\phi_b \times F_b \times S \times K_{zb} \times K_L=0.9 \times 12.465 \times 215336 \times 1.2 \times 1=2,898,896Nmm=2.90kNm$

## Question 2

What is Vr (kNm) of the joist? Write your answer to two decimal places (X.XX) Do not write the units.

$F_v(N/mm^2|MPa)=f_v \times (K_d \times K_{Hv} \times K_{Sv} \times K_T)=1.7472N/mm^2$
$A_n=(25.4*1.5)\times(25.4*7.25)=7,016mm^2$
$V_r(N)=\phi_v \times F_v \times (\frac{2}{3}A_n) \times K_{Zv}=0.9*1.7472*0.6667*7016*1.2=8,826N=8.83kN$

## Question 24

What is the actual EsI (Nmm²) of the member?

$I=\frac{bd^3}{12}=19,827,086mm^4$
$E=K_{sE}\times E=0.94*7500=7,050N/mm^2$
$EsI=139.780e9Nmm^2$

- ✔️ 139x10^9 Nmm²
- 7,500 MPa
- 118.4x10^9 Nmm²
- 84.4x10^9 Nmm²

## Question 25

Does the member work?

- No
- ✔️ Yes


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