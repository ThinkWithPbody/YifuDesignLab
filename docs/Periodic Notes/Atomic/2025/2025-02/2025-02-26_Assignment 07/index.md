---
excalidraw-plugin: parsed
excalidraw-open-md: true
tags:
  - note_atomic
title: 2025-02-26_Assignment 07
description: 
date: 2025-02-26
name: Assignment 07
slug: 2025-02-26_Assignment 07
people: 
location: 
weekday: 
time: 
share: true
hidden: true
---
%%[parents:: [ARC2046H](../../../../../Courses/2025/ARC2046H/ARC2046H-Structures_2.md)]%%
### Assignment 07

## Question 1
Out of all the species of trees in Canada, how many make up the majority of construction wood?

None
✔️4
7
30
All

## Question 2
Which of the following is NOT a species combination we use?

D.Fir-L
Hem-Fir
SPF
Nor
✔️LVL

## Question 3
Select all the factors that impact wood strength

✔️Species
✔️Chemicals (Preservative/Fire Retardant)
✔️Size
✔️System Effects
✔️Grade
✔️Service Conditions (Wet/Dry)
✔️Load Duration

## Refer to the following for questions 04-18
Find the capacity of a SPF No1/No2 2x4 stud in a 9'-0" wall with 610mm spacing, dry conditions and untreated (because it's inside an envelope). Assume the stud is connected to the sheathing to prevent weak-axis lateral buckling.

## Question 4
What does the reduction factor $\phi$ = ?

0.8
## Question 5
What Grade category would it be?

Structural Light Framing
✔️Stud
Beam and stringer
Post and timber
Structural Joists and Planks

## Question 6
What fc would you use in the design?
Write your answer in MPa to 1 decimal place (XX.X)

11.5 MPa
## Question 7
What E05 would you use in the design?
Write your answer in MPa to 0 decimal place (XXXX)

6500 mm
## Question 8
KD = 1
## Question 9
KH = 1.1
## Question 10
KSC = 1
## Question 11
KSE = 1
## Question 12
KT = 1
## Question 13
d = 89 mm
## Question 14
b = 38 mm
## Question 15
A = 3382 mm2
## Question 16
What is the buckling length in the STRONG direction, Ld = 2743 mm
## Question 17
What is the buckling length in the WEAK direction, Lb = 0 mm
## Question 18
What is the Compressive resistance Pr = ?
Try it using the big long equation. You may cross-reference with the Tables (you may have to interpolate).
Write your answer in **kN** to one decimal place (XX.X)

$\because$ Braced in WEAK axis
$\therefore$ Only calculate $P_{rd}$

$P_r(N)=\phi_c F_c A K_{zc} K_c$

$F_c(MPa)=f_c(K_D K_H K_{SC} K_T)$
$F_c(MPa)=11.5 \times (1 \times 1.1 \times 1 \times 1)= 12.65 MPa$

$K_{ZCd}=6.3(dL_b)^{-0.13}<=1.3=1.3$ (Assumed $L_b$ = 10 mm)

$C_{Cd}=L_d/d<= 50=30.82$

$K_{C}(Unitless)=(1.0+\frac{F_C K_{ZC} {C_{C}}^3}{35 E_{05} K_{SE} K_T})^{-1}$
$K_{Cd}=(1.0+\frac{12.65 \times 1.3 \times 30.82^3}{35 \times 6500 \times 1 \times 1})^{-1}=0.3209$

$P_{r}(kN)=\phi_c \times F_c \times A \times K_{zc} \times K_c \div 1000$
$P_{rd}=0.8 \times 12.65 \times 3382 \times 1.3 \times 0.3209 \div 1000=14.27 kN$
WOOD COMPRESSION TABLES, p.16 - $P_r = 14.127 kN$ (Interpolated linearly from 13.5 - 15.7) (Ignore the difference because the table is non-linear)

## Refer to the following for questions 19-29
You are designing the interior entrance of a community centre with exposed timber posts. Typically you would use Douglas-Fir, but the client has a sponsor who is donating 191x241 Cedar, Structural Select members. We are trying to set the bay sizes and to do that, we need to determine the capacity of the 5.0m tall columns. You've looked at the drawings and determined that we can brace the posts half-way up in the weak axis.

## Question 19
What does the reduction factor $\phi$ = ?

0.8
## Question 20
What Grade category would it be?

Structural Light Framing
Structural Joists and Planks
Beam and stringer
Stud
✔️Post and timber


## Question 21
What fc would you use in the design?
Write your answer in MPa to 1 decimal place (X.X)

7.5 MPa

## Question 22
What E05 would you use in the design?
Write your answer in MPa to 0 decimal place (XXXX)

5500 MPa

## Question 23
What does KD*KH*KSC*KT = ?

1

## Question 24
What does KSE = ?

1

## Question 25
What is the buckling length in the STRONG direction, Ld = ?

5000

## Question 26
What is the buckling length in the WEAK direction, Lb = ?

2500

## Question 27
What is Cc in the STRONG direction?
Write your answer to **THREE** decimal places (XX.XXX)

$C_{Cd}=L_d/d<= 50$

20.747

## Question 28
What is Cc in the WEAK direction?
Write your answer to **THREE** decimal places (XX.XXX)

$C_{Cb}=L_b/b<= 50$

13.089

## Question 29
What is the Compressive resistance Pr = ?
Try it using the big long equation. Remember that there is two direction to check.
You may cross-reference with the Tables (you may have to interpolate).
Write your answer in **kN** to one decimal place (XX.X)

$b=191$
$Lb=2500$
$d=241$
$Ld=5000$

$P_{r}(N)=\phi_c \times F_c \times A \times K_{zc} \times K_c$

$F_c(MPa)=f_c(K_D K_H K_{SC} K_T)=7.5 MPa$

$A=46031 mm^2$


$K_{ZCb}=6.3(bL_b)^{-0.13}<=1.3=1.1510$
$K_{ZCd}=6.3(dL_d)^{-0.13}<=1.3=1.0205$


$K_{Cb}=(1.0+\frac{F_C \times K_{ZCb} \times {C_{Cb}}^3}{35 \times E_{05} \times K_{SE} \times K_T})^{-1}$
$K_{Cb}=(1.0+\frac{7.5 \times 1.1510 \times 2,242.43}{35 \times 5500 \times 1 \times 1})^{-1}=0.90863$
$K_{Cd}=(1.0+\frac{7.5 \times 1.0205 \times 8,930.29}{35 \times 5500 \times 1 \times 1})^{-1}=0.73797$

$P_{rb}(kN)=0.8 \times 7.5 \times 46031 \times 1.1510 \times 0.90863 \div 1000=288.8$
$P_{rd}(kN)=0.8 \times 7.5 \times 46031 \times 1.0205 \times 0.73797 \div 1000=208.0$

$P_r=208.0kN$

WOOD COMPRESSION TABLES, p.40 - $P_{rd} = 208 kN$ $P_{rb} = 167 kN$

---

# Excalidraw Data

## Text Elements
%%
## Drawing
```compressed-json
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
```
%%