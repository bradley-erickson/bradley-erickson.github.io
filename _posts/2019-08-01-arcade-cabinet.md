---
title: 'Refurbishing an old arcade cabinet'
date: 2019-08-01
permalink: /posts/2019/08/arcade-cabinet/
excerpt: 'In the summer of 2019, I spent time refurbishing an old arcade cabinet. I will be updating this periodically with how I did it!'
tags:
  - arcade
  - raspberry pi
  - hardware
---

In the summer of 2019, I spent time refurbishing an old arcade cabinet. Here's how:

## Introduction

Arcade games provide a fun medium for 2-player gaming. Since I was little, I loved the idea of going to an Arcade and playing every game possible, but sadly, I was born a little past the arcade hype. I had seen some basic tabletop arcade units powered by a Raspberry Pi on the internet and thought that looked like a fun project. While the tabletop units are very portable, I wanted the full-blown arcade experience. I reached out to a friend and he knew a guy that just had an old stripped down Star Gate cabinet in his garage for sale. I immediately got his contact and bought the machine.

I will be breaking this down into main 2 categories: Hardware & Software. Hardware will focus on anything from the unit itself to the joysticks and buttons. Software will focus on the operating system and what configuration changes I made.

## Hardware

The hardware is broken down into 5 pieces: Cabinet, Controls, Computer, Power, and Sound.

### Cabinet

The cabinet I received was painted entirely black. Sadly, I forgot to take pictures of it in that state. I stripped the paint off using some paint remover. I was able to get down to the original paint, but not much more than that. The inside of the cabinet was already gutted down, so I will not be touching that in this section

| ![Outside before 01](/images/arcade/outside_before01.jpg) | ![Outside before 02](/images/arcade/outside_before02.jpg) | ![Outside before 03](/images/arcade/outside_before03.jpg) |
|:---:|:---:|:---:|
| Original Star Gate logo | Another view of logo | Front view without back attached |

I put down a primer coat of paint. My original design was to make a bunch of doodles on the sides, but I decided against that idea. The idea of *The Hive* popped into my head. Bee's are cool and the yellow will stand out. After a week of thinking, I decided on *The Hive*. I chose a basic design of honeycombs and a little bee flying through the air. My dad helped me create a stencil and did a good job helping me paint. We used black and yellow spray paint for the background and bottom. For the honeycomb and bees, we used some black wood paint.

| ![Outside white 01](/images/arcade/outside_white01.jpg) | ![Outside paint 01](/images/arcade/outside_paint01.jpg) | ![Outside paint 02](/images/arcade/outside_paint02.jpg) |
|:---:|:---:|:---:|
| Painted white | Painting view 1 | Painting view 2 |

| ![Outside final 01](/images/arcade/outside_final01.jpg) | ![Outside final 02](/images/arcade/outside_final02.jpg) |
|:---:|:---:|
| Final view 1 | Final view 2 |

### Controls/Computer

I had an extra Raspberry Pi sitting around, so I figured it would use that for the computer. For controls, I did some research into what setup each player should have. After reviewing common day fighting game boards and looking for parts, I decided each player will have 1 joy-con, 8 buttons, and a start button. For computer to controls, I narrowed it down to 2 options: IPAC and Plug-n-Play boards. I decided on IPAC so I did not have to deal with adding connectors. Essentially the board shown below with all the wires going into it, will act like a keyboard. That means each control is mapped to a single key (I will go into setting this up in a later section). Luckily, I found an IPAC setup with wires, 18 buttons, and 2 joy-cons from UltraCabs online [here](https://www.ultracabs.co.uk) (last I checked the website was down).

| ![Control design 01](/images/arcade/controls_design01.jpg) | ![Control design 02](/images/arcade/controls_design02.jpg) |
|:---:|:---:|
| Initial design | Final design |

I took some schematics of fighting game boards as a starting point for designing the board. I finalized the design on paper and transferred it to a 3D file. The initial design accounted for the entire control block to be 3D printed, but after analyzing the cost, I scrapped that idea. I went for a simpler design that I could attach to wood. Winona State University, the school I did my undergrad at, offered 3D printing for students, but had size limitations. I cut down the singular long piece and added some constraints to get printed as well.

**Improvement:** I must have been too excited while designing this, because I overlooked 1 crucial piece. The joy-con is supposed to under the top not over. Luckily, this is not a huge deal, just aesthetics.

| ![Control print 01](/images/arcade/controls_print01.jpg) | ![Control print 02](/images/arcade/controls_print02.jpg) |
|:---:|:---:|
| Prints unassembled | Assembled with buttons |

| ![Controls assembled](/images/arcade/controls_assembled.jpg) |
|:---:|
| Controls assembled |

My dad built the piece of wood that we attached the control print and computer to. Once I picked out spots for everything, I cut all the wires and started wiring the buttons. I had some leftover command strips so I used those to pretty up the wiring. A major difficult was attached this control block to the unit. I mismeasured the pillars and got really close to one of attachment holes. I added a gate latch to hold it in place and to have quick access if something breaks. On the mounted picture, notice the 2 wires for controls (1 for powering lights, 1 for the actual controls), an HDMI-DVI connector, and power.

| ![Control wiring 01](/images/arcade/controls_wiring.jpg) | ![Control wiring 02](/images/arcade/controls_wiring_mounted.jpg) |
|:---:|:---:|
| Controls wired | Control unit mounted |

The last piece of the controls, came a few months after I finished the project. I found that on the N64 emulator, I could not remap buttons to be combinations (like shift + R). Most emulators allow this and use this for the save/load/exit buttons. To resolve this, I created a save/load/exit section with a numpad for choosing which save slot to use. I plugged the buttons into the IPAC controller and the number directly into the Raspberry Pi. All that extra looking stuff is just leftovers from the coin mechanism.

| ![Save/Load/Exit piece](/images/arcade/controls_numpad.jpg) |
|:---:|
| Save/Load/Exit piece |

### Lights/Sound/Screen/Security

For the marquee light, I picked up an under cabinet/work bench light from Menard's. I did not want initially invest too much into the marquee label, so I printed off my design on thin paper and taped it to plexiglass. For the sound, I used an old amp I got from [Amazon](https://www.amazon.com/gp/product/B018QKX8E0/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) a few years ago combined with some speakers I tore apart from Goodwill. I know enough about speaker setup to solder some wires to the speakers and plug those wires into the amp. I use a 2-1 audio cable to connect the amp to the HDMI connected attached to the Raspberry Pi. Back in my high school gaming days, I had two monitors for my desktop. I had not been using both for a while so I put one in the cabinet. My dad built the walls of the "hallway" leading from the player to the screen. The power is located in the coin drop. Just flip the power switch and everything will turn on.
Finally, for security, I use a variety of tubular locks: 1 for the coin slot (access to the amp), 1 to the power, and 1 to open up the backside.

**Improvement** Replace the marquee with a better print and get a brighter light.

| ![Lights and sound 01](/images/arcade/lights_sound01.jpg) | ![Lights and sound 02](/images/arcade/lights_sound02.jpg) |
|:---:|:---:|
| Marquee light and speakers | Lit marquee |

| ![Lights and sound 03](/images/arcade/lights_sound03.jpg) | ![Power](/images/arcade/power01.jpg) |
|:---:|:---:|
| Mounted amp | Power strip in coin drop |

## Software

I will do my best to completely fill out this section, but since I am writing this a year later, I am certain I will miss things.

### IPAC configuration

To configure the IPAC system, I downloaded [WinIPAC V.2](https://www.ultimarc.com/control-interfaces/i-pacs/i-pac2/?selected_section=product_tab_25#product_tab_25) on my laptop. This is a graphical user interface to configuration what keys will correspond to which inputs. Just to be safe, I backed up the default then mapped the keys I wanted to use. I opened up notepad and tested the buttons to confirm the configuration was successful.

**Note:** Careful setting the controls for the joysticks. When you press up, the joystick will click the bottom switch.

### RetroPie

For the operating system, I installed [RetroPie](https://retropie.org.uk/). Retro Pie is an operating system dedicated for emulating games. I am running the build compatible with a Raspberry Pi 3. Retro Pie has a wonderful getting [startup guide](https://retropie.org.uk/docs/First-Installation/) for first time installation.

### Setting controls

To set the controls up inside RetroPie, we need to access the configuration files. When you start-up Retro Pie for the first time, it will ask you to configure whatever "controller" you have plugged in. I found it easier to lazily go through this and update them directly in the configuration file. To access the configuration file, **ADD SOMETHING HERE**. Retro Pie has a 3-tier hierarchy of controls: Global, System specific, and ROM specific. [This piece](https://retropie.org.uk/docs/RetroArch-Configuration/#hardcoded-configurations) of the Retro Pie documentation goes into where the configurations are located and how they look.

**Note:** The N64 uses a different emulating system than most. I found that I was unable to remap the Start, Load, and Exit buttons. Additionally, the N64 does not support button combinations such as *shift+R*. This is the reason I added the number pad and 3 additional buttons.

### Adding games

A flash drive is needed to add games. Simply plug in the flash drive to the system and boot it up. Then, boot the system down and unplug the flash drive. This formats the flash drive to have the correct directories for automatically adding games. To download emulators, check out [Cool ROM](https://coolrom.com.au/emulators/) or [Emulator.Games](https://emulator.games/). Since I am using a Raspberry Pi, the memory is limited. That means N64 games are about the max graphics it can handle. Just download the emulator zip files and place the zips inside their respective console folder on the flash drive. Lucky for you, most games made during the N64 era and prior are super small in terms of file size. Plug the flash drive back into the Raspberry Pi and power up. This may take longer than a usual boot, because we are copying games over.

**Note:** I had problems uploading N64 games at first. I fixed this by manually unzipping the file and placing the .z64 file in N64 directory.

### Music

The Emulation Station is the main screen where you choose what games to play from. I used [this guide](https://retropie.org.uk/forum/topic/9133/quick-and-easy-guide-for-adding-music-to-emulatonstation-on-retropie-noob-friendly/2) to add music to it. That guide was super easy to follow. To add the music, I would pull out the Micro-SD card and plug it into my laptop to transfer .mp3 files. Some of the music I chose:

* Kirby Air Ride - City Trials
* Super Smash Bros Brawl - Title theme
* Pokémon Diamond and Pearl - Route 216
* F-Zero - Theme
* Legend of Zelda - Theme
* Halo - Theme

## Test ride
