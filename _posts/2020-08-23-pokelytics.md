---
title: 'An Analytic Approach to the Pokémon Trading Card Game'
date: 2020-08-23
permalink: /posts/2020/08/pokelytics-00/
tags:
  - pokmeon
  - blog
  - pokelytics
  = unsupervised learning
  - Principle Component Analysis
  - Markbet Basket Analysis 
---

Introduction
======
Hello everyone! My name is Brad Erickson and I have been a fan of Pokémon for as long as I can remember. I have been playing the trading card game since Diamond and Pearl’s release in 2007. I had a good run my last year of the Senior division during the 2011-2012 season, just missing my invite by a few spots. In my career in the Master’s division, I’ve top 16’d Madison regionals and won a handful of League Cups. Outside of my passion for Pokémon, I recently began my pursuing my PhD in Computer Science, with a focus on Data Analytics.
Today, I will try to use my analytical toolset and apply it to the competitive Pokémon TCG scene. With these tools, I will be looking at what differentiates decklists of a single archetype and what cards are commonly found together. The tools may point of obvious observations, such as Jirachi and Escape Board being paired together, luckily, we have some more interesting findings.

Data
======
The data comes from the Limitless Online Tournament series. The first 2 tournaments were "Ultra Prism - Sword & Shield" format and the last 2/invitational were "Ultra Prism - Rebel Clash". We will focus on the more recent format. 
An example of what our data looks like is shown below. The percentile column refers to how well the deck did 100% = 1st, 0% = last (these are only for decks that made day 2). The bin column is for Top 8, Top 16, etc. Beyond the label column will just be what cards are in the deck and their respective counts.
