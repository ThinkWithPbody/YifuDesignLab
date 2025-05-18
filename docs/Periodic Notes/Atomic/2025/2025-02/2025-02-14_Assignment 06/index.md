---
excalidraw-plugin: parsed
excalidraw-open-md: true
tags:
  - note_atomic
title: 2025-02-14_Assignment 06
description: 
date: 2025-02-14
name: Assignment 06
slug: 2025-02-14_Assignment 06
people: 
location: 
weekday: 
time: 
share: true
hide: true
---
%%[parents:: [ARC2046H](/docs/Courses/2025/ARC2046H/ARC2046H-Structures_2.md)]%%
### Assignment 06

![2025-02-14_Assignment 06.png](Periodic%20Notes/Atomic/2025/2025-02-14_Assignment%2006/2025-02-14_Assignment%2006.png)

## Question 1
Did you give this question a try? No points are assigned to it.
![479x76](/docs/Periodic%20Notes/Atomic/2025/2025-02/2025-02-14_Assignment%2006/Attachments/2025-02-14_Assignment%2006/A05%20Q01.webp)
![482x261](/docs/Periodic%20Notes/Atomic/2025/2025-02/2025-02-14_Assignment%2006/Attachments/2025-02-14_Assignment%2006/A05%20Table%2001.webp)

Try using this Excel tool: [ARC2046H Calculations.xlsx](https://utoronto-my.sharepoint.com/:x:/g/personal/yifu_ding_mail_utoronto_ca/EUIvkUthhINNmcpESFCSjlQBWeMs9bx2KItOYbW56wy0DQ)

## Question 2
What two dimensions have the most impact on structural design of bending elements?

✔️Length and Depth
Length and Width
Length and Load
Load and Depth
Width and Depth

## Question 3
Match the following:

|     |                         |
| --- | ----------------------- |
| My  | Elastic Yielding Moment |
| Mp  | Plastic Yielding Moment |
| Mu  | Lateral Buckling Moment |
| Mr  | Moment Resistance       |
| Vr  | Shear Resistance        |

## Question 4
Class 1/2 sections are governed by local buckling.

True
✔️False

##### Local Buckling
- **Class 1-2**
	- Plastic Limit (ignoring local buckling)
- **Class 3**
	- Elastic Limit (experiences local buckling in the plastic range)
- Class 4
	- Local Buckling in Elastic Range



## Question 5
Class 3 sections are governed by local buckling.

✔️True
False

## Question 6
For a W310x33, with a yield stress of 345MPa (it's a hot-rolled section) what is My (kNm)? This means its Elastic!
Write you answer in **kNm** to one decimal place (XXX.X). Do not write the units.  

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



Even though the beam is Class 1-2, $S$ is needed to calculate $M_y$.
Find $S$ under [STEEL SECTIONS](/docs/Courses/2025/ARC2046H/Attachments/ARC2046H/STEEL%20SECTIONS.pdf)
$M_y=345\times 415000=143,175,000Nmm=143.2kNm$

## Question 7
For a W310x33, with a yield stress of 345MPa (it's a hot-rolled section) what is Mp (kNm)? This means its Plastic!
Write you answer in **kNm** to one decimal place (XXX.X). Do not write the units.

$M_p=345\times Z=165.6kNm$

## Question 8
What is the Mr of a W310x33 if we assume it is continuously braced, or very, very short? We know it is a Class 1 or 2 section (Plastic Modulus can be used)
Write you answer in **kNm** to one decimal place (XXX.X). Do not write the units.

Plastic Yielding Moment Continuously Braced
$M_r=\phi \cdot fy \cdot Z_x=149.0$

Verified using [ARC2046H Calculations.xlsx](https://utoronto-my.sharepoint.com/:x:/g/personal/yifu_ding_mail_utoronto_ca/EUIvkUthhINNmcpESFCSjlQBWeMs9bx2KItOYbW56wy0DQ)

## Question 9
Calculate the ultimate (or critical) moment, Mu, that would cause the top chord of a W310x33 to laterally buckle if it was only braced every 2500mm?
Write you answer in **kNm** to one decimal place (XXX.X). Do not write the units.

TIP: Plug this into your calculator multiple times. This is the big, horrible, hard equation that often people get wrong simply b/c of entering it wrong. Remember this is trying to buckling in the WEAK AXIS, so about Y-Y for your Moment of Inertia.

$M_u=\frac{w_2\pi}{L_u}\sqrt{EI_yGJ+(\frac{\pi E}{L_u})^2I_yC_w}$
$=\frac{1\times\pi}{2500}\sqrt{200000\times 1920000\times 77000\times 122000+(\frac{\pi \times 200000}{2500})^2\times 1920000\times 43800000000}$
$=118,678,943.49Nmm=118.68kNm$

Verified using [ARC2046H Calculations.xlsx](https://utoronto-my.sharepoint.com/:x:/g/personal/yifu_ding_mail_utoronto_ca/EUIvkUthhINNmcpESFCSjlQBWeMs9bx2KItOYbW56wy0DQ)

## Question 10
For the W310x33 that was only braced every 2500mm, Calculate Mr if ONLY laterally buckling alone governed? (ie Mr= Reduced Mu)
Write you answer in **kNm** to one decimal place (XXX.X). Do not write the units.
Note that there are no points for this questions

##### Moment (Plastic… If Elastic, $M_p$ becomes $M_y$)
- **Moment Resistance [Class 1 & 2](.md#^36391f)**
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
- **Moment Resistance [Class 3](.md#^3044ad)**
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
	- ![371x248](Periodic%20Notes/Atomic/2025/2025-02/2025-02-12_Module%2006%20Steel%20-%20Beam%20Design/Attachments/2025-02-12_Module%2006%20Steel%20-%20Beam%20Design/image.webp)



$M_r=\phi \times M_u=0.9 \times 118.68=106.8$

## Question 11
What is the Mr for the W310x33 with Lu=2500mm? Calculate by hand (use the data from previous questions)
Write you answer in **kNm** to one decimal place (XXX.X). Do not write the units.
Note that there are no points for this questions

$(M_u=118.68)!<(0.67\times M_p=110.95)$
$M_r=\min(1.15\phi M_p(1-\frac{0.28M_p}{M_u}),\phi M_p)$
$=min(104.43,149.04)=104.4 kNm$

Verified using [ARC2046H Calculations.xlsx](https://utoronto-my.sharepoint.com/:x:/g/personal/yifu_ding_mail_utoronto_ca/EUIvkUthhINNmcpESFCSjlQBWeMs9bx2KItOYbW56wy0DQ)

## Question 12
What is the Mr for the W310x33 with Lu=2500mm? Use the steel beam tables for Mr.
Write you answer in **kNm** to no decimal places (XXX). Do not write the units.

[STEEL BEAM TABLES](/docs/Courses/2025/ARC2046H/Attachments/ARC2046H/STEEL%20BEAM%20TABLES.pdf)
$Mr_{2500}=104$

## Question 13
What is the Vr of a W310x33? Try calculating by hand, but verify with the Steel Beam Tables.
Write you answer in **kN** to no decimal places (XXX). Do not write the units.

$Vr=423$

## Question 14
Did you try and do this question? (This is the only way I can make a question a Participation Question)

Plot the Moment Resistance of a W310x39 vs it’s unbraced length, looking up the Mr in the Steel Beam Tables. Look up the Shear resistance as well.

![398x213](/docs/Periodic%20Notes/Atomic/2025/2025-02/2025-02-14_Assignment%2006/Attachments/2025-02-14_Assignment%2006/A05%20Table%2002.webp)

## Question 15
Did you try and do this question? (This is the only way I can make a question a Participation Question)

Last week we needed to check a column in a renovation. The building was built in the 1950’s, when fy was 230MPa. In the same building, check and see if the roof member will work. The new factored moment on the 9m long W360x33 is 105kNm. The section is a Class 1/2 member. The existing joists, which brace the top flange, are every 3m. Ignore Serviceability requirements.   
If the beam doesn’t work, look up what new beam we could replace it with (fy=345MPa)

$M_r=93.44<105$, Won't work

![image](/docs/Periodic%20Notes/Atomic/2025/2025-02/2025-02-14_Assignment%2006/Attachments/2025-02-14_Assignment%2006/image.webp)

The beam $M_r>105$ at $L_u=3000$ with similar flange width and lower mass is W360x33 ($M_r=113$)

---

# Excalidraw Data

## Text Elements
%%
## Drawing
```compressed-json
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
```
%%