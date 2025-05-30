---
share: true
hidden: true
tags:
  - project
status: DONE
---

## SPT Install and Update

1. Use BsgLauncher.exe to install or update official EFT to your best SSD, use matching server version.
2. Download SPT AKI automated installer [here](https://sp-tarkov.com/#download).
3. Move SPT installer to a separate empty folder on your best SSD, affixed with the SPT version number (e.g. `Game/EFT/SPT 3.11.3/`), then run the SPT automatic install executable.
%%	- When updating to minor versions without making changes to the modlist, just copy over the old files to the new location.
		- Game Settings: "/user/sptSettings"
		- Launcher settings: "/user/launcher"
		- Mods: "/user/mods" & "/BepInEx/plugins"
			**Never delete or replace "/BepInEx/plugins/spt".**
		- Mod Settings: "/BepInEx/config"
		- Save Profiles (only if you run a server): "/user/profiles"%%

The mod list is compatible with **Mod Organizer** for profile management, meaning more than one instance of the game can be stored without taking excessive disk space. It is the easiest way to stay up to date, but it is not mandatory.

### Mod Organizer 2

1. Download and install [MO2](https://github.com/ModOrganizer2/modorganizer/releases).
2. Download and install [SPT ModOrganizer Integration](https://hub.sp-tarkov.com/files/file/1314-spt-modorganizer-integration/#overview) by extracting the `plugins` folder to the `<MO Install Directory>`.
3. Create a new **MO Global Instance** directed to the `<SPT Install Directory>` (e.g. `Game/EFT/SPT 3.11.3/`). Settings can be kept default, ignore pop-ups.
4. [[index#Patch Note & Downloads|Download]] a package or patch and **extract** files to the **MO Global Instance** directory under `%appdata%\Local\ModOrganizer\<InstanceName>\`, then refresh MO.
	![[./Escape From Tarkov_image-2.png|/Projects/2024/Escape From Tarkov/Escape From Tarkov_image-2.png]]
	- **Packages** are named `SPT <SPTVersion>_<Package>`. They contain all mods of a major version.
	- **Patches** are named `SPT <SPTVersion>_<Package>.<Patch>`. They are smaller and incomplete, meant to be installed sequentially after packages to distribute mod and config updates quickly.
5. **Select** the MO profile for the current patch (or package if no patch has been distributed yet).
	- **Profiles** are the fastest way to switch between mod lists, but they only work if you've already imported all mods they reference first.
	- The **PersistentFiles** mod is how default configs are distributed and also functions as an archive for your SPT settings and profile when you start playing. **Always load PersistentFiles with a Priority of 0.** Be ware of SPT profile incompatibilities between major version updates.

## Project Fika (MPT)

#### To Join Our Modded Fika Server

- Add an executable for **just the client** to MO.
	- Open the **Modify Executables** screen using **Ctrl + E** or use Tools > Executables.
	- **Add executable from file** for `<SPT Install Directory>\SPT.Launcher.exe` and give it a memorable name (e.g. "Launch Client"), then click OK.
		- ![[./Escape From Tarkov_image.png|/Projects/2024/Escape From Tarkov/Escape From Tarkov_image.png]]
- Select the **Launch Client** option from MO and click **Run**.
	- Do not simply run `SPT.Launcher.exe` (unless you installed mods normally without MO).
	- Optionally, add it as a shortcut.
		- ![[./Escape From Tarkov_image-1.png|/Projects/2024/Escape From Tarkov/Escape From Tarkov_image-1.png]]
- In **Launcher Settings**, change URL to `https://173.32.64.239:6969`.
	- You are encouraged to start the game with an Unheard profile.

#### To Start and Join a Modded Local Server

- Select the **Launch SP Tarkov** option from MO and click **Run**.
	- Do not simply run `SPT.Server.exe` or `SPT.Launcher.exe` (unless you installed mods normally without MO).
	- Optionally, set affinity for the client and server by modifying `sptvfsbridge.bat` - see example file below.
- In **Launcher Settings**, change URL back to `https://127.0.0.1:6969`.

`sptvfsbridge.bat`

```bash
@echo off
setlocal

set "launcher_path=SPT.Launcher.exe"
set "server_path=SPT.Server.exe"

REM Launch the server.exe
start "" /affinity F "%server_path%"

REM Wait for a moment to ensure the server.exe has started
timeout /t 25 /nobreak >nul

REM Launch the launcher.exe
start "" /affinity F0 "%launcher_path%"

endlocal
```

> [!tip]
> If you want to use your own profile on our server or download the one in use on our server for your local server, contact me.

### Default Hotkeys

- Z: Prone
- X: Crouch
	- Q: Toggle Lean Left
	- E: Toggle Lean Right
	- LA + X: Shoulder Transition
	- LA + W: Blind Fire Overhead
	- LA + S: Blind Fire Right Side
	- LA + A: Sidestep Left
	- LA + D: Sidestep Right
- C: Mount Weapon%%
	- Ctrl + M4 to dial optic in
	- Ctrl + M5 to dial optic out%%
- Scroll: Stance
	- C + Scroll: Walk Speed
	- CC: Walk
- V: Melee Weapon
	- VV: Quick Melee
- R: Reload
	- RR: Quick Reload
	- LC + R: Check Magazine
	- LC + LS + R: Inspect Weapon
	- LC + LS + R Continuous: Check Chamber / Fix Malfunction
	- LA + R: Detach Magazine
	- LA + LC + R: Unload Chamber
- T: Ping
	- Y: Quick Phrase
		- YY: Phrase Menu
	- F1: Mumble
		- F2: Command Follow Me (ask a member of faction or squad to follow)
		- F3: Command Cover Me (regroup, follow closely, cover me)
		- F4: Command On Your Own (initial tactic and patrol)
		- F5: Command Go Forward (push)
		- F6: Command Hold Position (hold)
		- F7: Command Stop (stop)
		- F8: Command Attention (reset target)
- L: Bipod
	- LC + L: Fold / Unfold Stock
- G: Discard Item
	- LS + G: Prepare Grenades
- O: Check Time
	- OO: Check Exits and Bosses
	- I: Task List
- M: Map
	- +/-: Map Zoom
	- LC + M: Minimap
	- Num8/Num5: Minimap Zoom
- Insert: Amands's Graphics Menu
- Home: Reshade Menu
- End: Fix "Hands are busy"
- KeypadPlus: Freecam
	- KeypadEnter: Teleport to Freecam
	- KeypadPeriod: Freecam Controls
	- KeypadMultiply: Freecam UI
- RC: Fika Chat
- M0: Fire
	- F: Interact
	- FF: Sense
- M1: Scope
	- LC + M2: Switch Scope
	- LS + M2: Change Scope Magnification
	- LA + Scroll: Scope Zoom In / Out
	- LA: Hold Breath
	- PgUp: Scope Elevation Up
	- PgDn: Scope Elevation Down
- M2: Toggle Tactical Device
	- LC + M3: Tactical Device Mode
	- B + M3: Tactical Device Activation Mode
	- N: Toggle Head Equipment
	- H: Toggle Head Tactical Device
		- LC + H: Head Tactical Device Mode
- M3: Free Look%%
	- Ctrl + Scroll: Cycle High-ready Low-ready stance
	- M5 to Active Aim stance
	- M4 to Short-stock stance
	- J to Patrol stance%%
- M4: Zoom
- F5: Revive
- F8: Extract
	- M1/M2: Jump to player
	- Space + M1: Snap to head
	- LC + M1: Snap to back
- F9: Pause
- F12: BepInEx Menu
- M2: Gift item from stash to other accounts
	- Alt Shift M1: Automatically sell item from stash to most profitable market

### Modlist

For downloads, head down to [[index#Patch Note & Downloads|Download]]
For key mapping, see [[index#Default Hotkeys|Default Hotkeys]]

Manual install locations are marked with 🍌 for **"/BepInEx/plugins"** and 🥒 for **"/user/mods"**.

#### Tools

[Server Value Modifier](https://hub.sp-tarkov.com/files/file/379-server-value-modifier-svm/#tab_d24083dde670a53728f69fa322aa580ec032191a) 🥒 (Server settings)
[Profile Editor](https://hub.sp-tarkov.com/files/file/184-spt-aki-profile-editor/) (Read installation, player health, quest, and items)
[Tarkin Item Exporter](https://hub.sp-tarkov.com/files/file/2724-tarkin-item-exporter/)

#### Bots

[MOAR + Bagels](https://hub.sp-tarkov.com/files/file/1059-moar-bagels-ultra-lite-spawn-mod/?highlight=MOAR) 🍌🥒
[Looting Bots](https://hub.sp-tarkov.com/files/file/1096-looting-bots/) 🍌
[Big Brain](https://hub.sp-tarkov.com/files/file/1219-bigbrain/#overview) 🍌
[Way Points](https://hub.sp-tarkov.com/files/file/1119-waypoints-expanded-navmesh/) 🍌
[No Bush](https://hub.sp-tarkov.com/files/file/2811-no-bush-updated-for-3-11/) 🍌
#### Gameplay

[Project Fika](https://discord.gg/project-fika) ([Documentation](https://project-fika.gitbook.io/wiki)) 🍌🥒
[Geko's Better Progression](https://hub.sp-tarkov.com/files/file/2773-geko-s-better-progression/) 🍌🥒 (Play-to-win)
[Health Per Level](https://hub.sp-tarkov.com/files/file/2327-health-per-level/) 🥒 (Health growth)
[Revival Mod](https://hub.sp-tarkov.com/files/file/2725-revivalmod-second-chance-survival-system-for-single-player-tarkov/?highlight=revival) 🍌🥒 (Bring Portable Defibrillator)
[Continuous Healing](https://hub.sp-tarkov.com/files/file/2546-continuous-healing/) 🍌
[Continuous Load Ammo](https://hub.sp-tarkov.com/files/file/2798-continuous-load-ammo/) 🍌
[Friendly PMC](https://hub.sp-tarkov.com/files/file/989-friendly-pmc/) 🍌🥒 (Command AIs including Knight)
[Virtual's Custom Quest Loader](https://hub.sp-tarkov.com/files/file/885-virtual-s-custom-quest-loader/) 🍌🥒
[Tarkov Weather System](https://hub.sp-tarkov.com/files/file/2796-tarkov-weather-system/) 🥒
[Late to the Party](https://hub.sp-tarkov.com/files/file/1099-late-to-the-party/) 🍌🥒 (Realistic Scav runs)
[Backdoor Bandit](https://hub.sp-tarkov.com/files/file/2575-backdoor-bandit-bb-updated/) 🍌🥒 (Breach doors)
[Shiny Airdrop Guns!](https://hub.sp-tarkov.com/files/file/1572-shiny-airdrop-guns/) 🥒 (Some airdrop guns have innate stats)
[Josh Mate's Better Backpacks](https://hub.sp-tarkov.com/files/file/2764-josh-mate-s-better-backpacks-ported-to-3-11/) 🥒
[WTT - Pack 'n' Strap](https://hub.sp-tarkov.com/files/file/1790-wtt-pack-n-strap/#tab_f222634d79eef27cc61efe96df69a224f7c465b8) 🍌🥒 (Belts and packs)
[Boss Notifier](https://hub.sp-tarkov.com/files/file/1737-boss-notifier/#overview) 🍌 (Inter center level 1-3 unlocks)
[Bosses Have Lega Medals](https://hub.sp-tarkov.com/files/file/2109-bosses-have-lega-medals/) 🥒
[Live Flea Prices](https://hub.sp-tarkov.com/files/file/1561-live-flea-prices/) 🥒 (Fetch flea prices from live server)

#### QOL

[Dynamic Maps](https://hub.sp-tarkov.com/files/file/1981-dynamic-maps/) 🍌
[PAUSE](https://hub.sp-tarkov.com/files/file/2729-pause/#overview) 🍌
[UI Fixes](https://hub.sp-tarkov.com/files/file/1860-ui-fixes/) 🍌 (Drag to swap, UI QOL changes)
[Loot Value](https://hub.sp-tarkov.com/files/file/1606-lootvalue/) 🍌🥒 (Alt Shift M0 to quick sell)
[QuickSell](https://hub.sp-tarkov.com/files/file/2318-quicksell/) 🍌 (N/M to sell to Flea/Traders)
[More Checkmarks](https://hub.sp-tarkov.com/files/file/1159-morecheckmarks/) 🍌🥒 (Show requirement for quests, hideout, crafting)
[All Quests Checkmarks](https://hub.sp-tarkov.com/files/file/2705-all-quests-checkmarks/#overview) 🍌🥒 (Better checkmarks for quests, compatible with More Checkmarks via config)
[Quest Tracker](https://hub.sp-tarkov.com/files/file/1574-quest-tracker/) 🍌 (M1 to track quests)
[Skipper](https://hub.sp-tarkov.com/files/file/1861-skipper/) 🍌 (LC to skip quests)
[Expanded Task Text](https://hub.sp-tarkov.com/files/file/2853-expanded-task-text-ett/?highlight=expanded) 🥒
[Ammo Stats in Description](https://hub.sp-tarkov.com/files/file/284-ammo-stats-in-description/) 🥒 (Colorful ammo)
[Modding Stats Helper](https://hub.sp-tarkov.com/files/file/1814-modding-stats-helper-by-wara/#overview) 🍌 (Show relative stats)
[Trader Modding And Improved Weapon Building](https://hub.sp-tarkov.com/files/file/1795-trader-modding-and-improved-weapon-building/) 🍌🥒 (Filters & show Flea Prices)
[AutoDeposit](https://hub.sp-tarkov.com/files/file/2027-autodeposit/) 🍌
[Stash Search](https://hub.sp-tarkov.com/files/file/1769-stash-search/) 🍌 (LC + F to search in stash, LC + C to clear)
[Stash Management Helper](https://hub.sp-tarkov.com/files/file/2514-stash-management-helper/) 🍌
[HandsAreNotBusy](https://hub.sp-tarkov.com/files/file/1810-handsarenotbusy/?highlight=hands) 🍌 （Press End to stop hand busy bug)
[Simple Workout](https://hub.sp-tarkov.com/files/file/1989-simple-workout-qte/#overview) 🥒 (SPT balanced fatigue)

#### Visual

[Vocal Player](https://discord.com/channels/1202292159366037545/1230117857610698772) 🍌 (Announces actions)
[Film Look for Tarkov (ReShade Preset)](https://hub.sp-tarkov.com/files/file/1013-film-look-for-tarkov-reshade-preset/) 🍌🥒
[Amands's Graphics](https://hub.sp-tarkov.com/files/file/813-amands-s-graphics/) 🍌 (Less fog, color grading)
[Amands' Sense](https://hub.sp-tarkov.com/files/file/1361-amands-sense/?highlight=amands#overview) 🍌 (Optional loot helper)
[FOV and Optics Fix](https://hub.sp-tarkov.com/files/file/942-fontaine-s-fov-fix-variable-optics/) 🍌 (M4/5 to zoom in/out)
[HollywoodFX](https://hub.sp-tarkov.com/files/file/2683-hollywoodfx/#overview) 🍌 (Bullet impacts)
[Realistic Thermal Scopes](https://hub.sp-tarkov.com/files/file/2739-realistic-thermal-scopes/) 🥒
[Realistic NVG](https://hub.sp-tarkov.com/files/file/1303-borkel-s-realistic-night-vision-goggles-nvgs-and-t-7/) 🍌🥒%%[Loot Highlighter](https://hub.sp-tarkov.com/files/file/2835-loot-highlighter/) 🍌 (Disabled by default)%%
[Simple Crosshair](https://hub.sp-tarkov.com/files/file/1920-simple-crosshair/) 🍌
[Player Encumbrance Bar](https://hub.sp-tarkov.com/files/file/1898-player-encumbrance-bar/) 🍌
[StatTrack](https://hub.sp-tarkov.com/files/file/2501-stattrack/) 🍌🥒
[Freecam](https://hub.sp-tarkov.com/files/file/279-freecam/?highlight=free#overview) 🍌 (F10 to Freecam)
[Hideout Cat](https://hub.sp-tarkov.com/files/file/2720-hideout-cat/#overview) 🍌 (Cat)

#### Archive

##### Outdated Mods

[SWAG + DONUTS](https://hub.sp-tarkov.com/files/file/878-swag-donuts-dynamic-spawn-waves-and-custom-spawn-points/) 🍌🥒
[SAIN](https://hub.sp-tarkov.com/files/file/1062-sain-2-0-solarint-s-ai-modifications-full-ai-combat-system-replacement/) 🍌🥒
[That's Lit](https://hub.sp-tarkov.com/files/file/1453-that-s-lit/) 🍌 (With That's Lit Sync)
[Questing Bots](https://hub.sp-tarkov.com/files/file/1534-questing-bots/#overview) 🍌🥒

[Realism Mod](https://hub.sp-tarkov.com/files/file/606-spt-realism-mod/) 🍌🥒 (Everything overhauled)
[Quick Throw Grenades](https://hub.sp-tarkov.com/files/file/1695-quick-throw-grenades/?highlight=grenade#overview) 🍌
[Shoulder Swap On Lean](https://discord.com/channels/1202292159366037545/1222463708534407210) 🍌
[Item Info](https://hub.sp-tarkov.com/files/file/985-item-info/) 🥒 (Rarity recolor and detailed description)
[Visceral Combat](https://discord.com/channels/1202292159366037545/1236748474653872228) 🍌
[Custom Music Player](https://hub.sp-tarkov.com/files/file/1832-stalker-music-pack/#overview) 🥒 (Distributed with tracks)

##### Disabled Mods

[Acid's Bot Placement System](https://hub.sp-tarkov.com/files/file/2782-abps-acid-s-bot-placement-system/#comments) 🍌🥒
[Web Map](https://hub.sp-tarkov.com/files/file/1421-techhappy-s-web-minimap/#overview) 🍌 (Replaced by Dynamic Maps)
[Expanded Door Interactions](https://hub.sp-tarkov.com/files/file/1865-expanded-door-interactions/) 🍌 (Annoying UI)
[Use Items Anywhere](https://hub.sp-tarkov.com/files/file/1416-use-items-anywhere/) 🍌 (Hotkey backpack items)
[Realistic Thermal](https://hub.sp-tarkov.com/files/file/1510-borkel-s-big-realistic-thermal-package-bring-real-life-realism-to-your-thermal-s/) 🥒
[Headshot Damage Redirection](https://hub.sp-tarkov.com/files/file/1809-headshot-damage-redirection-hdr/) 🍌 (We don't need that)
[Random Season](https://hub.sp-tarkov.com/files/file/2610-random-season-ripoff/) 🥒 (Replaced by Tarkov Weather System)

###### Outdated

[Declutterer](https://hub.sp-tarkov.com/files/file/1785-de-clutterer-updated-by-cj/) 🍌 (Optional performance mod)
[No Grenade ESP](https://hub.sp-tarkov.com/files/file/1029-no-grenade-esp/) 🍌 (Incompatible with SAIN)

### Patch Note & Downloads

##### 3.11.3_1.2

Removed Random Season
Removed Acid's Bot Placement System
Added MOAR + Bagels
Added HandsAreNotBusy
Added Continuous Load Ammo
Added No Bush
Added Expanded Task Text
Added Tarkov Weather System

##### 3.11.3_1.1

[Patch Download](http://www.mediafire.com/view/7pp7gg7vsivec2s)
Added Stash Search
Added Trader Modding And Improved Weapon Building
Added FOV-Fix-port-3.11
Added Amands' Sense
Added Realistic Thermal Scopes
Added Stash Management Helper
Added StatTrack
Added Player Encumbrance Bar
Added Random Season
Added Simple Workout
Added Continuous Healing
Added Film Look for Tarkov (ReShade Preset)
Added Bosses Have Lega Medals
Added Acid's Bot Placement System
Added Freecam

##### 3.11.3_1.0

[Package Download](http://www.mediafire.com/view/5cgy25rp1h811x9)
Bump bump bump SPT version to 3.11.3

##### 3.8.3_2.2

Removed Headshot Damage Redirection

##### 3.8.3_2.1

[Patch Download](http://www.mediafire.com/view/bnpu2afxpbot90l)

**Mods and MO Profiles are distributed together.**
Added Realism Mod
Added AutoDeposit
Added Quick Throw Grenade
Updated Looting Bots
Updated Borkel's Realistic Night Vision Goggles
Updated Late to the Party
Updated Fontaine's FOV Fix & Variable Optics
Updated Dynamic Maps
Updated That's Lit
Updated That's Lit Sync
Updated UI Fixes
Updated Stash Search

##### 3.8.3_2

[Package](http://www.mediafire.com/view/msx1i8v7aqdoxwk)
[Profile](http://www.mediafire.com/view/7i0apd7w7ax9rm1)

**All mod files turned MO2 compatible and distributed separately.** This means that MO2 is not mandatory and merely makes updating easier.

Added Dynamic Maps
Removed Web Map
Removed Expanded Door Interactions
Removed Declutterer
Removed No Grenade ESP
Removed Pause
Updated Fika

##### 3.8.3_1

[Package](http://www.mediafire.com/view/c87ornfb1ouw15p)

%%#### 3.8.1

###### Patch 2024-05-15 for 3.8.1_3>4

Added Custom Music Player
Updated Fika & DONUTS & Late to the Party Config
Updated SVM Preset

###### Patch 2024-05-10 for 3.8.1_2>3

Added Visceral Dismemberment
Added Vocal Player
Added Shoulder Swap On Lean
Updated Josh Mate's Better Backpacks
Updated Borkel's Realistic Night Vision Goggles
Updated Backdoor Bandit
Updated Server Value Modifier

###### Patch 2024-05-07 for 3.8.1_1>2

Updated Borkel's Realistic Night Vision Goggles
Updated Borkel's Big Realistic Thermal Package
Updated Config Files

###### Patch 2024-05-06 for 3.8.1_0>1

Added UI Fixes
Added Boss Notifier
Added Shiny Airdrop Guns!%%
