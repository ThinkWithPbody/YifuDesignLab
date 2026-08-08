---
share: true
hidden: true
hide: []
tags:
  - project
title: mINeCraFT club Guide
status: DONE
priority: medium
due:
completion: 2024-06-10
---

![Logo|16](https://live.staticflickr.com/65535/52191413864_3b47958f71_o.png) Modpack Download: [mcc-1.21.1-neoforge-2.8](http://www.mediafire.com/view/ssi83v41i8p58t1)

# Install

## Curse Forge Install

1. Download Curse Forge Standalone [Here](https://www.curseforge.com/download/app).
2. Download the mINeCraFT club modpack above.
3. Install the modpack on Curse Forge.
	1. Go to Minecraft
	2. From the top right, Create Custom Profile
	3. Click the underlined word **import**
	4. Select the modpack
4. Click Play

## Curse Forge Update

### Backup:

- exposures/
- schematics/
- screenshots/
- xaero/
- xaeros-drawings/
- Distant_Horizons_server_data/

### Optional Backup:

- options.txt
- servers.dat
- XaeroWaypoints_BACKUP*/

# Default Hotkeys

## 1. Movement

LC = Sneak
LS = Sprint
Z = Crawl
H = Jetpack Engine
- Ctrl + H = Jetpack Hover Mode

## 2. Inventory

Tab = Inventory
Q = Offhand Swap
%%V = Hotbar Swap
- LS + V = Tetra Use Secondary%%
%%R = Tetra Toolbelt
- LC + R = Tetra Toolbelt Open
- LS + R = Tetra Toolbelt Restock%%
E = Sophisticated Backpack
- Mouse3 = Backpack Sort
- C = Backpack Upgrade Slot 1
T = Delete Item
	Most recently deleted items are stored in the Trash Slot UI
- LS + T = Delete All Items of Type
- , = Toggle Trash Slot UI
LC + LS + Mouse3 = Inventory Profiles GUI
- LS + Mouse1 Swipe = Move Items Between Containers
- Mouse3 = Inventory Sort
	- *Sort the inventory under cursor.*
- ; = Highlight Storage
- LA = Inventory Lock
	- Lock inventory slots to prevent sorting, moving or dropping.
- F = Move Matching Items
	- Move from the inventory under cursor to the other.
	- LC + F = Move All Selected
	- LS + F = Move Everything
		- *Useful for looting*
- G = Drop Selected
	- Y = Drop All Selected
	- LS + Y = Drop Everything
		- *Drops everything from the inventory under cursor*
		- *Works best with Sophisticated Backpack Pick Up or Magnet Upgrade to quickly transfer to backpack*
	- LC + G = Drop One Stack Selected

## 3. Common

R = Point Blank Reload Gun
- Y = Point Blank Attachment Mode
- X = Change Fire Mode
- F = Switch Scope
- LS + R = Inspect Gun
LS + F = Create Mod Block Rotation
T = Create Aeronautics Physics Staff Rotate Mode
	 I = Linked Typewriter Curio Slot
	. = Tracks Tuning
U = Death History
O = Autofish
- LC + O = Autofish GUI
P = List Players (Minimap Icon)
%%- F = Torch
    > Place torch from hotbar.%%
%%K = Toggle Block Randomizer%%
%%K = Quark Placement Orientation Lock
	*Locks the placement orientation of blocks such as stairs.*%%
L = Advancements
Z = Touhou Little Maid Dismount
	Enter = STT AI Chat
	, = Switch Broom Control Mode
N + Mouse2 = Carry On
- *Works on entities within a small range.*
F = Effortless Building
	LC + Z = Undo
	LC + Y = Redo
	+ = Modifier Menu
J = Reacharound Placement
LA = Create Mod Toolbox (Schematic Overlay)
Capslock = Push to Talk
- LC + Capslock = Voice Chat GUI
%%    LS + Capslock = Mute Microphone%%
Enter = Chat
/ = Command
Num 0 = Physics Toggle
F4 = Exposure Camera Controls
F6 = Shaderpack Selection
F7 = Physics Menu
%%F8 = Apotheosis World Tier%%
F9 = Observable Profiler Screen

## 4. Map

M = Worldmap Toggle
- LS + M = Minimap Toggle
	- Backspace = Minimap Enlarge
	- \+ = Minimap Zoom In
	- \- = Minimap Zoom Out
- ' = Waypoint Screen
	- *This is the key left of Enter*
	- B = New Waypoint
	- LS + B = New Quick Waypoint
	- \[ = Toggle Waypoint In-Game
	- ] = Toggle Waypoint On-Map
/creative_dim = Creative Sandbox
## 5. Information

A = JEI Bookmark
- R = JEI Show Recipe
	*Affects the item under cursor*
- U = JEI Show Uses
	*Affects the item under cursor*
- Backspace = JEI Show Previous Recipe
	*Only works when accessing a recipe via a previous one*
- LC + O = JEI Overlay Toggle
	*Only works inside the inventory UI*
- LC + F = JEI Search Bar Focus
Num 1 = The One Probe Overlay Toggle
- Num 2 = The One Probe Overlay Liquid
F9 = Observable Profiler

## 6. Misc

Mouse4 = Back
	*Navigate back from the previous UI*
%%Mouse5 = Camera Zoom%%
%%Pause = Reduce FPS
    LC + Pause = FPS Reducer GUI%%
%%J = Ping Menu%%
Num 0 = Social Interaction
%%- \\\\ = Salute
- Num 7 = Emote Yes
- Num 4 = Emote No
- Num 8 = Emote Clap
- Num 5 = Emote Weep
- Num 9 = Emote Wave
- Num 6 = Emote Shrug%%
F1 = UI
F2 = Cinematic Camera
F3 = Information Overlay
F5 = Perspective Toggle
%%F6 = Shoulder Surfing Toggle
    F7 = Shoulder Surfing Swap
    Up Arrow = Shoulder Surfing Camera Up
    Down Arrow = Shoulder Surfing Camera Down
    Left Arrow = Shoulder Surfing Camera Left
    Right Arrow = Shoulder Surfing Camera Right
    Page Up = Shoulder Surfing Camera Closer
    Page Down = Shoulder Surfing Camera Farther%%
F10 = Dynamic Surroundings
F11 = Fullscreen
F12 = Screenshot
%%F12 = Camera Mode%%

## 7. Commands

`/trigger sethome`
`/trigger home`
`/trigger spawn`
`/trigger back`
`/trigger tpa set`

# Changelog

## 1.21.1-2.8

Added:
- Create: Coasters Simulated
- Create: Advanced Optimization
- Sophisticated Storage Create Integration
- Sophisticated Backpacks Create Integration
- Create Better FPS
- Sound Physics: Aeronautics
- Enhanced Celestials 2: Core
	- Enhanced Celestials 2: Default Lunar Events
	- Enhanced Celestials 2: Shader Supoport

Removed:
- Enhanced Celestials (Superceded by Enhanced Celestials 2: Core)
	- Peaceful Moon
	- Ender Moon
	- Horde Moon
	- Black Moon
	- Kaboom Moon
	- Spider Moon
- Ping to Map (Redundant visual overlay)

## 1.21.1-2.7.1

Added:
- Xaero's Maps x Waystones (XaeroPlus waystone waypoints broken)

Removed:
- Xaero Map Regions (Jank)

## 1.21.1-2.7

Bumped neoforge to 21.1.244.

Added:
- XaeroPlus (Performance and misc features)
- Xaero's Maps: Multiplayer+ (Shared map progress)
- Compass to Map: Xaero's Minimap & Explorer's Compass & Nature's Compass Addon (Show compass destination on map)
- Sable x Xaero Bridge (Show sub-levels on map)
- Ping to Map: Xaero's Minimap & Ping Wheel Addon (Show pings on map)
- Xaero Map Regions (Regions on map)
- Xaero's Drawings (Draw on map)

Removed:
- Xaero's Maps x Waystones (Deprecated, use XaeroPlus)
- Critters and Companions (Shell bug and ecosystem mismatch)

## 1.21.1-2.6

Added:
- Create Jetpack
- Jade Sable Compat
- VS/Sable Hose Connectors

## 1.21.1-2.5

Added:
- Cosmetic Armor Reworked
- Fast Travel Waypoints
- Waystone Teletport Pets
- Maidsoul Kitchen (Maids use kitchen from mods such as Farmer's Delight)
- Maid Useful Tasks (Logging, locate, revive)
- Better Carryon Maid (N + Mouse2 will use saddle carry animation)
- Empty Hand Keybind - Hold Onto THIS (\` to empty selected hotbar, again to switch back)
- Exposure Catalog

Removed:
- IPBR+ generated normals (Causing artifacts with TLM assets and general visual noise)

Changed:
- Default Hotkeys Remapped
- Atlas keys information updated
- New options file distributed

## 1.21.1-2.4

Added:
- ~~Sable: Collision Damage~~ Not ready for implementation
- Keybind Atlas (K to view all keybinds)
- Wakes (Visual effeccts in water)
- Nyf's Spiders (Spider AI)
- BarSwap (V to swap hotbar rows)
- Moon events
	- Peaceful Moon
	- Ender Moon
	- Horde Moon
	- Black Moon
	- Kaboom Moon
	- Spider Moon
- Sable Dynamic Lights
- Lamb Dynamic Lights
- Fragrant Flowers Expanded (Resource pack for flowers)
- Icon Xaero's (Resource pack for map entity icons)
- Drip sounds (Ambient sounds)
- More Sound (Compat layer for Sounds)

Removed:
- Embrace Pixels PBR (Using generated normals instead)

## 1.21.1-2.3

Added:
- Aero Portals (Create Aeronautics + Portals)
	- Aero Claims
		- Open Parties And Claims
	- Create Aeronautics Curios
	- Create Treadmill
	- Aeronautics Replay
	- Pointblank Aero Compat
- Touhou Little Maid
	- Tide Maid
	- Maid Use Hand Crank
	- Maid Beacon
- Creative Sandbox (Enter with /creative_dim)
- Presence Footsteps

Removed:
- Just Another Void Dimension
- Inv Move

## 1.21.1-2.0
New World Save

Removed:
- Terralith
- Apotheosis

Added:
- Create Aeronautics



## 1.21.1-1.8
Cleaned up world save data

Added:
- Trash Slot
- Companion

## 1.21.1-1.7
Bumped Neoforge to 21.1.218

Removed:
- Clean Swing
- The One Probe
- Terralith
- Trash Slot
- Overloaded Armor Bar
- Ready Player Fun

Added:
- An Earth dimension at 1:6000 scale
	- -1355 255 -749
	- [Coordinate Calculator](https://earth.motfe.net/coordinate-calculator/)
- Multiplayer Server Pause
- Qliphoth Awakening
- Revive Me!
- PointBlank: Jelly
- [Point Blank - Counter-Strike](https://legacy.curseforge.com/minecraft/customization/point-blank-counter-strike)
- Smart Particles
- Particular Reforged
- Particle Effects C
- Particle Rain
- Inventory Particles C
- InvMove
- Cut Through
- Jade
- Jade Addons
- Overflowing Bars
- Tide 2
- RealmRPG Balloons
- Critters and Companions
- Exposure
- Exposure Polaroid
- Exposure Addon
- Viscord
- Simple Datapacks

Updated:
- Create
- Apotheosis + Components
- Distant Horizons
- Many other mods

Client Ignore List:
- \AmbientEnvironment*.jar
- \AmbientSounds*.jar
- \better-loading-screen*.jar
- \betterbiomeblend*.jar
- \BetterF3*.jar
- \betterfoliage*.jar
- \betterfpsdist*.jar
- \BetterPingDisplay*.jar
- \BetterThirdPerson*.jar
- \blockrandomizer*.jar
- \blur-neoforge-*.jar
- \BridgingMod-*.jar
- \chat_heads*.jar
- \cherishedworlds*.jar
- \colorfulhearts*.jar
- \Controlling-*.jar
- \coolrain-*.jar
- \CutThrough-*.jar
- \DetailArmorBar*.jar
- \double_hotbar*.jar
- \DripSounds*.jar
- \durabilitytooltip*.jar
- \ears-forge*.jar
- \elytracam*.jar
- \embeddium*.jar
- \EnchantmentDescriptions*.jar
- \entityculling*.jar
- \Fallingleaves*.jar
- \firstperson-*.jar
- \forgeautofish*.jar
- \FpsReducer2*.jar
- \HealthOverlay*.jar
- \InventoryParticles-*.jar
- \InventoryProfilesNext*.jar
- \InvMove-*.jar
- \LegendaryTooltips*.jar
- \loot_journal*.jar
- \make_bubbles_pop*.jar
- \modnametooltip*.jar
- \MouseTweaks*.jar
- \MyServerIsCompatible*.jar
- \notenoughanimations*.jar
- \oculus-mc*.jar
- \OptiFine*.jar
- \overloadedarmorbar*.jar
- \ParticleEffects-*.jar
- \particlerain-*.jar
- \particular-*.jar
- \PresenceFootsteps*.jar
- \Prism*.jar
- \raised-forge*.jar
- \reforgedplaymod*.jar
- \seamless-loading-screen*.jar
- \ShoulderSurfing*.jar
- \shutupexperimentalsettings*.jar
- \smoothscrolling-*.jar
- \soundphysics*.jar
- \sounds*.jar
- \MRU*.jar
- \torch-key*.jar
- \torohealth*.jar
- \TravelersTitles*.jar
- \ToastControl*.jar


## 1.21.1-1.0

Bumped version to 1.21.1 neoforge

Removed:
    Amplified Nether
    Alex's Mobs
    Alex's Delight
    Dave's Potionerring
    MineColonies
    TownTalk
    Sophisticated Storage
    Starter Kit

Unavailable:
    Awesome Dungeon
    Better Spawn Control
    Better Village
    Chisels and Bits
    Drip Sounds
    Durability Tooltip
    Fast Suite
    Goblin Trader
    Multiplayer Server Pause
    Naturalist
    Presence Footsteps
    Quark
    Quark's Delight
    Regrowth
    Tetra
    Tetra Extras
    Tetra's Delight
    Immersive Weathering

Added:
    Apotheosis (Replacing Tetra)
    Dynamic Surroundings
    ImmediatelyFast
    Immersive Portals