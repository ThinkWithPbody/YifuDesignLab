---
tags:
  - project
status: DONE
share: true
hidden: true
---
## SPT Install and Update

1. Use BsgLauncher.exe to install or update official EFT to your best SSD
2. Download SPT AKI automated installer [here](https://sp-tarkov.com/#download)
3. Install SPT files in a separate folder affixed with version number
4. Install this [SPT Modlist](index.md#spt-modlist)
%%	- When updating to minor versions without making changes to the modlist, just copy over the old files to the new location.
		- Game Settings: "/user/sptSettings"
		- Launcher settings: "/user/launcher"
		- Mods: "/user/mods" & "/BepInEx/plugins"
			**Never delete or replace "/BepInEx/plugins/spt".**
		- Mod Settings: "/BepInEx/config"
		- Save Profiles (only if you run a server): "/user/profiles"%%
%%![|500](https://live.staticflickr.com/65535/53696801218_db324e3ae4_o.jpg)%%

## SPT Mods Install and Update

The modlist is compatible with **Mod Organizer** for profile management, meaning more than one instance of the game can be stored without taking excessive disk space, but it is not mandatory. 

### Mod Organizer 2
1. Download and install [MO2](https://github.com/ModOrganizer2/modorganizer/releases).
	- Download and install [SPT ModOrganizer Integration](https://hub.sp-tarkov.com/files/file/1314-spt-modorganizer-integration/#overview) by extracting it to the MO install location.
2. Create a new global instance in your SPT folder. Settings can be kept default, ignore pop-ups.
	- Under SPT root, edit `sptvfsbridge.bat` and add `REM ` at the start of line 9 and 12 so that it reads for example `REM start "" "%server_path%"`, then save the file. This is so that only the client will run, and instantly.
3. [Download](index.md#patch-note-and-downloads) a **package** or **patch** and extract files to the MO instance location under `MO\<InstanceName>\`, then refresh MO.
	![2024-06-04T22_27_17-05_00_TWP-X570-WIN10(Obsidian)](./Attachments/Escape%20From%20Tarkov/2024-06-04T22_27_17-05_00_TWP-X570-WIN10(Obsidian).jpg)
	- **Packages** are named `SPT Salt <SPTVersion>_<Package>`. They contain all mods of a major version.
	- **Patches** are named `SPT Salt <SPTVersion>_<Package>.<Patch>`. They are smaller and incomplete, meant to distribute mod updates quickly.
	- The **PersistentFiles** mod is how default configs are distributed and is a placeholder for your SPT settings and profile. Simply copy the files in this mod from `MO\<InstanceName>\mods\PersistentFiles-*\` as well as any extra files you want to keep from `MO\<InstanceName>\overwrite\` into an archive, then install it in MO as a mod set to a high priority to keep files across updates.
4. **Profiles** are the fastest way to switch between mod lists, but they only work if you've already imported all mods they reference. Select the profile for the current package or patch.
5. Click `Run` to launch SPT.
	- Don't forget to change SPT Launcher settings on Game Path and URL.

![Pasted image 20240520011534](./Attachments/Escape%20From%20Tarkov/Pasted%20image%2020240520011534.png)

## Project Fika (MPT)

To join my Fika server, run Aki.Launcher.exe and in "Settings", change URL to `http://173.32.64.239:6969`.
To join local server, change URL back to `http://127.0.0.1:6969`.

> [!tip]
> If you want to use your own profile on our server or download the one in use on our server for your local server, contact me.

## Modlist

Manual install locations are marked with 🍌 for **"/BepInEx/plugins"** and 🥒 for **"/user/mods"**.

#### Tools
[Server Value Modifier](https://hub.sp-tarkov.com/files/file/379-server-value-modifier-svm/#tab_d24083dde670a53728f69fa322aa580ec032191a) 🥒 (Server settings)
[Profile Editor](https://hub.sp-tarkov.com/files/file/184-spt-aki-profile-editor/) (Read installation, player health, quest, and items) 

#### Bots
[SWAG + DONUTS](https://hub.sp-tarkov.com/files/file/878-swag-donuts-dynamic-spawn-waves-and-custom-spawn-points/) 🍌🥒
[SAIN](https://hub.sp-tarkov.com/files/file/1062-sain-2-0-solarint-s-ai-modifications-full-ai-combat-system-replacement/) 🍌🥒
[Big Brain](https://hub.sp-tarkov.com/files/file/1219-bigbrain/#overview) 🍌
[Way Points](https://hub.sp-tarkov.com/files/file/1119-waypoints-expanded-navmesh/) 🍌
[That's Lit](https://hub.sp-tarkov.com/files/file/1453-that-s-lit/) 🍌 (With That's Lit Sync)
[Looting Bots](https://hub.sp-tarkov.com/files/file/1096-looting-bots/) 🍌
[Questing Bots](https://hub.sp-tarkov.com/files/file/1534-questing-bots/#overview) 🍌🥒

#### Gameplay
[Project Fika](https://discord.gg/project-fika) ([Documentation](https://github.com/project-fika/fika-documentation)) 🍌🥒
[Realism Mod](https://hub.sp-tarkov.com/files/file/606-spt-realism-mod/) 🍌🥒 (Everything overhauled)
[Late to the Party](https://hub.sp-tarkov.com/files/file/1099-late-to-the-party/) 🍌🥒 (Realistic Scav runs)
[Backdoor Bandit](https://hub.sp-tarkov.com/files/file/1154-backdoor-bandit-bb/#overview) 🍌🥒 (Shoot open doors)
[Josh Mate's Better Backpacks](https://hub.sp-tarkov.com/files/file/772-josh-mate-s-better-backpacks/#overview) 🥒 (Backpack rebalance)
[Shiny Airdrop Guns!](https://hub.sp-tarkov.com/files/file/1572-shiny-airdrop-guns/) 🥒 (Some guns have innate stats)
[Quick Throw Grenades](https://hub.sp-tarkov.com/files/file/1695-quick-throw-grenades/?highlight=grenade#overview) 🍌
[Use Items Anywhere](https://hub.sp-tarkov.com/files/file/1416-use-items-anywhere/) 🍌 (Hotkey backpack items)
[Boss Notifier](https://hub.sp-tarkov.com/files/file/1737-boss-notifier/#overview) 🍌 (Inter center level 1-3 unlocks)
[Live Flea Prices](https://hub.sp-tarkov.com/files/file/1561-live-flea-prices/) 🥒 (Fetch flea prices from live server)

#### QOL
[Dynamic Maps](https://hub.sp-tarkov.com/files/file/1981-dynamic-maps/) 🍌
[Shoulder Swap On Lean](https://discord.com/channels/1202292159366037545/1222463708534407210) 🍌
[Vocal Player](https://discord.com/channels/1202292159366037545/1230117857610698772) 🍌 (Announces actions)
[Expanded Task List](https://hub.sp-tarkov.com/files/file/1415-expanded-task-text-ett/) 🥒 (Detailed task list)
[Loot Value](https://hub.sp-tarkov.com/files/file/1606-lootvalue/) 🍌🥒 (Alt Shift M1 to quick sell)
[Item Info](https://hub.sp-tarkov.com/files/file/985-item-info/) 🥒 (Rarity recolor and detailed description)
[More Checkmarks](https://hub.sp-tarkov.com/files/file/1159-morecheckmarks/) 🍌🥒 (Show requirement for quests, hideout, crafting)
[Stash Search](https://hub.sp-tarkov.com/files/file/1769-stash-search/)) 🍌 (Ctrl F in stash)
[AutoDeposit](https://hub.sp-tarkov.com/files/file/2027-autodeposit/) 🍌
[UI Fixes](https://hub.sp-tarkov.com/files/file/1860-ui-fixes/) 🍌 (Drag to swap, UI QOL changes)
[Skipper](https://hub.sp-tarkov.com/files/file/1861-skipper/) 🍌 (Ctrl to skip quests)

#### Visual
[FOV and Optics Fix](https://hub.sp-tarkov.com/files/file/942-fontaine-s-fov-fix-variable-optics/) 🍌🥒 (M4/5 to zoom in/out)
[Realistic NVG](https://hub.sp-tarkov.com/files/file/1303-borkel-s-realistic-night-vision-goggles-nvgs-and-t-7/) 🍌🥒
[Realistic Thermal](https://hub.sp-tarkov.com/files/file/1510-borkel-s-big-realistic-thermal-package-bring-real-life-realism-to-your-thermal-s/) 🥒
[Visceral Dismemberment](https://discord.com/channels/1202292159366037545/1236748474653872228) 🍌
[Amands's Graphics](https://hub.sp-tarkov.com/files/file/813-amands-s-graphics/) 🍌 (Less fog, color grading)
[Custom Music Player](https://hub.sp-tarkov.com/files/file/1832-stalker-music-pack/#overview) 🥒 (Distributed with tracks)

#### Disabled Mods
[Amands's Sense](https://hub.sp-tarkov.com/files/file/1361-amands-sense/#overview) 🍌 (Optional loot helper)
[Visceral Bodies](https://discord.com/channels/1202292159366037545/1228199049996402791) (Bodies glitch)
[Web Map](https://hub.sp-tarkov.com/files/file/1421-techhappy-s-web-minimap/#overview) 🍌 (Replaced by Dynamic Maps)
[Expanded Door Interactions](https://hub.sp-tarkov.com/files/file/1865-expanded-door-interactions/) 🍌 (Annoying UI)
[Declutterer](https://hub.sp-tarkov.com/files/file/1785-de-clutterer-updated-by-cj/) 🍌 (Optional performance mod)
[No Grenade ESP](https://hub.sp-tarkov.com/files/file/1029-no-grenade-esp/) 🍌 (Incompatible with SAIN)
[Pause](https://hub.sp-tarkov.com/files/file/1793-pause-reupload/) 🍌 (P to pause, may cause death)
[Headshot Damage Redirection](https://hub.sp-tarkov.com/files/file/1809-headshot-damage-redirection-hdr/) 🍌 (We don't need that)

#### Default Hotkeys
- C to mount weapon
	- Ctrl + M4 to dial optic in
	- Ctrl + M5 to dial optic out
- G to quick throw grenades
- Ctrl to look around
	- Ctrl + Scroll to cycle High-ready Low-ready stance
	- M5 to Active Aim stance
	- M4 to Short-stock stance
	- J to Patrol stance
- V to quick melee
	- Double V to use melee weapon
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

### Patch Note & Downloads

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
