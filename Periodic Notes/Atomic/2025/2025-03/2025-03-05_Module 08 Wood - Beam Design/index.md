---
excalidraw-plugin: parsed
excalidraw-open-md: true
tags:
  - note_atomic
title: 2025-03-05_Module 08 Wood - Beam Design
description: 
date: 2025-03-05
name: Module 08 Wood - Beam Design
slug: 2025-03-05_Module 08 Wood - Beam Design
people: 
location: 
weekday: 
time: 
share: true
hide: true
---
%%[parents:: [[../../../../../Courses/2025/ARC2046H/ARC2046H-Structures_2|ARC2046H]]]%%
### Wood - Beam Design

![[Periodic Notes/Atomic/2025/2025-03-05_Module 08 Wood - Beam Design/2025-03-05_Module 08 Wood - Beam Design.svg|Periodic Notes/Atomic/2025/2025-03-05_Module 08 Wood - Beam Design/2025-03-05_Module 08 Wood - Beam Design.svg]]

Refer to details outlined in [[../../2025-02/2025-02-26_Module 07 Wood - Intro and Column Design/index#Module 07 Wood - Intro and Column Design|Module 07 Wood - Intro and Column Design]]
#### Bending Design

- $M_{r}(Nmm)=\phi_b \times F_b \times S \times K_{zb} \times K_L$: **Bending Design**
	- $\phi_b$ = 0.9 Material reduction factor (higher than compression)
	- $F_b(N/mm^2|MPa)$ = the bending strength – incorporates various factors
		- $F_b = f_b \times (K_D \times K_{Hb} \times K_{Sb} \times K_T)$
			- $f_b (MPa)$ = Material strength
			- $K_D$ = Duration Factor
			- $K_{Hb}$ = System Factor
			- $K_{Sb}$ = Service Factor for bending
			- $K_{Se}$ = Service Factor for stiffness
			- $K_T$ = Treatment Factor
	- $S(mm3)$ = Elastic section modulus
		- Refer to [[../../../../../docs/assets/img/SECTION PROPERTIES.pdf|SECTION PROPERTIES]]
		- Typically rectangles
			- $S=\frac{bd^2}{6}$
	- $K_{zb}$ = the size factor in bending
	- $K_L$ = lateral restraint factor
		- $K_L$ = 1.0 provided that the ends are restrained from laterally rotating and the depth to width ratio does not exceed:
			- 4:1 if no intermediate support is provide on the compression edge
			- 5:1 if the member is held in line by purlins or tie rods
			- 6.5:1 if the compression edge is held in line by direct connection of decking or joists spaced not more than 610 mm apart
			- 7.5:1 if the compression edge is held in line by direct connection of decking or joists spaced not more than 610 mm apart and bridging or blocking is provided at a spacing not exceeding eight times the depth of the member
			- 9:1 if both edges are held in line
		- If the above criteria is not met, $K_L$ may be calculated
	- $1,000,000 Nmm = 1 kNm$

#### Shear Design

- $V_r(N)=\phi_v \times F_v \times (\frac{2}{3}A_n) \times K_{Zv}$: **Shear Design**
	- $\phi_v$ = 0.9 
	- $F_v(N/mm^2|MPa)=f_v \times (K_d \times K_{Hv} \times K_{Sv} \times K_T)$
		- $f_v(MPa)$ = specified strength in shear  
		- $K_d$ = Duration Factor
		- $K_{Hv}$ = System Factor
		- $K_{Sv}$ = Service Factor for shear
		- $K_T$ = Treatment Factor
	- $A_n(mm^2)$ = net area of cross section ($b \times d$ for a rectangular section)
	- $K_{Zv}$ = is the size factor in shear
	- $1,000N=1kN$

![[../../../../../docs/assets/img/image.webp|640x364]]

#### Stiffness | Serviceability

- $\Delta=\frac{5wL^4}{384\times E I}$
- $E I=\frac{5wL^4}{384\times \Delta}$

#### Calculations / Example


---

# Excalidraw Data

## Text Elements
%%
## Drawing
```compressed-json
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
```
%%