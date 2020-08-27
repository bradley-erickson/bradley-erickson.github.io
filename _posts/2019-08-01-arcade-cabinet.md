---
title: 'Refurbishing an old arcade cabinet'
date: 2019-08-01
permalink: /posts/2019/08/arcade-cabinet/
tags:
  - arcade
  - raspberry pi
  - hardware
---

### Under Construction

In the summer of 2019, I spent time refurbishing an old arcade cabinet. I will be updating this periodically with how I did it!

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

I had an extra Raspberry Pi sitting around, so I figured it would use that for the computer. For controls, I did some research into what setup each player should have. After reviewing common day fighting game boards and looking for parts, I decided each player will have 1 joy-con, 8 buttons, and a start button. For computer to controls, I narrowed it down to 2 options: IPAC and Plug-n-Play boards. I decided on IPAC so I didn't have to deal with adding connectors. Essentially the board shown below with all the wires going into it, will act like a keyboard. That means each control is mapped to a single key (I'll go into setting this up in a later section). Luckily, I found an IPAC setup with wires, 18 buttons, and 2 joy-cons from UltraCabs online [here](https://www.ultracabs.co.uk) (last I checked the website was down).

| ![Control design 01](/images/arcade/controls_design01.jpg) | ![Control design 02](/images/arcade/controls_design02.jpg) |
|:---:|:---:|
| Initial design | Final design |

I took some schematics of fighting game boards as a starting point for designing the board. I finalized the design on paper and transferred it to a 3D file. The initial design accounted for the entire control block to be 3D printed, but after analyzing the cost, I scrapped that idea. I went for a simpler design that I could attach to wood. Winona State University, the school I did my undergrad at, offered 3D printing for students, but had size limitations. I cut down the singular long piece and added some constraints to get printed as well.
**Improvement:** I must have been too excited while designing this, because I overlooked 1 crucial piece. The joy-con is supposed to under the top not over. Luckily, this is not a huge deal, just aesthetics.

| ![Control print 01](/images/arcade/controls_print01.jpg) | ![Control print 02](/images/arcade/controls_print02.jpg) |
|:---:|:---:|
| Prints unassembled | Assembled with buttons |

### Lights/Sound/Security

sound and light

## Software

### IPAC configuration

### RetroPie

### Setting controls

### Adding games

### Music
