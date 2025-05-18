---
excalidraw-plugin: parsed
excalidraw-open-md: true
tags:
  - note_atomic
title: 2025-02-12_Assignment 02
description: 
date: 2025-02-12
name: Assignment 02
people: 
location: 
weekday: 
time: 
share: true
hide: true
---
%%[parents:: [[../../../../../Courses/2025/ARC2046H/ARC2046H-Structures_2|ARC2046H]]]%%
### Assignment 02

![[Periodic Notes/Atomic/2025/2025-02-12_Assignment 02/2025-02-12_Assignment 02.png|Periodic Notes/Atomic/2025/2025-02-12_Assignment 02/2025-02-12_Assignment 02.png]]

**Question 1**
What live load would be required for the design of living room floor members in a residential unit?
Group of answer choices

7.2 kPa
1.9 kPa
✔️4.8 kPa
2.4 kPa
1.4 kPa

**Question 2**
What is the total dead load (kPa) for a roof with asphalt strip shingles, 19mm plywood sheathing, 2x8 joists at 16" c/c, 100mm of blown glass fibre insulation, 20mm of gypsum wallboard, and assuming an allowance of 0.05 kPa for mechanical/electrical?
Group of answer choices

0.55 kPa
✔️0.60 kPa
0.72 kPa
0.69 kPa
0.52 kPa

	Refer to `DEAD LOADS.pdf`
	asphalt strip shingles => 0.15
	19mm plywood sheathing => 0.11
	2x8 joists at 16" c/c => 0.09 ($8in = \lfloor203mm\rfloor=184mm$)
	100mm of blown glass fibre insulation => 0.04
	20mm of gypsum wallboard => 0.16
	mechanical/electrical => 0.05
	$\sum = 0.60 kPa$

**Question 3**
For the following loads acting on a roof, what would the worst case Factored Load Combination be? All loads are acting downward. Dead=1.25kPa, Live=2.40kPa, Snow=1.12kPa and Wind=1.00kPa
Group of answer choices

5.77 kPa
✔️6.28 kPa
6.68 kPa
5.16 kPa
5.64 kPa

	Refer to `LOAD COMBINATIONS.pdf`
	Use the Ultimate Limit States Calculator above

**Question 4**
The following is a part plan from a project under construction. What is the Length of 2WB04?
Provide your answers in meters.
![[../../../../../assets/img/Part Plan NFX.jpg|400]]

	12

**Question 5**
From the same partial plan as the previous question, what is the Tributary Width of 2WB04?
Provide your answers in meters.

	4

**Question 6**
From the same partial plan as the previous questions, what is the Tributary Area of 2WB04?
Provide your answers in m2.

	48

**Image for question 7-11**
![[../../../../../assets/img/Pasted image 20250115172052.png|Pasted image 20250115172052]]
*Dumbest answers are provided for when you can't trust your instincts.*

**Question 7**
For the following question, what are the Reactions (kN)?
Write your answer to 1 decimal place (XX.X)

wf = 9.3 kN/m
L = 13.4 m

	$\lfloor\frac{9.3\times13.4}{2}\rfloor=62.3$

**Question 8**
For the following question, what the maximum Vf (kN)?
Write your answer to 1 decimal place (XX.X). The Numbers differ from the previous question.

wf = 7.9 kN/m
L = 11.2 m

	$R1=\lfloor\frac{7.9\times11.2}{2}\rfloor=44.24$
	$R1-7.9X-V=0$
	$V = 44.24 - 7.9x$
```chart
type: line
labels: [0, 2.8, 5.6, 8.4, 11.2]
series:
  - title: V = 44.24 - 7.9X
    data: [44.24, 22.12, 0, -22.12, -44.24]
tension: 1
width: 77%
labelColors: false
fill: true
beginAtZero: false
bestFit: false
bestFitTitle: undefined
bestFitNumber: 0
```
<pre class="dataview dataview-error">Evaluation Error: ReferenceError: Chart is not defined
    at eval (eval at &lt;anonymous&gt; (plugin:dataview), &lt;anonymous&gt;:18:1)
    at DataviewInlineApi.eval (plugin:dataview:19027:16)
    at evalInContext (plugin:dataview:19028:7)
    at asyncEvalInContext (plugin:dataview:19038:32)
    at DataviewJSRenderer.render (plugin:dataview:19064:19)
    at DataviewJSRenderer.onload (plugin:dataview:18606:14)
    at e.load (app://obsidian.md/app.js:1:1214378)
    at DataviewApi.executeJs (plugin:dataview:19607:18)
    at DataviewCompiler.dataviewJS (plugin:obsidian-mkdocs-publisher:37:47968)
    at convertDataviewQueries (plugin:obsidian-mkdocs-publisher:40:1349)</pre>

**Question 9**
For the following, where is Vf=0 kN?
Write your answer to 1 decimal place (XX.X). The Numbers differ from the previous question.

wf = 6.2 kN/m
L = 11.2 m

	$R1=\lfloor\frac{6.2\times11.2}{2}\rfloor=34.72$
	$R1-6.2X-V=0$
	$V = 34.72 - 6.2x$
	$x=34.72\div6.2=5.6$

**Question 10**
For the following question, what the maximum Mf (kN)?
Write your answer to 1 decimal place (XX.X). The Numbers differ from the previous question.

wf = 7.8 kN/m
L = 9.6 m

	$R1=\lfloor\frac{7.8\times9.6}{2}\rfloor=37.44$
	$\sum_M=0=7.8\times x\times \frac{1}{2}x-37.44x+M_f$
	$M_f=-3.9x^2+37.44x$
	$\arg\max_{x \in (0,9.6)} M_f(x)=-\frac{b}{2a}=4.8$
	$\max_{x \in (0,9.6)} M_f(x)=M_f(4.8)=89.856$
<pre class="dataview dataview-error">Evaluation Error: ReferenceError: Chart is not defined
    at eval (eval at &lt;anonymous&gt; (plugin:dataview), &lt;anonymous&gt;:18:1)
    at DataviewInlineApi.eval (plugin:dataview:19027:16)
    at evalInContext (plugin:dataview:19028:7)
    at asyncEvalInContext (plugin:dataview:19038:32)
    at DataviewJSRenderer.render (plugin:dataview:19064:19)
    at DataviewJSRenderer.onload (plugin:dataview:18606:14)
    at e.load (app://obsidian.md/app.js:1:1214378)
    at DataviewApi.executeJs (plugin:dataview:19607:18)
    at DataviewCompiler.dataviewJS (plugin:obsidian-mkdocs-publisher:37:47968)
    at convertDataviewQueries (plugin:obsidian-mkdocs-publisher:40:1349)</pre>

**Question 11**
For the following question, where does the maximum Mf occur?
Write your answer to 1 decimal place (XX.X). The Numbers differ from the previous question.

wf = 9.7 kN/m
L = 13 m

	$R1=\lfloor\frac{9.7\times13}{2}\rfloor=63.05$
	$\sum_M=0=9.7\times x\times \frac{1}{2}x-63.05x+M_f$
	$M_f=-4.85x^2+63.05x$
	$\arg\max_{x \in (0,9.6)} M_f(x)=-\frac{b}{2a}=6.5$
<pre class="dataview dataview-error">Evaluation Error: ReferenceError: Chart is not defined
    at eval (eval at &lt;anonymous&gt; (plugin:dataview), &lt;anonymous&gt;:18:1)
    at DataviewInlineApi.eval (plugin:dataview:19027:16)
    at evalInContext (plugin:dataview:19028:7)
    at asyncEvalInContext (plugin:dataview:19038:32)
    at DataviewJSRenderer.render (plugin:dataview:19064:19)
    at DataviewJSRenderer.onload (plugin:dataview:18606:14)
    at e.load (app://obsidian.md/app.js:1:1214378)
    at DataviewApi.executeJs (plugin:dataview:19607:18)
    at DataviewCompiler.dataviewJS (plugin:obsidian-mkdocs-publisher:37:47968)
    at convertDataviewQueries (plugin:obsidian-mkdocs-publisher:40:1349)</pre>

**Question 12**
What is the worst Cf (kN) on the following column?
![[../../../../../assets/img/Pasted image 20250115172353.png|300]]
296 kN
182 kN
✔️263 kN
322 kN
346 kN

**Question 13**
In the previous question, where does the maximum Cf occur on the column?
Group of answer choices

At L3
✔️L1 to L2
Below L1
L3 to Roof
L2 to L3
z`

---

# Excalidraw Data

## Text Elements
%%
## Drawing
```compressed-json
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
```
%%