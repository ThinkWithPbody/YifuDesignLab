---
excalidraw-plugin: parsed
excalidraw-open-md: true
tags:
  - note_atomic
title: 2025-02-12_Stress and Strain - Part 02
description: 
date: 2025-02-12
name: Stress and Strain - Part 02
people: 
location: 
weekday: 
time: 
share: true
hidden: true
---
%%[parents:: [2025-02-12_Stress and Strain - Part 02](index.md)]%%
### Stress and Strain - Part 02

![2025-02-12_Stress and Strain - Part 02.png](Periodic%20Notes/Atomic/2025/2025-02-12_Stress%20and%20Strain%20-%20Part%2002/2025-02-12_Stress%20and%20Strain%20-%20Part%2002.png)

- Recap
	- Principals of Stress and Strain (Using Axial)
		- Stress
			- $\sigma(N/mm^2|MPa)=\frac{P(N)}{A(mm^2)}$
		- Strain
			- $\varepsilon (mm/mm|Unitless)=\frac{\Delta L(mm)}{L(mm)}$
		- Modulus of Elasticity
			- $E(MPa)=\frac{\sigma}{\varepsilon}$
	- Neutral Axis and Centroid
		- Neutral Axis
			- The axis about which an object will rotate if spinning freely. (the median line). The mean axis of mass, gravity and inertia.
		- Centroid
			- The mean position of matter in a body.
			- The centre of mass, centre of gravity or centre of inertia.
			- The intersection of neutral axes or median lines.
			- The point about which a body will rotate if spinning freely.
		- Equivalent Couples
			- When a force is applied concentrically to a body it will move or translate in line with the applied force.
			- When a concentric moment is applied to a body it will rotate about its centre of gravity.
			- When a force is applied eccentrically to a body, it will both translate and rotate.
			- The effect on the body will be the same as if a concentric force and moment are applied to the body simultaneously.
	- Equivalent Forces (Couples)
		- Examples
	- Internal Forces
	- Internal Stresses
- Bernoulli Hypothesis
	- Intro
		- Engineer’s Beam Theory or Classic Beam Theory
		- Both da Vinci and Galileo tried to create a “Beam Theory” but didn’t have calculus or Hooke’s Law (springs)
		- Based on ideas from Jacob Bernoulli, it was created in 1750 by Leonhard Euler and Daniel Bernoulli, but people didn’t trust that math could be used in Engineering…
		- Precedent design existed until the Eiffel Tower and Ferris Wheel were designed (1890’s)
		- https://en.wikipedia.org/wiki/Euler%E2%80%93Bernoulli_beam_theory
	1. Plane sections remain plane
		- ![Pasted image 20250129112341](/docs/Periodic%20Notes/Atomic/2025/2025-02/2025-02-12_Stress%20and%20Strain%20-%20Part%2002/Attachments/2025-02-12_Stress%20and%20Strain%20-%20Part%2002/Pasted%20image%2020250129112341.png)
		- For beam-like elements, transverse cross sections perpendicular to the neutral axis remain plane and perpendicular to the neutral axis.
	2. To remain plane, the strain must vary linearly with the distance from the neutral axis
	3. In normal ranges, we know stress and strain are proportional (Modulus of Elasticity). Therefore, the stress must also vary linearly with it’s distance from the neutral axis
- Stress in a beam
	- $M(kNm|1,000,000 Nmm)=\frac{W \cdot L}{2}(kN) \cdot \frac{L}{4}(m)=\frac{W(kN/m)\cdot L^2(m^2)}{8}$
	- Elastic Bending Stress $S$
		- $M(Nmm|\frac{1}{1,000,000} kNm)=\sigma(MPa|N/mm^2) \cdot S(mm^3)$
		- Elastic Bending of any shape, where S is dependant on the profile
		- Use if **Brittle**
	- Plastic Bending Stress $Z$
		- $M=\sigma Z$
		- Plastic Bending of any shape, where Z is dependant on the profile
		- Use if and only if **Ductile**
	- Strain Moment of Inertia $I$
		- $\Delta(mm)=\frac{5 \cdot w(kN/m|N/mm) \cdot l^4(mm^4)}{384 \cdot E(MPa|N/mm^2) \cdot I(mm^4)}$
			- $I_{req}(mm^4)=\frac{5 \cdot w(kN/m|N/mm) \cdot l^4(mm^4)}{384 \cdot E(MPa|N/mm^2) \cdot \Delta(mm)}$
		- Use only if **UDL** Uniformly Distributed Load
	- $r$
		- $M=\sigma r$
	- Shapes
		- Rectangular cross section
			- $S(mm^3)=\frac{b(mm) \cdot d^2(mm^2)}{6}$
			- $Z(mm^3)=\frac{b(mm) \cdot d^2(mm^2)}{4}$
			- $I(mm^4)=\frac{b(mm) \cdot d^3(mm^3)}{12}$
			- $r=\frac{d}{\sqrt{12}}$
		- I Beam50/
	- For I Beam
		- ![500](/docs/Periodic%20Notes/Atomic/2025/2025-02/2025-02-12_Stress%20and%20Strain%20-%20Part%2002/Attachments/2025-02-12_Stress%20and%20Strain%20-%20Part%2002/Pasted%20image%2020250129142127.png)
	- For other Geometric Sections
		- ![600](/docs/Periodic%20Notes/Atomic/2025/2025-02/2025-02-12_Stress%20and%20Strain%20-%20Part%2002/Attachments/2025-02-12_Stress%20and%20Strain%20-%20Part%2002/Pasted%20image%2020250129142735.png)
	- Take away
		- Deformation and strength are related for each material and we have data on most materials when they are in a normal range of behaviour.
		- There are section properties that allow us to calculate strength and deformation of shapes.
		- Combine our knowledge of the shape and the material, and we can design members to a certain strength and deformation.
		- Biggest Impacts on Design
			- $L$
				- $L^2$ Strength
					- $M=\frac{W\cdot L^2}{8}$
				- $L^4$ Serviceability
					- $\Delta=\frac{5 \cdot w \cdot l^4}{384 \cdot E \cdot I}$
			- $d$
				- $d^2$ Strength
					- $S=\frac{b \cdot d^2}{6}$
				- $d^3$ Serviceability
					- $I=\frac{b \cdot d^3}{12}$
- Examples
	1. A simply supported steel beam spans 4.0m. If the factored load on the beam is 7.8 kN/m, and the reduced capacity of the steel is 0.9*300MPa, what depth does it need to be if it is 13mm wide rectangle? Check for elastic and plastic behavior.
	2. What is the stress on a simply supported W310x39 beam that spans 5.6 m and has a factored load of 27.5 kN/m if the beam remains in the elastic zone.
	3. d required?
		- wf=50kN/m
		- L=10m
		- b=50mm
		- Steel $\phi$fy=270 MPa
		- Steel E = 200,000 MPa
		- Dmax = L/360
		- Limit to Elastic Behavior
			- $I = 5*50*10000^4/384/200000/10000*360$
			- $d=\sqrt[3]{I*12/50}$


---

# Excalidraw Data

## Text Elements
%%
## Drawing
```compressed-json
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
```
%%