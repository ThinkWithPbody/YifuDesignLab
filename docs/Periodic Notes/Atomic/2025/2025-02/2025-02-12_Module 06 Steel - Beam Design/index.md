---
excalidraw-plugin: 
excalidraw-open-md: true
tags:
  - note_atomic
title: 2025-02-12_Module 06 Steel - Beam Design
description: 
date: 2025-02-12
name: Module 06 Steel - Beam Design
people: 
location: 
weekday: 
time: 
share: true
hidden: true
---
%%[parents:: [2025-02-12_Module 06 Steel - Beam Design](index.md)]%%
### Module 06 Steel - Beam Design

![2025-02-12_Module 06 Steel - Beam Design.png](Periodic%20Notes/Atomic/2025/2025-02-12_Module%2006%20Steel%20-%20Beam%20Design/2025-02-12_Module%2006%20Steel%20-%20Beam%20Design.png)

#### Lateral Torsional Buckling

##### Local Buckling
- **Class 1-2** ^36391f
	- Plastic Limit (ignoring local buckling)
- **Class 3** ^3044ad
	- Elastic Limit (experiences local buckling in the plastic range)
- Class 4
	- Local Buckling in Elastic Range

##### Yielding Moments (kNm)
- **Elastic**
	- $M_y=\sigma S$
- **Plastic**
	- $M_p=\sigma Z$
- If a beam is continuously braced at the top
	- **Elastic**
		- $M_r=\phi \cdot fy \cdot S$
	- **Plastic**
		- $M_r=\phi \cdot fy \cdot Z$

##### Lateral Buckling Moment
- $M_u=\frac{w_2\pi}{L_u}\sqrt{EI_yGJ+(\frac{\pi E}{L_u})^2I_yC_w}$
	- $M_u$ = the bending moment which results in lateral buckling of the compression flange. 
		- U stands for ultimate, but we could say critical.
	- $w_2$ = 1.0 (if M at middle is greater than M at ends)  (all simply supported beams)
	- $\pi$ = 3.14
	- $L_u$ = the laterally unsupported length of the compression flange
	- $E$ = the modulus of elasticity
	- $I_y$ = the moment of inertia of the beam in the direction opposite to the applied load
	- $G$ = the shearing modulus of elasticity, generally 77,000 MPa
	- $J$ = the polar moment of inertia (From Beam properties)
	- $C_w$ = the warping constant (From Beam properties)

#### Total Steel Beam Capacity $V_r$ & $M_r$

##### Moment (Plastic… If Elastic, $M_p$ becomes $M_y$)
- **Moment Resistance [Class 1 & 2](index.md#^36391f)**
	- $M_r$
		- If $M_u<=0.67M_p$
			- $M_r=\phi M_u$
		- Else $M_r=1.15\phi M_p(1-\frac{0.28M_p}{M_u})$
		- If $M_r>\phi M_p$
			- $M_r=\phi M_p$
	- Where
		- $\phi=0.9$
		- $M_u$ = Buckling moment at the unsupported length
		- $M_p$ = Plastic Moment (with no reduction factor) $Z$
- **Moment Resistance [Class 3](index.md#^3044ad)**
	- $M_r$
		- If $M_u<=0.67M_y$
			- $M_r=\phi M_u$
		- Else $M_r=1.15\phi M_y(1-\frac{0.28M_y}{M_u})$
		- If $M_r>\phi M_y$
			- $M_r=\phi M_y$
	- Where
		- $\phi=0.9$
		- $M_u$ = Buckling moment at the unsupported length
		- $M_y$ = Elastic Moment (with no reduction factor) $S$
- Moment Resistance Curve
	- ![371x248](/docs/Periodic%20Notes/Atomic/2025/2025-02/2025-02-12_Module%2006%20Steel%20-%20Beam%20Design/Attachments/2025-02-12_Module%2006%20Steel%20-%20Beam%20Design/image.webp)

##### Shear
- $V_r=\phi A_wF_s$
	- $V_r$ = Reduced shear resistance
	- $\phi$ = Material Reduction Factor for Steel, 0.90
	- $A_w$ = Area of Web, d*w
	- $F_s$ = ultimate shear stress, varies depending on slenderness of web
		- = $0.66\times Fy$ for stocky members
- Tips
	- Use [BEAM LOADING DIAGRAMS](/docs/Courses/2025/ARC2046H/Attachments/ARC2046H/BEAM%20LOADING%20DIAGRAMS.pdf) to determine $M_f$ and $V_f$


%%
# Excalidraw Data

## Text Elements

## Drawing
```compressed-json
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
```
%%