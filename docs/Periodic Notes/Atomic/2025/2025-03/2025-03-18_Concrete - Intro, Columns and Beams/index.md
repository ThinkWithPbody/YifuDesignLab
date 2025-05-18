---
excalidraw-plugin: parsed
excalidraw-open-md: true
tags:
  - note_atomic
  - Courses_2025_ARC2046H_Exam
title: 2025-03-18_Concrete - Intro, Columns and Beams
description: 
date: 2025-03-18
name: Concrete - Intro, Columns and Beams
slug: 2025-03-18_Concrete - Intro, Columns and Beams
people: 
location: 
weekday: 
time: 
share: true
hide: true
---
%%[parents:: [ARC2046H](/docs/Courses/2025/ARC2046H/ARC2046H-Structures_2.md)]%%
### Concrete - Intro, Columns and Beams

![2025-03-18_Concrete - Intro, Columns and Beams.svg](Periodic%20Notes/Atomic/2025/2025-03-18_Concrete%20-%20Intro,%20Columns%20and%20Beams/2025-03-18_Concrete%20-%20Intro,%20Columns%20and%20Beams.svg)

- Concrete Mix
	- Aggregate
		- Course
		- Fine
	- Water
		- W/C Ratio
	- Sand
	- Portland Cement
	- Entrained Air
		- Little bubbles
	- Admixtures?
		- Plasticizer
		- Fast Cure
	- Fibers?
		- Fiber glass
		- Nylon
		- Rayon
- Concrete
	- Slump Range (mm)
	- Curing
		- 70% Strength at 7 Days
		- If 100% strength is not reached in 28 Days
		- Test again at 56 Days
		- $f'_c$
			- F prime C
- Concrete Stress Strain Curve
	- Concrete
		- $f'_c=25MPa$
			- Structural concrete typically 20-40
			- Specified Concrete Strength for Applications
				- 20 MPa: Footings, Caissons
				- 25 MPa: Foundation Walls, Slab on Grade
				- 30 MPa: Framed Slab, Columns (low-rise)
				- 30-40 MPa: Columns (mid-rise)
				- 30-70 MPa: Columns (high-rise)
		- $E=14,000-41,000$
		- $\phi_c = 0.65$ ^f452bc
			- Concrete is the least predictable of all material
		- $\alpha=0.8$ ^eb0569
			- Uneven distribution of concrete
		- Tensile Strength: 2-5 MPa, assume 0
		- Flexural Strength: 3-5 MPa, assume 0
	- Steel Rebar
		- $f_y=400MPa$
			- Forged instead of rolled or pressed
		- $E=200,000MPa$
		- $\phi_s = 0.85$ ^5616de
		- Steel Rebar Sizes
			- 10M bars are really floppy and bend if stepped on, typically used for shear reinforcing
			- Tend to be spaced as low as 2.5 times the diameter of the bar, as high as 500mm or $3\times t_{wall/slab}$
			- Usually fewer larger bars is cheapest, but more smaller bars work better
				- Typically 15M, 20M, 25M in structural design
				- 45M and 55M are available, but as a last resort - use of expensive couplers

| Sizes | A (mm²) |
|-------|---------|
| 10M   | 100     |
| 15M   | 200     |
| 20M   | 300     |
| 25M   | 500     |
| 30M   | 700     |
| 35M   | 1000    |
| 45M   | 1500    |
| 55M   | 2000    |

- Reinforcing / Development
	- Compression
		- Concrete and steel share compression load based on stiffness
		- Steel has 2 roles in compression
			- Longitudinal steel carries load, needs to be designed
			- Ties keep concrete from "bursting" prior to reaching full compressive strength
		- Why steel in concrete is great
			- Column is composite - Strain must be the same for steel and concrete.
			- Steel is much stiffer than concrete (Es=200,000MPa > Ec=30,000MPa)
			- Steel Stress will be much higher than Concrete Stress (same strain)
			- Steel yields before concrete reaches full stress capacity (around e=0.0015) , but the steel will continue to yield (we like yielding!) until the concrete fails (e=0.0030)
			- We use the best parts of both materials, to their limit!
- Compression
	- $\rho$
	- Basic Compression (Force = Strength × Area)
	- $P_r = 0.80P_{r0}$  (to account for possible eccentricity)
	- $P_{r0} = P_{rc} + P_{rs}$
		- $P_{r0}$ = The column resistance with no eccentricity
		- $P_{rc}$ = The resistance due to concrete
		- $P_{rs}$ = The resistance due to steel
	- $P_{rc} = a_1 f_c f’_c A_c$
		- $\alpha_1$ = 0.8 (close) factor for uneven distribution of concrete
		- $f_c$ = 0.65 Concrete reduction factor
		- $f’_c$ = specified concrete strength (25 MPa to 35 MPa)
		- $A_c$ = Area of concrete
	- $P_{rs} = f_s f_y A_s$
		- $f_s$ = 0.85 rebar reduction factor
		- $f_y$ = 400 MPa steel yield strength ^273812
		- $A_s$ = Area of steel
	- Transformed Sections
		- $\rho=A_s / A_g$
		- $p_{r0}=A_g(\rho \times \phi_s \times f_y + (1 - \rho) \times \alpha_1 \times \phi_c \times f'_c)$
		- $p_r=0.8\times p_{r0}$
- **Moment at ends**
	- Concrete Compression with Moment
	- Concrete columns end up taking Moment. Column design needs to account for Axial load and Bending Moment
	- Interaction Diagram
		- ### Interaction Diagram
		
		![2025-03-19_Interaction Diagram.svg](Periodic%20Notes/Atomic/2025/2025-03/2025-03-19_Interaction%20Diagram/2025-03-19_Interaction%20Diagram.svg)
		
		
		
		---
		- Calculation
			- $\gamma h=h - 2\times(Cover + \unicode{x2300}Ties + \frac{1}{2}\unicode{x2300}Bars)$ ^adc004
			- $\gamma = \gamma h \div h$
			- $A_g(mm^2)=b \times h$
			- $P_r/A_g(MPa)=P_F(N) \div A_g(mm^2)$
			- $M_r/A_{gh}(MPa)=M_F(Nmm) \div (A_g \times h)$
			- $P_g=e=A_s \div A_g$
				- $A_s{req}=e \times A_g=P_g \times A_g$
				- $N_{Bars}=A_s{req} \div A_{Bars}$
				- Evenly distributed (4,8,12,16,etc)
- **Slenderness (Buckling)**
	- Concrete isn’t as easily governed by buckling b/c it’s stocky
	- If there are Shear Walls acting as the LLRS, 90% Concrete Columns get to ignore Slenderness
	- Slenderness effects may be neglected for columns if:
		- $k_{Lu}/r < 34-12M_1/M_2$, where
			- k = effective length factor (similar to steel)
			- Lu = unbraced length of member
			- M1 = Smaller End Moment
			- M2 = Larger End Moment
- Bending
	- ![2025-03-18_Concrete - Intro, Columns and Beams-image](/docs/assets/img/2025-03-18_Concrete%20-%20Intro,%20Columns%20and%20Beams-image.webp)
		- Cover = Fire protection, from code
		- Bottom Steel = “Tension” bars
		- Top Steel = Holds stirrup. Unless reverse bending, As’
			- Top steel for reverse bending if any, or just to hold the ties
		- Stirrups = Shear, Shrinkage Cracks
		- h = height
		- b = width
		- d = Top to center of working steel
			- Note $h$ and $d$ is different in concrete beams - d is to the center of steel - concrete has no tension
	- Balanced, Over or Under Reinforced
		- Balanced: rebar reaches yield stress as concrete reaches f’c.
		- Over-reinforced: Concrete reached f’c before the steel yields.  The member acts very brittle
		- Under-reinforced: Steel yields before the concrete reaches f’c. Steel will continue to deform without a change in stress until the concrete has achieved its maximum stress.  This results in desirable ductile behaviour.  Therefore it is our objective for bending members to be under-reinforced. This does NOT mean it’s under-designed.
	- Bending Design
		- Concrete
			- Concrete in the tension zone cracks so concrete on the tension side of the neutral axis is neglected
			- Beam will be under-reinforced, so the reinforcing steel and the concrete will reach their design stresses.
			- The parabolic stress profile in the concrete can be approximated by a rectangular one.
			- The diagrams show the stress distribution in concrete at various states of loading.
		- Stress Profile
			- ![2025-03-18_Concrete - Intro, Columns and Beams-image-1-1](/docs/assets/img/2025-03-18_Concrete%20-%20Intro,%20Columns%20and%20Beams-image-1-1.webp)
			- ![2025-03-18_Concrete - Intro, Columns and Beams-image-2](/docs/assets/img/2025-03-18_Concrete%20-%20Intro,%20Columns%20and%20Beams-image-2.webp)
			- ![2025-03-18_Concrete - Intro, Columns and Beams-image-3](/docs/assets/img/2025-03-18_Concrete%20-%20Intro,%20Columns%20and%20Beams-image-3.webp)
				- #Courses/2025/ARC2046H/Exam 
				- $T(N)=\phi_S \times A_S \times f_y$
				- $C_c(N) = \alpha_1 \times \phi_c \times f’_c \times A_c$
				- $A_c(mm^2) = b \times \beta_1c$
				- $\beta_1c(mm)= T/ (\alpha_1 \times \phi_c \times f’_c \times b)$: Height Of Stress Profile 
				- $M_r(Nmm) = T \times (d-(\beta_1c)/2)$
				- [^eb0569](index.md#^eb0569)
				- [^5616de](index.md#^5616de)
				- [^f452bc](index.md#^f452bc)
				- [^273812](index.md#^273812)
	- Beam Tips
		- A slab is a wide flat beam.
		- Concrete beams are not always rectangular.  T-shaped beams use the slab in compression. The design basis for a T-beam is the same as that for a rectangular beam.
		- Ensure that the beam is under-reinforced for the basic premise to hold true.  Limit the depth of the compression block to a specified maximum.
		- Can increase bending resistance by adding reinforcement in the compression zone. 
- Shear
	- $V_r(N) = V_c + V_s$
	- $V_c(N) = 0.2 \times \lambda \times \phi_c \times \sqrt{f’_c} \times b_w \times d$
	- $V_s(N) = \phi_s \times A_v \times f_y \times d \div s$
	- Where
		- $V_c$ = the shear resistance of the concrete
		- $V_s$ = the shear resistance of the steel 
		- $\lambda$ = 1.0 for normal concrete. Factor for low density concrete.
		- $b_w$ = minimum effective web width within the depth d. (Usually b)	
		- $A_v$ = cross sectional area of reinforcing steel crossing the tension plane.
			- Note that a typical stirrup has two vertical legs and they both count separately so that Av equals the cross sectional area of the bar times the number of vertical legs.
		- $s$ = the spacing of the stirrups
- Continuous Beams
	- ![2025-03-18_Concrete - Intro, Columns and Beams-image-4](/docs/assets/img/2025-03-18_Concrete%20-%20Intro,%20Columns%20and%20Beams-image-4.webp)
	- ![2025-03-18_Concrete - Intro, Columns and Beams-image-5](/docs/assets/img/2025-03-18_Concrete%20-%20Intro,%20Columns%20and%20Beams-image-5.webp)
	- 

---

# Excalidraw Data

## Text Elements
%%
## Drawing
```compressed-json
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
```
%%