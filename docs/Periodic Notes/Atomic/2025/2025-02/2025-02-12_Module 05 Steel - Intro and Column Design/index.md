---
share: true
hidden: true
excalidraw-plugin: parsed
excalidraw-open-md: true
tags:
  - note_atomic
  - Courses_2025_ARC2046H_Exam
  - course
title: 2025-02-12_Module 05 Steel - Intro and Column Design
description: 
name: Module 05 Steel - Intro and Column Design
date: 2025-02-12
people: 
location: 
weekday: 
time: 
---

%%[parents:: [[index|2025-02-12_Module 05 Steel - Intro and Column Design]]]%%

### Steel - Intro and Column Design

![[Periodic Notes/Atomic/2025/2025-02-12_Module 05 Steel - Intro and Column Design/2025-02-12_Module 05 Steel - Intro and Column Design.png|Periodic Notes/Atomic/2025/2025-02-12_Module 05 Steel - Intro and Column Design/2025-02-12_Module 05 Steel - Intro and Column Design.png]]

- Steel Sections and Properties
	- Hot Rolled
		- 345 MPa
	- Cold Rolled
		- 350 MPa
		- Manufactured from plate
	- Naming Convention
		- W150x30
			- ~150mm Deep
			- 30kg/m
		- L102x76x9.5
			- d;b;t
				- 102 Deep
				- 76 Wide
				- 0.5 Thickness
		- HSS152x102x6.4
			- HSS: Hollow Structural Section
			- d;b;t
		- HP Shapes (heavy I-shapes)
		- M Shapes (very light I-shapes)
		- SLB Shapes (super light beams)
		- S Shapes (I-shapes with tapered flanges)
		- WT Shapes (Structural Tees)
		- CFC & CFZ (cold formed)
		- WWF (Welded wide flange)
	- Typical Steel Properties
		- fy = 350 MPa for HSS sections (Cold Formed)
		- fy = 345 MPa for W, C, L sections (Hot Rolled)
		- fu = 450 MPa
		- E = 200,000 MPa
		- G = 77,000 MPa
	- Typical Steel Reduction Factors
		- HP Shapes (heavy I-shapes)
		- M Shapes (very light I-shapes)
		- SLB Shapes (super light beams)
		- S Shapes (I-shapes with tapered flanges)
		- WT Shapes (Structural Tees)
		- CFC & CFZ (cold formed)
		- WWF (Welded wide flange)
- **Tension Resistance | Tensile Capacity**
	- $T_r=\phi \cdot A_g \cdot f_y$
		- Derived from $\sigma=\frac{P}{A}$
		- $\phi$: The material factor, 0.9 for steel
		- $T_r$: Tension force, reduced
		- $A_g$: Gross Sectional Area
		- $f_y$: Yield Strength of Steel | $\sigma$ = 350 MPa
	- $T_r=0.85 \cdot \phi \cdot A_\text{ne} \cdot f_u$
		- $A_\text{ne}$: Net cross sectional area, reduced for bolt holes etc.
		- $f_u$: Ultimate Strength of Steel = 450 MPa
- **Compression Squashing** (Strength) ^3a6dc5
	- $P_y=f_yA$
		- Derived from $\sigma=\frac{P}{A}$
- **Compression Buckling** (Stiffness)
	- $P_\text{cr}=\frac{\pi^2\cdot E\cdot I}{(kL)^2}$
		- $P_\text{cr}$: The critical load, or buckling load
		- $\pi$: 3.14159
		- $E(MPa)$: The modulus of elasticity of the material (200000)
		- $I(mm^4)$: The moment of inertia in the direction that the member is allowed to buckle (often Iyy)
		- $kL(mm)$: The effective length of the member
- **Combine Squashing and Buckling** #Courses/2025/ARC2046H/Exam
	- $C_r=\phi\cdot A \cdot f_y \cdot (1 + \lambda^{2 \cdot n})^\frac{-1}{n}$ ^779b09
		- $C_r = 0$ if $kL/r > 200$
		- $C_r$: the compression capacity
		 - $\phi$: the material factor (0.9 for steel)
		- $A (mm^2)$: the cross sectional area
		- $f_y(MPa)$: the yield strength of the steel (350)
		- $\lambda = \sqrt{f_y/f_{cr}}$
			- $\lambda = \frac{kL}{r}\cdot\sqrt{\frac{f_y}{\pi^2 \cdot E}}$
		- $f_\text{cr}=P_\text{cr}/A$ or the stress at $P_\text{cr}$ ($f$ is the same as $\sigma$)
		- $n=1.34$ (for W shapes and HSS shapes)
		- $r$ = radius of gyration (Shape or Section Property)
			- probably $r_y$ if buckling is in the weak axis

---

# Excalidraw Data

## Text Elements

%%

## Drawing

```compressed-json
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
```

%%
