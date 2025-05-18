---
excalidraw-plugin: parsed
excalidraw-open-md: true
tags:
  - note_atomic
title: 2025-03-12_Assignment 09
description: 
date: 2025-03-12
name: Assignment 09
slug: 2025-03-12_Assignment 09
people: 
location: 
weekday: 
time: 
share: true
hide: true
---
%%[parents:: [[../2025-03-12_Module 09 Composite Materials/index|2025-03-12_Module 09 Composite Materials]]]%%
### Assignment 09

![[Periodic Notes/Atomic/2025/2025-03-12_Assignment 09/2025-03-12_Assignment 09.svg|Periodic Notes/Atomic/2025/2025-03-12_Assignment 09/2025-03-12_Assignment 09.svg]]

#### Question 1

Load tends to go to the ______________ element.

strongest  
elastic  
weakest  
✔️stiffest

#### Question 2

What is the increase in Area when two square elements on top of each other are analyzed as Composite instead of Load Sharing?

Triple (3x)  
Double (2x)  
✔️The same (1x)  
Quadruple (4x)

#### Question 3

What is the increase in Bending Moment when two square elements on top of each other are analyzed as Composite instead of Load Sharing?

Quadruple (4x)  
The same (1x)  
Triple (3x)  
✔️Double (2x)

#### Question 4

What is the increase in Bending Stiffness when two square elements on top of each other are analyzed as Composite instead of Load Sharing?

The same (1x)  
✔️Quadruple (4x)  
Double (2x)  
Triple (3x)

#### Question 5

What is critical for two elements to be composite?

Transformed Section  
✔️Longitudinal Shear Transfer  
Load Sharing  
Stiffness

#### Questions 6 to 14 refer to the following information:

A W150x37 has been cast in a 305 mm Diameter sonotube. This is below grade, so we don't have any buckling issue. The concrete has an E=30,000 MPa

NOTE: The Steel code has been updated for W150x37. The area is 4730mm2

![[../../../../../docs/assets/img/W150x37.webp|640x819]]

#### Question 6

What is EAsteel?

✔️946x10^6 N  
2050x10^6 N  
13,666x10^6 N  
2996x10^6 N  
2192x10^6 N  
141.9x10^6 N

$EA_s=200,000\times4730=946,000,000N$

#### Question 7

What is EAconcrete?

2192x10^6 N  
13,666x10^6 N  
✔️2050x10^6 N  
141.9x10^6 N  
2996x10^6 N  
946x10^6 N

$A_c=((305/2)^2\times \pi)-4730=68,331mm^2$
$EA_c=30,000\times A_c=2,049,949,924N$

#### Question 8

What is EAtotal?

13,666x10^6 N  
✔️2996x10^6 N  
946x10^6 N  
2050x10^6 N  
141.9x10^6 N  
2192x10^6 N

$EA_{total}=\sum{EA}=2,995,949,924N$

#### Question 9

What percentage of the load goes to the Steel?

Write the answer as a % to one decimal place (XX.X)

$EA_s \div EA_{total}=0.3157=31.6\%$

#### Question 10

What percentage of the load goes to the Concrete?

Write the answer as a % to one decimal place (XX.X)

$EA_s \div EA_{total}=0.6842=68.4\%$

#### Question 11

Remembering that buckling isn't an issue, so the capacity of a steel column would be Cr = fyA, what is the compressive capacity of the Steel portion in kN?

Write the answer in kN to no decimal places (XXXX)

- **Compression Squashing** (Strength)
	- $P_y=f_yA$
		- Derived from $\sigma=\frac{P}{A}$

$C_r=350MPa \times 4730mm^2 =1,655,500N=1,656kN$

#### Question 12

If the reduction factor for concrete is 0.65 and the maximum stress this concrete can see in compression is f'c = 20MPa, what is the compressive resistance of the concrete portion?

Write the answer in kN to no decimal places (XXX)

$C_r=0.65 \times 20MPa \times 68,331 =888,303N=888kN$

#### Question 13

If the load on the load-sharing column is Pf=1500kN, knowing the percentage of load that goes to each material and the capacity of each of those members, does the STEEL work (is Cf<Cr)?

✔️Yes  
No

$C_f=1500kN\times 31.6\%=474kN<C_r=1,656kN$

#### Question 14

If the load on the load-sharing column is Pf=1500kN, knowing the percentage of load that goes to each material and the capacity of each of those members, does the CONCRETE work (is Cf<Cr)?

✔️No  
Yes

$C_f=1500kN\times 68.4\%=1,026kN>C_r=888kN$

#### Question 15

Did you complete this question?

![[../../../../../docs/assets/img/ARC2046 Assignment 08 Question 15.pdf|ARC2046 Assignment 08 Question 15]]

✔️Yes  
No

#### Questions 16 to 23 refer to the following:

![[../../../../../docs/assets/img/Concrete beam section.webp|640x311]]

#### Question 16

What is the area of the steel?

Write your answer in mm² to zero decimal places. Do not write the units.

$A_s=5 \times 500 = 2500mm^2$

#### Question 17

What is the area of the concrete? You do not need to subtract the area of the steel.

Write your answer in mm² to zero decimal places. Do not write the units.

$A_c=300mm*600mm=180,000mm^2$

#### Question 18

What is the E (MPa) of the steel?

Write your answer to zero decimal places. Do not write the units.

$E_s=200,000MPa$

#### Question 19

What is the E (MPa) of the concrete?

Write your answer to zero decimal places. Do not write the units.

$E_c=27,500MPa$

#### Question 20

What is the area of the steel if we transform it to concrete?

Write your answer in mm² to zero decimal places. Do not write the units.

$A_{stc}=A_s \times (E_s/E_c)=18,182mm^2$

#### Question 21

What is the Total Equivalent Area of the section if we transformed the steel to concrete?

Write your answer in mm² to zero decimal places. Do not write the units.

$A_{Ttc}=18,182+180,000=198,182mm^2$

#### Question 22

What is the area of the concrete if we transformed it to steel instead?

Write your answer in mm² to zero decimal places. Do not write the units.

$A_{cts}=A_c \times (E_c/E_s)=24,750mm^2$

#### Question 23

What is the Total Equivalent Area of the section if we transformed the concrete to steel?

Write your answer in mm² to zero decimal places. Do not write the units.

$A_{Tts}=2500+24,750=27,250mm^2$

---

# Excalidraw Data

## Text Elements
%%
## Drawing
```compressed-json
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
```
%%