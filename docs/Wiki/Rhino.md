---
share: true
hidden: false
tags:
  - wiki
title: Rhino
---

### Keyboard

| Key     | Command Macro                                                                                             |
| ------- | --------------------------------------------------------------------------------------------------------- |
| F1      | ! _PointsOn                                                                                               |
| F2      | ! _PointsOff                                                                                              |
| F3      | '_DisableOsnap _Toggle                                                                                    |
| F4      | '_Snap                                                                                                    |
| F5      | ! _GumballAlignment _Cycle                                                                                |
| F6      | ! _Camera _Toggle                                                                                         |
| F7      | _noecho -_Grid _ShowGrid _ShowGridAxes _Enter  -_RunScript (Rhino.Print "Grid Display Toggled.")          |
| F8      | _noecho _PrintDisplay _State _On _Scale _echo _Pause _Enter -_RunScript (Rhino.Print "PrintDisplay Set.") |
| LC + F8 | _noecho _PrintDisplay _State  _Toggle _Enter -_RunScript (Rhino.Print "PrintDisplay Toggled.")            |
| F9      | ! _CommandHistory                                                                                         |
| F10     | ! _DocumentProperties                                                                                     |
| F11     | '_Help                                                                                                    |
| F12     | '_DigClick                                                                                                |
| LC + E  | ! _Extend _Enter                                                                                          |

### Aliases

| Alias | Command Macro          |
| ----- | ---------------------- |
| B2    | '_Boolean2Objects      |
| BC    | '_BlendCrv             |
| BD    | '_BooleanDifference    |
| BI    | '_BooleanIntersection  |
| BS    | '_BooleanSplit         |
| BU    | '_BooleanUnion         |
| CB    | ! \_CurveBoolean       |
| COi   | '_Copy _Inplace        |
| DD    | '_Distance             |
| DI    | '_DimAligned           |
| DM    | '_Mirror               |
| EC    | '_ExtrudeCrv           |
| ES    | '_ExtrudeSrf           |
| FL    | '_Fillet _Dynamic=Yes  |
| HP    | ! _HistoryPurge        |
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

[[../Projects/2024/Yifu Design Lab/Attachments/Yifu Design Lab/BatchExportSTLByObj.py|BatchExportSTLByObj.py]]

#### View

[[./Attachments/Rhino/FindAllHiddenClippingPlaneLayers.py|FindAllHiddenClippingPlaneLayers.py]]

#### Geo

[[./Attachments/Rhino/HatchFromCenterline.py|HatchFromCenterline.py]]

![[./Attachments/Rhino/HatchFromCenterline.gif|HatchFromCenterline]]

### Plugins

#### Package Manager

byRhinoGadget
Caribou
[Flexibility](https://www.food4rhino.com/en/app/flexibility)
[Metahopper](https://www.food4rhino.com/en/app/metahopper)
[Open Nest](https://www.food4rhino.com/en/app/opennest)
[SnappingGecko](https://www.food4rhino.com/en/app/snappinggecko)

#### [Food4Rhino](https://www.food4rhino.com/en)

Bifocals
[Bowerbird](https://www.food4rhino.com/en/app/bowerbird#downloads_list)
[Elefront](https://www.food4rhino.com/en/app/elefront)
human
[Kangaroo Physics](<https://www.food4rhino.com/en/app/kangaroo-physics>
[Ladybug Tools](https://www.food4rhino.com/en/app/ladybug-tools)
[Ngon](https://www.food4rhino.com/en/app/ngon)
[pOd](https://www.food4rhino.com/en/app/podghbutton)
[Pufferfish](https://www.food4rhino.com/en/app/pufferfish)
[Dendro](https://www.food4rhino.com/en/app/dendro#)

### Commands

`OptionsExport`
`_SaveWindowLayout`
`_ExportRuiFile`
