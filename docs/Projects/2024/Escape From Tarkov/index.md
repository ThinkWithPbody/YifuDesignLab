---
share: true
hidden: true
tags:
  - project
status: DONE
---

## SPT Install and Update

1. Use BsgLauncher.exe to install or update official EFT matching server version to your best SSD
2. Download SPT AKI automated installer [here](https://sp-tarkov.com/#download)
3. Move SPT installer to a separate empty folder affixed with version number (e.g. `Game/EFT/SPT 3.11.3/`) and install SPT files
%%	- When updating to minor versions without making changes to the modlist, just copy over the old files to the new location.
		- Game Settings: "/user/sptSettings"
		- Launcher settings: "/user/launcher"
		- Mods: "/user/mods" & "/BepInEx/plugins"
			**Never delete or replace "/BepInEx/plugins/spt".**
		- Mod Settings: "/BepInEx/config"
		- Save Profiles (only if you run a server): "/user/profiles"%%
%%![|500](https://live.staticflickr.com/65535/53696801218_db324e3ae4_o.jpg)%%

### SPT Mods Install and Update

The mod list is compatible with **Mod Organizer** for profile management, meaning more than one instance of the game can be stored without taking excessive disk space. It is the easiest way to stay up to date, but it is not mandatory.

## Mod Organizer 2

1. Download and install [MO2](https://github.com/ModOrganizer2/modorganizer/releases).
	- Download and install [SPT ModOrganizer Integration](https://hub.sp-tarkov.com/files/file/1314-spt-modorganizer-integration/#overview) by extracting it to the MO install location (`%appdata%\Local\ModOrganizer\`).
2. Create a new global instance directed to the folder you just installed SPT in (e.g. `Game/EFT/SPT 3.11.3/`). Settings can be kept default, ignore pop-ups.
3. [[index#Patch Note & Downloads|Download]] a **package** or **patch** and extract files to the MO instance location under `%appdata%\Local\ModOrganizer\<InstanceName>\`, then refresh MO.
	![[./Attachments/Escape From Tarkov/2024-06-04T22_27_17-05_00_TWP-X570-WIN10(Obsidian).jpg|2024-06-04T22_27_17-05_00_TWP-X570-WIN10(Obsidian)]]
	- **Packages** are named `SPT <SPTVersion>_<Package>`. They contain all mods of a major version.
	- **Patches** are named `SPT <SPTVersion>_<Package>.<Patch>`. They are smaller and incomplete, meant to be installed sequentially after packages to distribute mod updates quickly.
	- The **PersistentFiles** mod is how default configs are distributed and also functions as an archihve for your SPT settings and profile as soon as you start playing. Simply copy the files in this mod from `MO\<InstanceName>\mods\PersistentFiles-*\` as well as any extra files you want to keep from `MO\<InstanceName>\overwrite\` into an archive, then install it in MO as a mod and set to a high priority to keep files across updates. Be ware of SPT profile incompatibilities between major version updates.
4. **Profiles** are the fastest way to switch between mod lists, but they only work if you've already imported all mods they reference first. Select the profile for the current patch (or package if no patch has been distributed yet).
5. Click `Run` to launch SPT.
	- Don't forget to change SPT Launcher settings on Game Path and URL.
	- Optionally, add the launch shortcut to your Desktop


## Project Fika (MPT)

To join my Fika server, run Aki.Launcher.exe and in "Settings", change URL to `http://173.32.64.239:6969`.
To join local server, change URL back to `http://127.0.0.1:6969`.

> [!tip]
> If you want to use your own profile on our server or download the one in use on our server for your local server, contact me.

## Modlist

For downloads, head down to [[index#Patch Note & Downloads|Download]]

Manual install locations are marked with 🍌 for **"/BepInEx/plugins"** and 🥒 for **"/user/mods"**.

#### Tools

[Server Value Modifier](https://hub.sp-tarkov.com/files/file/379-server-value-modifier-svm/#tab_d24083dde670a53728f69fa322aa580ec032191a) 🥒 (Server settings)
[Profile Editor](https://hub.sp-tarkov.com/files/file/184-spt-aki-profile-editor/) (Read installation, player health, quest, and items)
[Tarkin Item Exporter](https://hub.sp-tarkov.com/files/file/2724-tarkin-item-exporter/)

#### Bots

[Big Brain](https://hub.sp-tarkov.com/files/file/1219-bigbrain/#overview) 🍌
[Way Points](https://hub.sp-tarkov.com/files/file/1119-waypoints-expanded-navmesh/) 🍌
[Looting Bots](https://hub.sp-tarkov.com/files/file/1096-looting-bots/) 🍌

#### Gameplay

[Project Fika](https://discord.gg/project-fika) ([Documentation](https://project-fika.gitbook.io/wiki)) 🍌🥒
[Geko's Better Progression](https://hub.sp-tarkov.com/files/file/2773-geko-s-better-progression/) 🍌🥒 (Play-to-win)
[Health Per Level](https://hub.sp-tarkov.com/files/file/2327-health-per-level/) 🥒
[Revival Mod](https://hub.sp-tarkov.com/files/file/2725-revivalmod-second-chance-survival-system-for-single-player-tarkov/?highlight=revival) 🍌🥒
[Friendly PMC](https://hub.sp-tarkov.com/files/file/989-friendly-pmc/) 🍌🥒
[Virtual's Custom Quest Loader](https://hub.sp-tarkov.com/files/file/885-virtual-s-custom-quest-loader/) 🍌🥒
[Late to the Party](https://hub.sp-tarkov.com/files/file/1099-late-to-the-party/) 🍌🥒 (Realistic Scav runs)
[Backdoor Bandit](https://hub.sp-tarkov.com/files/file/2575-backdoor-bandit-bb-updated/) 🍌🥒
[Shiny Airdrop Guns!](https://hub.sp-tarkov.com/files/file/1572-shiny-airdrop-guns/) 🥒 (Some guns have innate stats)
[Josh Mate's Better Backpacks](https://hub.sp-tarkov.com/files/file/2764-josh-mate-s-better-backpacks-ported-to-3-11/) 🥒
[WTT - Pack 'n' Strap](https://hub.sp-tarkov.com/files/file/1790-wtt-pack-n-strap/#tab_f222634d79eef27cc61efe96df69a224f7c465b8) 🍌🥒 (Belts and packs)
[Boss Notifier](https://hub.sp-tarkov.com/files/file/1737-boss-notifier/#overview) 🍌 (Inter center level 1-3 unlocks)
[Live Flea Prices](https://hub.sp-tarkov.com/files/file/1561-live-flea-prices/) 🥒 (Fetch flea prices from live server)

#### QOL

[Dynamic Maps](https://hub.sp-tarkov.com/files/file/1981-dynamic-maps/) 🍌
[PAUSE](https://hub.sp-tarkov.com/files/file/2729-pause/#overview) 🍌
[Loot Value](https://hub.sp-tarkov.com/files/file/1606-lootvalue/) 🍌🥒 (Alt Shift M1 to quick sell)
[More Checkmarks](https://hub.sp-tarkov.com/files/file/1159-morecheckmarks/) 🍌🥒 (Show requirement for quests, hideout, crafting)
[All Quests Checkmarks](https://hub.sp-tarkov.com/files/file/2705-all-quests-checkmarks/#overview) 🍌🥒 (Better checkmarks for quests, compatible with More Checkmarks via config)
[Ammo Stats in Description](https://hub.sp-tarkov.com/files/file/284-ammo-stats-in-description/) 🥒 (Colorful ammo)
[Modding Stats Helper](https://hub.sp-tarkov.com/files/file/1814-modding-stats-helper-by-wara/#overview) 🍌
[AutoDeposit](https://hub.sp-tarkov.com/files/file/2027-autodeposit/) 🍌
[UI Fixes](https://hub.sp-tarkov.com/files/file/1860-ui-fixes/) 🍌 (Drag to swap, UI QOL changes)
[QuickSell](https://hub.sp-tarkov.com/files/file/2318-quicksell/) 🍌
[Quest Tracker](https://hub.sp-tarkov.com/files/file/1574-quest-tracker/) 🍌
[Skipper](https://hub.sp-tarkov.com/files/file/1861-skipper/) 🍌 (Ctrl to skip quests)

#### Visual

[Vocal Player](https://discord.com/channels/1202292159366037545/1230117857610698772) 🍌 (Announces actions)
[Amands's Graphics](https://hub.sp-tarkov.com/files/file/813-amands-s-graphics/) 🍌 (Less fog, color grading)
[HollywoodFX](https://hub.sp-tarkov.com/files/file/2683-hollywoodfx/#overview) 🍌 (Bullet impacts)
[Realistic NVG](https://hub.sp-tarkov.com/files/file/1303-borkel-s-realistic-night-vision-goggles-nvgs-and-t-7/) 🍌🥒
[Simple Crosshair](https://hub.sp-tarkov.com/files/file/1920-simple-crosshair/) 🍌
[Hideout Cat](https://hub.sp-tarkov.com/files/file/2720-hideout-cat/#overview) 🍌 (Cat)

#### Archive

##### Outdated Mods

[SWAG + DONUTS](https://hub.sp-tarkov.com/files/file/878-swag-donuts-dynamic-spawn-waves-and-custom-spawn-points/) 🍌🥒
[SAIN](https://hub.sp-tarkov.com/files/file/1062-sain-2-0-solarint-s-ai-modifications-full-ai-combat-system-replacement/) 🍌🥒
[That's Lit](https://hub.sp-tarkov.com/files/file/1453-that-s-lit/) 🍌 (With That's Lit Sync)
[Questing Bots](https://hub.sp-tarkov.com/files/file/1534-questing-bots/#overview) 🍌🥒

[Realism Mod](https://hub.sp-tarkov.com/files/file/606-spt-realism-mod/) 🍌🥒 (Everything overhauled)
[Quick Throw Grenades](https://hub.sp-tarkov.com/files/file/1695-quick-throw-grenades/?highlight=grenade#overview) 🍌
[Use Items Anywhere](https://hub.sp-tarkov.com/files/file/1416-use-items-anywhere/) 🍌 (Hotkey backpack items)
[Shoulder Swap On Lean](https://discord.com/channels/1202292159366037545/1222463708534407210) 🍌
[Expanded Task List](https://hub.sp-tarkov.com/files/file/1415-expanded-task-text-ett/) 🥒 (Detailed task list)
[Item Info](https://hub.sp-tarkov.com/files/file/985-item-info/) 🥒 (Rarity recolor and detailed description)
[Stash Search](https://hub.sp-tarkov.com/files/file/1769-stash-search/)) 🍌 (Ctrl F in stash)
[FOV and Optics Fix](https://hub.sp-tarkov.com/files/file/942-fontaine-s-fov-fix-variable-optics/) 🍌🥒 (M4/5 to zoom in/out)
[Realistic Thermal](https://hub.sp-tarkov.com/files/file/1510-borkel-s-big-realistic-thermal-package-bring-real-life-realism-to-your-thermal-s/) 🥒
[Visceral Combat](https://discord.com/channels/1202292159366037545/1236748474653872228) 🍌
[Custom Music Player](https://hub.sp-tarkov.com/files/file/1832-stalker-music-pack/#overview) 🥒 (Distributed with tracks)

##### Disabled Mods


###### Outdated

[Amands's Sense](https://hub.sp-tarkov.com/files/file/1361-amands-sense/#overview) 🍌 (Optional loot helper)
[Visceral Bodies](https://discord.com/channels/1202292159366037545/1228199049996402791) (Bodies glitch)
[Web Map](https://hub.sp-tarkov.com/files/file/1421-techhappy-s-web-minimap/#overview) 🍌 (Replaced by Dynamic Maps)
[Expanded Door Interactions](https://hub.sp-tarkov.com/files/file/1865-expanded-door-interactions/) 🍌 (Annoying UI)
[Declutterer](https://hub.sp-tarkov.com/files/file/1785-de-clutterer-updated-by-cj/) 🍌 (Optional performance mod)
[No Grenade ESP](https://hub.sp-tarkov.com/files/file/1029-no-grenade-esp/) 🍌 (Incompatible with SAIN)
[Pause](https://hub.sp-tarkov.com/files/file/1793-pause-reupload/) 🍌 (P to pause, may cause death)
[Headshot Damage Redirection](https://hub.sp-tarkov.com/files/file/1809-headshot-damage-redirection-hdr/) 🍌 (We don't need that)

## Default Hotkeys

- C to mount weapon
	- Ctrl + M4 to dial optic in
	- Ctrl + M5 to dial optic out
- G to prepare grenades
- Alt to look around
	- Ctrl + Scroll to cycle High-ready Low-ready stance
	- M5 to Active Aim stance
	- M4 to Short-stock stance
	- J to Patrol stance
- V to use melee weapon
	- Double V to quick melee
	- Hold V to hold melee weapon
- F12 to change Fika Core settings such as health bar, damage multiplier, and AI range
	- T to ping
	- F9 to enter free cam
		- M1/M2 to jump to player
		- Space while jumping to snap to head
		- Ctrl while jumping to snap to back
		- T to teleport to free cam
- M2 item in stash to gift to other accounts
- Alt Shift M1 item in stash to automatically sell to most profitable market
- O to check bosses
- F1 to Mumble
	- F2 to Command Follow Me (ask a member of faction or squad to follow)
	- F3 to Command Cover Me (regroup, follow closely, cover me)
	- F4 to Command On Your Own (initial tactic and patrol)
	- F5 to Command Go Forward (push)
	- F6 to Command Stop (stop)
	- F7 to Command Spread Out (find cover)
	- F8 to Command Attention (reset target)

## Patch Note & Downloads

##### 3.11.3_1.0

[Package Download](http://www.mediafire.com/view/lsnuhc29ii4gsig)
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
