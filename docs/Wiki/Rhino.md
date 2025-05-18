---
tags:
  - wiki
title: Rhino
share: true
hide: false
---
### Keyboard

| Key | Command Macro                                                                                                                     |
| --- | --------------------------------------------------------------------------------------------------------------------------------- |
| F1  | ! _PointsOn                                                                                                                       |
| F2  | ! _PointsOff                                                                                                                      |
| F3  | '_DisableOsnap _Toggle                                                                                                            |
| F4  | '_Snap                                                                                                                            |
| F5  | ! _GumballAlignment _Cycle                                                                                                        |
| F6  | ! _Camera _Toggle                                                                                                                 |
| F7  | noecho -_Grid _ShowGrid _ShowGridAxes _Enter  -_RunScript (Rhino.Print "Grid Display Toggled.")                                   |
| F8  | noecho _PrintDisplay _State  _Toggle _Color _Display _Scale 10000 _Enter _Enter -_RunScript (Rhino.Print "PrintDisplay Toggled.") |
| F9  | ! _CommandHistory                                                                                                                 |
| F10 | ! _DocumentProperties                                                                                                             |
| F11 | '_Help                                                                                                                            |
| F12 | '_DigClick                                                                                                                        |


### Aliases

| Alias | Command Macro          |
| ----- | ---------------------- |
| B2    | '_Boolean2Objects      |
| BD    | '_BooleanDifference    |
| BI    | '_BooleanIntersection  |
| BS    | '_BooleanSplit         |
| BU    | '_BooleanUnion         |
| CB    | ! \_CurveBoolean       |
| COi   | '_Copy _Inplace        |
| DD    | '_Distance             |
| DI    | '_Dim                  |
| DM    | '_Mirror               |
| EC    | '_ExtrudeCrv           |
| ES    | '_ExtrudeSrf           |
| FL    | '_Fillet _Dynamic=Yes  |
| LI    | '_Polyline             |
| MV    | ! _Move _Vertical=Yes  |
| SC    | '_Scale                |
| S1    | '_Scale1D              |
| S2    | '_Scale2D              |
| TR    | '_Extend _Enter        |
| PP    | '_PushPull             |
| RO    | '_Rotate               |
| R3    | '_Rotate3D             |
| RB    | '_RebuildCrvNonUniform |


### Scripts

#### I/O
[[Configs/Files/BatchExportSTLByObj.py|BatchExportSTLByObj.py]]

#### View
[[../assets/img/FindAllHiddenClippingPlaneLayers.py|FindAllHiddenClippingPlaneLayers.py]]


#### Geo
[[../assets/img/HatchFromCenterline.py|HatchFromCenterline.py]]
![[../assets/img/HatchFromCenterline.gif|HatchFromCenterline]]

### Plugins
#### Package Manager:

Caribou
[Flexibility](https://www.food4rhino.com/en/app/flexibility)
[Metahopper](https://www.food4rhino.com/en/app/metahopper)
[Open Nest](https://www.food4rhino.com/en/app/opennest)
[SnappingGecko](https://www.food4rhino.com/en/app/snappinggecko)

#### [Food4Rhino](https://www.food4rhino.com/en):
Bifocals
[Bowerbird](https://www.food4rhino.com/en/app/bowerbird#downloads_list)
[Elefront](https://www.food4rhino.com/en/app/elefront)
human
[Kangaroo Physics](https://www.food4rhino.com/en/app/kangaroo-physics
[Ladybug Tools](https://www.food4rhino.com/en/app/ladybug-tools)
[Ngon](https://www.food4rhino.com/en/app/ngon)
[pOd](https://www.food4rhino.com/en/app/podghbutton)
[Pufferfish](https://www.food4rhino.com/en/app/pufferfish)


### Commands

`OptionsExport`
`_SaveWindowLayout`
`_ExportRuiFile`