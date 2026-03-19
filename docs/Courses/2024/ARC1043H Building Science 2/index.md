---
tags:
  - course
start: 2024-01-05
due:
completion: 2024-04-01
people:
  - "[[People/Bomani Khemet|Bomani Khemet]]"
location: DA200
weekday: 1
time: 900
share: true
status: DONE
---
## Course Brief

[code:: ARC1043H]
[title:: Building Science 2]

## Modules

### Module 1

#### Requirements for exterior walls
1. Strength
2. Durable
3. Economical
4. Aesthetically pleasing
5. Heat
6. Wind
7. Moisture
8. Rain
9. Solar and UV
10. Sound and Noise
11. Fire

#### Building Enclosures
- Volume to Surface area ratio
- Form that sheds snow and rain
- No windows
- Climate

#### Degree Days
T.base = 18℃
##### Heating Degree Days (HDD)
HDD = SUM(IF(T.average < T.base, (T.base - T.average) * Days in month))
##### Cooling Degree Days (CDD)
CDD = SUM(IF(T.average > T.base, (T.average - T.base) * Days in month))

### Module 2

Chapter 15.6

Heat flow between environmental separators 
Interior, exterior, microclimate, soil

HDD => RSI, R

Perfect wall: continuous insulation, moisture control, 
HRV: recycles and captures interior heat
Insulated glass frame, filled with: air, argon, krypton, xenon > heavier
VIP: Vacuum insulated panel
XPS: extruded polystyrene 

Saskatchewan conservation home: innovative low energy home
Originally a solar home
R7

Heat transfer types:
- Conduction
	- Occurs through 
		- solids
		- still liquids
		- still gases
- Convection
	- Occurs through 
		- Moving liquids
		- Moving gases
- Radiation
	- Always radiating out energy cold or hot unless at absolute zero, 0K
	- Occurs through
		- Vacuum
		- Gases
		- Liquids

Thermal resistance definition:
R: thermal resistance (m^2 C / W) = l: Thickness of material (m) / k: thermal conductivity (W / m C)

Thermal transmittance ( W / m^2 C): U = 1 / R

U = k / l

Interstitial temperatures:
Change in temperature across a single material: Delta T m = R material / R total * Delta T total
Delta T total = Absolute( T in - T out)

### Module 3

**Degree days average calculation base / balance point temperature**
Canada 18
Denmark 14

**Thermal Resilience**
Winter: 2 hours - 2 days
Summer: 12 hours - 4 days

Heating: Cents / kWh

Annual heating / cooling load: kWh / m^2 / a (annual) or W / m^2
Energy intensity: 

Heat flow / Q (W)
= Area (m^2) * {Delta T (C) | Degree Days (C-Days)} / Thermal Resistance R (m^2 C / W or ft^2 F / Btu)
= Area (m^2) * {Delta T (C) | Degree Days (C-days)} * Thermal Conductivity U (W / m^2 C)

Thermal Resistance:
R = RSI * 5.678 = 1 / U
R: hr ft^2 F / Btu
RSI: m^2 K / W

1 kWh = 41.667 Wd
1 Wd = 0.024 kWh
1 kW = 3600 kJ/h
1 Year = 8765.999 h

**Passive House**: sustainability standard, 15 kWh / m^2 / an or 10 W / m^2


### Module 4

Passive house: performance based guideline
OBC descriptive: 1400 pages
German performance: 400 pages

Psi: variable for linear thermal bridge
Chi: linear thermal bridge
Q = U * A * DeltaT + Psy * L * DeltaT + Chi * n

R Effective = A Total /  (A 1 / R 1 + A 2 / R 2 )
OC = On center

### Module 5

### Module 6

20-25mm diameter stones, free draining soil and gravel with no fine particles 

M (vapour permeance)= u (material vapour permeability) / l (material thickness)
1 perm = 57 ng (nanograms of water)/ (Pa (Pascal)* m^2 * s (seconds))
OBC Vapor barrier: 60 ng/(Pa m^2 s)

Vapour flow (ng)= M * A (m^2 area) * Theta (s time) * (Pwvin- Pwvout) (Pa vapour pressure difference)
### Module 7

Sea level = 101.325 kPa (kN / m^2) (force / surface area)
Average human area = 0.15 - 0.4 m^2
Force = Force m (kg) * Acceleration a (m / s^2)
Airflow: pressure difference & path
NPP / NPL: Neutral pressure point / level

Wind effect
Stack effect

Stack effect P = Gravity g * ( Height from NPP h * Total Pressure Patm / Gas Constant for Air Ra ) * ((1 / Toutside) - (1 / Tinside))

### Module 8

### Module 9

Cost of Air infiltration W/m^2

**Psychrometric Chart**
https://www.psych-chart.com/

**Latent heat loss**: H2O
Q.l (W)= Volume flow rate V. (m^3) * Air Density p (kgda/m^3) * Enthalpy | Latent heat of vaporization h.fg (kJ/kgwv) * Moisture Content Change (Win - Wout) ()

**Sensible heat loss**: 70% N2, 20% O2, 1% Ar, CO2
Q.s (W)= Volume flow rate V. (m^3) * Air Density p (kgda/m^3) * Heat Capacity Cpair (kJ/kgC) * Temperature Change (Tin - Tout) (C)

**V.** (m^3/h) = Building Volume V (m^3) * Air change per hour ACH (ACH50Pa)

0.15 ACH4Pa
w = 0.0004 kgwv/kgda
Cpair = 1.005 kJ/kgC
h.fg = 2465 kJ/kgwv
p = 1.2 kgda/m^3
1 W = 1 J/s = 3.6 kJ/h

Qinf (infiltration)  = Ql + Qs
W / m^2 (GFA)

Studio project:
Estimate NSWE window to wall ratio,
Over all volume,
Surface area,


### Module 10

##### Wall assembly 11 aspects:
- Strong
- Durable
- Control
	- Fire
	- Heat flow
	- Liquid water
	- Water vapor
	- Air flow
	- Solar radiation
	- Noise / sound
- Economical
- Beauty / Aesthetics

Q = (A * Tdelta) / R = U (W / m^2 C) * A * Tdelta = (U * A * Tdelta) _Areas_ + (Psy (W / m C) * L * Tdelta) _Linear_ = U * A * HDD _Heating Seasons C18_ [[index#Heating Degree Days (HDD)|Heating Degree Days (HDD)]] = U * A * CDD _Cooling Seasons C18_ _W-days * 1 kW/1000W * 24Hours/1Day = kWh_

Air: Dry + Moist [[index#Module 9|Module 9]]
ACH _Airtightness_
Q Latent & Sensible [[index#Module 9|Module 9]]

**Passive House** design to / meet in simulation package before permit given:
OR{
	AND{
		**TEDI** Thermal Energy Demand Intensity: 15 kWh/m^2a _per annual_
		Energy Use Intensity: 60 kWh/m^2a
	}
	Peak Heating / Cooling: 10 W/m^2
}

### Module 11

### Module 12


## Projects

### [[Projects/2024/Building Science 2 - Project 1/Building Science 2 - Project 1|Project 1]]

### [[Projects/Building Science 2 - Project 2|Project 2]]

### [[Projects/Building Science 2 - Project 3|Project 3]]

### [[Projects/Building Science 2 - Project 4|Project 4]]
