---
excalidraw-plugin: parsed
excalidraw-open-md: true
tags:
  - note_atomic
  - Courses_2025_ARC2046H_Exam
title: 
description: 
date: 2025-03-12
name: Module 09 Composite Materials
slug: 2025-03-12_Module 09 Composite Materials
people: 
location: 
weekday: 
time: 
share: true
hidden: true
---
%%[parents:: [ARC2046H](../../../../../Courses/2025/ARC2046H/index.md)]%%
### Composite Materials

![2025-03-12_Module 09 Composite Materials.svg](Periodic%20Notes/Atomic/2025/2025-03-12_Module%2009%20Composite%20Materials/2025-03-12_Module%2009%20Composite%20Materials.svg)

- Load Sharing
	- When two element or materials are arranged so that they mutually support load they are said to be sharing the load.
	- The proportion of load that each resists is proportional to the stiffness of that element or material.
		- Load will follow the path of greatest resistance (or the stiffest element)
		- Multiple elements supporting the same load share it based on stiffness
		- The load likes the path with the MOST resistance.
	- To share load at all, they need to move (squash) together
		1. $\sigma=F/A$ | $F=\sigma \times A$
		2. $\varepsilon=\Delta L/L$
			1. [Periodic Notes/Atomic/2025/2025-02/2025-02-12_Stress and Strain/2025-02-12_Stress and Strain](../../2025-02/2025-02-12_Stress%20and%20Strain/index.md#881997)
		3. $E=\sigma / \varepsilon$ | $\sigma=E \times \varepsilon$
	- Rearrange 3 into 1
	- $F=E \times \varepsilon \times A$
		- $E$ and $A$ are for each material
		- $\varepsilon$ has to be the same because they are moving together
		- $\therefore$ For each material $x$
			- $F_x=(E \times A)_x \times \varepsilon$
		- $\therefore$ $F=F_s + F_c=\varepsilon \times ((EA)_s + (EA)_c)=\varepsilon \times \sum(EA)$
			- $\sum(EA)$ is the axial stiffness of the combined system
		- $\therefore$ $\varepsilon=F/\sum(EA)$
		- $\because$ $F_x=(EA)_x \times \varepsilon$
		- $\therefore$ $F_x=F \times (EA)_x / \sum(EA)$
	- $F_x=F \times (EA)_x / \sum(EA)$
		- $E(MPa)$
		- $A(mm^2)$
		- $EA(N)$

- Load Sharing Example
	- We have a steel HSS152x152x9.5 column filled with concrete. What load (kN) does the steel carry and what load does the concrete carry if Ec = 30,000MPa? Take a guess which will carry more load. Steel or Concrete?

- Transformed Sections #Courses/2025/ARC2046H/Exam 
	- Transform the Steel into Concrete from the previous example
		- HSS152x152x9.5, filled with concrete with E=30,000MPa
	- We can think of one of the elements in terms of the other. We “transform” the section
		- So for ANY object of ANY material (or combo of materials) will act the same as long as S(EA) is the same!
	- $A_{Transformed}=n \times A_s$
		- $n=E_s/E_c$: Ratio of Modular of Elasticity
		- $A_t=E_s \div E_c \times A_s=200,000 MPa \div 30,000 MPa \times 5210 mm^2=34,733 mm^2$
			- $A_{total}=A_t + A_c=34,733+17,689=52,422 mm^2$

- Composite Action
	- If two objects or materials are combined so that they support load as one, the system is said to be composite.  In order for a system to be considered composite, the materials must be bonded so that they won’t slip relative to each other
		- In axial loading, this is easy. But in bending, we need to make sure shear can be transferred across the plane where the materials interface
		- They can be two different materials (like our example) or two pieces of wood (glulam beams)
	- For bending elements, **longitudinal shear** is **critical**
		- If there is no bond along the interface (or SHEAR PLANE), the elements will slip along that plane. That’s like two small beams sharing load
		- If we ensure the two planes don’t slip, it’s like we have one deep beam
	- Composite vs Non-Composite, two 140x140 beams
		- A (Axial and Shear)
			- $A_{sharing} = 140 \times 140 + 140 \times 140 = 39,200mm^2$
			- $A_{composite} = 140 \times 280 = 39,200mm^2$
			- $A_{composite} = A_{sharing}$
		- S (Moment)
			- $S_{sharing} = 140 \times 1402/6 + 140 \times 1402/6 = 0.915 \times 106mm^3$
			- $S_{composite} = 140 \times 2802/6 = 1.83 \times 106mm^3$
			- $S_{composite} = 2 \times S_{sharing}$
		- I (Stiffness)
			- $I_{sharing} = 140 \times 1403/12 + 140 \times 1403/12 = 64.0 \times 106mm^4$
			- $I_{composite} = 140 \times 2803/12 = 256 \times 106mm^4$
			- $I_{composite} = 4 \times I_{sharing}$

- Composite Structural Construction
	- ![640x232](./Attachments/2025-03-12_Module%2009%20Composite%20Materials/image.webp)
	- ![355x298](./Attachments/2025-03-12_Module%2009%20Composite%20Materials/image-1.webp)


---

# Excalidraw Data

## Text Elements
%%
## Drawing
```compressed-json
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
```
%%