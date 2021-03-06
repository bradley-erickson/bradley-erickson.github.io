---
layout: single
title: Data Driven Pokémon - Episode 1
header:
  teaser: /images/pokemon_backs.jpg
date: 2020-08-22
permalink: /posts/2020/08/data-driven-pokemon-01/
excerpt: I take a crack at explaining and visualizing important decklist features in the Pokémon Trading Card Game.
tags:
  - Pokémon
  - data science
  - unsupervised learning
  - Principle Component Analysis
  - Market Basket Analysis 
---

## Introduction

Hello everyone! My name is Brad Erickson and I have been a fan of Pokémon for as long as I can remember. I have been playing the trading card game since Diamond and Pearl’s release in 2007. I had a good run my last year of the Senior division during the 2011-2012 season, just missing my invite by a few spots. In my Master’s division career, I’ve top 16’d Madison regionals and won a handful of League Cups. Outside of my passion for Pokémon, I recently began my pursuing my PhD in Computer Science, with a focus on machine learning and analytics.
Today, I will try to use my analytical toolset and apply it to the competitive Pokémon TCG scene. With these tools, I will be looking at what differentiates decklists of a single archetype and what cards are commonly found together. The tools may point out obvious observations, such as Jirachi and Escape Board being paired together, luckily, I have more interesting findings to talk about.

## For non-Pokémon players

The Pokémon Trading Card Game consists of 2 players playing 60 card decks. Every 3 months, a new set of cards are released and thus change how decks are built. The following is a set of common vocabulary:

* Format: Set of card sets players are allowed to use.
* Archetype: Primary cards used in deck.
* Top X: Prize payout is determined by how well a player places. If a player places 12th, they placed in Top 16.

## Data

The data comes from the Limitless Online Tournament series. The first 2 tournaments were "Ultra Prism - Sword & Shield" format and the last 2/invitational were "Ultra Prism - Rebel Clash". We will focus on the more recent format.
An example of what our data looks like is shown below. The percentile column refers to how well the deck did 100% = 1st, 0% = last (these are only for decks that made day 2). The bin column is for Top 8, Top 16, etc. Beyond the label column will just be what cards are in the deck and their respective counts.

![Data snippet](/images/pokemon01/data_snippet.png)

## Analysis

First, I will take a gander at everything combined. I will use this first analysis to explain what I am doing and what the plots show. Then, I will be individually looking at 5 of the most played archetypes from these events: Blacephalon, Dragapult, PikaRom, Zacian, and Zacian ADP.
The primary method we are using is Principle Component Analysis (PCA). PCA is a dimension reduction technique. This means that we are feeding in data, in our case decklists, with many variables, e.g. 1 Absol, 3 Acro Bike, etc., and returning a new set of variables that will maximize variance between decklists. This means that similar decklists will be like one another, while different decklists are further apart.
Additionally, we will be conducting Market Basket Analysis (MBA). Stores use this technique to determine what items are often purchased together. In our analysis, we will probably see some obvious items, or cards, used in the same decklist. For example, if you play Malamar, you will play Inkay. Both PCA and MBA may seem a hair confusing, so we will work through the Overall decks slowly.

### Overall

Focusing on the Ultra Prism - Rebel Clash format, these are the most common decks across Qualifier #3, Qualifier #4, and the Invitational:

![Most played decks](/images/pokemon01/overall_deck_counts.png)

We will now apply PCA to the data. With this many decks, we will likely see differences primarily among the top decks. The bar plot below shows the cards that contribute the most to separating the different decks. We see that quite a few at type related, which makes sense that Fire decks should be separate from the lightning decks. Additionally, we see Professor’s Research on here. This will help further separate decks based on the draw engine they run.

![Overall PCA contributions](/images/pokemon01/overall_pca_contrib.png)

Now that we know what cards are contributing the most to the separation of the decks, we can look at the decks themselves. The graph below shows all the decks used with the card contributions on top. We have the colors grouped by Top 8, Top 16, etc. We can tell based on the card contributions what decks are where. The lower left is for Fire decks (mostly Blacephalon), the lower right is for Lightning decks (PikaRom), and the top is for Metal decks (Zacian, Zacian ADP). Along the x-axis and y-axis, we see a percentage value. This is the percent variance explained. In layman’s terms, the x-axis explains 30.4% of the variance among decks. The y-axis explains 23.1%. Together, they explain 53.4% of the variance. Ideally, we want this number to be close to 100%, but the massive overlap in cards (Quick Ball, Dedenne-GX, Switch, etc.) makes that difficult.
We can learn a few things about how decks are built. Since Professor’s Research is pointing in an opposite direction from the Fire area, we can assume that most Fire decks do not focus on using Research as their draw supporter. This makes sense because Welder exists. Similarly, Scoop Up Net opposes the Lightning decks. With the focus of GX and V Pokémon in PikaRom, it makes sense that we do not see many of them running Scoop Up Net. This does not mean that every Lightning deck does not play Scoop Up Net. This simply means that Scoop Up Net is not commonly found in Lightning decks. That is about all we can pull from PCA on all the decklists, so we will move onto the MBA.

![Overall PCA biplot](/images/pokemon01/overall_pca_biplot.png)

To start with the MBA, we will look at what cards are most used. With our data, we will simply ask if Quick Ball is in a deck or not and not bother checking how many Quick Ball a deck has. The bar plot shows the top 20 cards used in all decks. Right away, we see that Quick Ball is used in 100% of decks. Switch is used is most but not all decks. We can see some common tech cards such as Tool Scrapper and Bench Barrier Mew. Later, we will use this to determine what the core of an archetype is.

![Overall card frequencies](/images/pokemon01/overall_card_frequency.png)

For relationships between cards, we will look at what cards are in the same deck as another and how often. If I chose to play X, how likely am I to play Y? We will say that X -> Y. Note that X -> Y is not necessarily the same as Y -> X. For this graphic, the size compares how popular that rule, or card pair, is used in decks. The color describes how strong that relationship is, or how likely they are to be played together. The darker the circle, the more likely they are. This is difficult to look at for the overall data because many of the rules only apply to specific archetypes. The graph below illustrates this problem. We have 3 chunks of relationships: the larger is all things Blacephalon, the medium chunk is for Dragapult, and the smallest is ADP and Water Energy. I will take a closer look when I get to specific archetypes.

![Overall card relationships](/images/pokemon01/overall_rules.png)

Now that we finished the overall decklists, we can begin focusing on the individual archetypes. Instead of a large explanation for each archetype, I will include the graphs and a list of interesting findings.

### Pikachu & Zekrom Tag Team

Note: Pikachu & Zekrom Tag Team, or PikaRom, here is referring to decks labelled Pikachu & Zekrom Tag Team. Green’s Pikachu and Zekrom are not included with this portion of analysis.

![PikaRom PCA contributions](/images/pokemon01/pikarom_pca_contrib.png)

The main distinction card to PikaRom lists is Volkner. This is not super surprising. I find that PikaRom players love playing with every out to every item card or love playing for the almost guaranteed turn 2 full blitz with a Tag Call engine. In the biplot, we see decks along the right side all use Volkner, while decks on the left use a Tag Call/Guzma & Hala/Marnie engine. Decks along the middle went for a split between the engines. Additionally, we see Jirachi and Escape Board opposing Dedenne-GX, Professor’s Research, and others. Looking back on some of the lists, I noticed that Jirachi engines played fewer Dedenne-GX and Professor’s Research. The colors in this biplot correspond to which Tournament they were played in. We see few players opt for Marnie in Qualifier #3, but many played Marnie in Qualifier #4. Additionally, we see that no players in the Invitational opted for a full Volkner engine.

![PikaRom PCA biplot UPR-RCL](/images/pokemon01/pikarom_pca_biplot_tours.png)

Additionally, we can look at how Rebel Clash changed the format. We see that most deck pre-Rebel Clash focused on Jirachi and Volkner for their draw engine. The introduction of Speed Energy gave a boost of energy to Guzma & Hala’s power.

![PikaRom PCA biplot UPR-SWSH](/images/pokemon01/pikarom_pca_biplot_all_tours.png)

Future work: PikaRom over multiple formats.

Our deck basket will help us understand common cards and relationships within decks.

**Core must-haves:** Dedenne-GX, Quick Ball, Electropower, Lightning Energy, Pikachu & Zekrom Tag Team, Tapu Koko Prism, and Boss’s Orders

**Big contenders:** Switch, Raichu & Alolan Raichu Tag Team, Thunder Mountain, Speed Energy, Reset Stamp, Boltund V, Energy Switch, Zeraora-GX, Electromagnetic Rader, and Professor’s Research

**Common Techs:** Big Charm, Great Catcher, Stadium-bump Marshadow, and Mallow & Lana

![PikaRom card frequency](/images/pokemon01/pikarom_card_frequency.png)

Looking at the rules, we find an obvious rule right off the bat. Playing Jirachi implying Escape Board and vice versa. Interesting to see that Stadium Nav is only played with some form of Volkner engine. The last piece is the Tag Call engine. We see playing Air Balloon, implies playing a Tag Call engine with Mallow & Lana; however, neither of those imply you play Air Balloon.  

![PikaRom card relationships](/images/pokemon01/pikarom_rules.png)

### Zacian

Note: The Zacian labels includes both Combo-Style Zacian (Jirachi Prism Star and Detective Pikachu Mr. Mime) and Straight Zacian.

![Zacian PCA contributions](/images/pokemon01/zacian_pca_contrib.png)

Whether a player plays an Acro Bike engine or not, helps decide what other cards you are playing. Looking at our biplot, we can see that few Qualifier #3 Zacian decks opted for the Acro Bike Engine. The players that did not opt for Acro Bikes, went more for cards like Shrine of Punishment, Sonia, or Metal Goggles. With the Mr. Mime pointing in the same direction as Acro Bike, we know that players who used the Acro Bike engine played an increase count of Mr. Mime. The 2 decks, or points, in the lower left corner are the 2 instances of Straight-Zacian.

![Zacian PCA biplot UPR-RCL](/images/pokemon01/zacian_pca_biplot.png)

**Core must-haves:** Marnie, Metal Energy, Metal Saucer, Oranguru, Professor’s Research, Quick Ball, Switch, and Zacian V

**Big contenders:** Dedenne-GX, Escape Board, Great Catcher, Jirachi, Boss’s Orders, Scoop Up Net, Jirachi Prism, Mr. Mime, and Tool Scrapper

**Common Techs:** Tapu Fini and Dusk-Mane Necrozma

![Zacian card frequency](/images/pokemon01/zacian_card_frequency.png)

About half of the decks played Acro Bike. According to our rules, if you play Acro Bike, you are more likely to play Tapu Fini. While this is not a super strong relationship, it happens often. We see Galarian Zigzagoon, Hoopa, and Metal Goggles all imply you play Shrine of Punishment. Zigzagoon and Hoopa are different damage modifiers to pair with Shrine of Punishment for setting up big knockouts. Lastly, we see Metal Goggles and Reset Stamp implying you play Mew.

![Zacian card relationships](/images/pokemon01/zacian_rules.png)

### Dragapult

![Dragapult PCA contributions](/images/pokemon01/dragapult_pca_contrib.png)

Starting off with Dragapult, we see that Crushing Hammer and Super Scoop Up account for most of the variance between decks. These are 2 more popular routes players take when deciding how to build their Dragapult deck. We also see Cynthia and Marnie as cards that introduce a lot of variance. Looking at our biplot, we see they are opposites of one another. Usually players will not play a large mix of both. We see that the Super Scoop Up is pointing in the same direction as Malamar and Inkay. We will see if this is a common combination during our MBA. We have a pretty good spread between Quarter #3 and Quarter #4, but we see now Invitational decks chose the Giant Bomb or Super Scoop Up route.

![Dragapult PCA biplot UPR-RCL](/images/pokemon01/dragapult_pca_biplot_tours.png)

For Dragapult, it is worth looking at how decks stacked up based on placement. The points are all roughly the same as before, just colored by Top 8, Top 16, etc. We see no darker points near Super Scoop Up. This means that this version of Dragapult did not place super well. Crushing Hammer, Power Plant, and Reset Stamp seems to be factors of the better placing Dragapult decks.

![Dragapult PCA biplot UPR-RCL](/images/pokemon01/dragapult_pca_biplot_groups.png)

**Core must-haves:** Quick Ball, Switch, Psychic Energy, Mysterious Treasure, Boss’s Orders, Dragapult V, and Dragapult VMAX

**Big contenders:** Professor’s Research, Horror Energy, Dedenne-GX, Jirachi, Marnie, Escape Board, Scoop Up Net, and Galarian Zigzagoon

**Common Techs:** Reset Stamp, Phione, Bench Barrier Mew, and Scoop Up Block Mr. Mime

![Dragapult card frequency](/images/pokemon01/dragapult_card_frequency.png)

Looking at the relationships, we have some interesting findings. For one, it appears that if you are playing Gengar & Mimikyu Tag Team or Super Scoop Up, then we imply you are playing a Malamar engine. Interestingly, if you play Oranguru, we can imply you are playing Mewtwo. This is common combo to use: Mewtwo a supporter to the top of your deck and use Oranguru to put it into your hand. Lastly, we see a classic late game combo to ruin our opponent’s chances of drawing those last few outs: Plant and Stamp. If a player plays Power Plant, we can assume they also play Reset Stamp.

![Dragapult card relationships](/images/pokemon01/dragapult_rules.png)

### Blacephalon

![Blacephalon PCA contributions](/images/pokemon01/blacephalon_pca_contrib.png)

The cards that contribute the most variance to Blacephalon are Scoop Up Net and Acro Bike. Scrolling back through the lists, it looks like decks did not often play both cards. In our biplot, we see a few different chunks of data. First off, we see a large chunk of the decks on the left side. These are probably the more straightforward builds. On the top right, we see another chunk. These decks put a focus tools and stadiums with cards like Stadium Nav, Beast Bringer, and Adventure Bag. Lastly, there is a few scattered points in the bottom right corner. These decks rely on an Acro Bike engine.

![Blacephalon PCA biplot UPR-RCL](/images/pokemon01/blacephalon_pca_biplot.png)

**Core must-haves:** Jirachi, Quick Ball, Switch, Fire Energy, Fiery Flint, Fire Crystal, Heat Factory, Welder, Oricorio-GX, Blacephalon, Cramorant V, and Energy Retrieval

**Big contenders:** Dedenne-GX, Escape Board, Blacephalon-GX, Ultra Space, Ordinary Rod, Scoop Up Net, and Zacian V

**Common Techs:** Mewtwo, Beast Bringer, and Great Catcher

![Blacephalon card frequency](/images/pokemon01/blacephalon_card_frequency.png)

Looking at our card associations, we see the Jirachi Prism/Mr. Mime/Oranguru combo. I am not surprised that these appeared together. Additionally, we see Beast Bringer implies Adventure Bag and vice versa. This is an obvious pair, but Victini V implying both cards are strange. Lastly, we have Tapu Fini implies Great Catcher. Blacephalon has a lot of must-haves which means there is not going to be a ton of variation between decklists.

![Blacephalon card relationships](/images/pokemon01/blacephalon_rules.png)

### Zacian/Arceus, Dialga, & Palkia Tag Team

Note: Zacian/Arceus, Dialga, & Palkia Tag Team will be referred to as Zacian/ADP.

![Zacian/ADP PCA contributions](/images/pokemon01/zacianADP_pca_contrib.png)

Acro Bike, Scoop Up Net, and Jirachi all contribute a great deal to the variations in ADP Zacian decklists. Looking at our biplot, we see an opposing force to the Jirachi engine with Crushing Hammer and Air Balloon. It appears that Order Pad and Acro Bike were used instead of Scoop Up Nets and Jirachi as well. We do not see much change in the deck between Quarter #3 and Quarter #4. There is only 1 ADP Zacian used at the Invitational.

![Zacian/ADP PCA biplot UPR-RCL](/images/pokemon01/zacianADP_pca_biplot_tours.png)

I decided to include the biplot that includes all the Qualifiers. This shows how Boss’s Orders took over the deck and got rid of Custom Catchers entirely. Also, we can see how the decks managed their engines more. The top half decks went more for the Tag Call engine, whereas the bottom half decks went for an Acro Bike engine with basic Water Energy and Energy Spinners.

![Zacian/ADP PCA biplot UPR-SWSH](/images/pokemon01/zacianADP_pca_biplot_overall.png)

Going back to the UPR – RCL format.

**Core must-haves:** ADP-GX, Dedenne-GX, Metal Energy, Metal Saucer, Professor’s Research, Quick Ball, Switch, Zacian V, and Boss’s Orders

**Big contenders:** Water Energy, Marnie, Energy Spinner, Energy Switch, and Cherish Ball

**Common Techs:** Great Catcher, Tool Scrapper, Chaotic Swell, and Galarian Zigzagoon

![Zacian/ADP card frequency](/images/pokemon01/zacianADP_card_frequency.png)

The relationships among cards are interesting. If you play Air Balloon, we can imply you might also play Eldegoss. Air Balloon is an additional switch card to play in case player start with Eldegoss in their active. Tapu Fini implies you play both Shrine of Punishment and Zamazenta V. Galarian Zigzagoon and Mewtwo both imply you play Scoop Up Net. Both Zigzagoon and Mewtwo require Scoop Up Net for repeated use. Lastly, we see that Crushing Hammer implies Chaotic Swell. This is for the builds that try to disrupt your opponent.

![Zacian/ADP card relationships](/images/pokemon01/zacianADP_rules.png)

## Conclusion

This article is probably very different than what you are used to, and I hope it remained interesting throughout. Ideally, I would like to run this type of analysis on future or past events. A few ideas for future work are decks from when they released to when they rotated or how a deck looks when it first releases compared to after a few tournaments. We saw the latter with PikaRom players opting to play Marnie in Qualifier #4, but not Qualifier #3. I would also like to improve the graphics I used to be more reader friendly. Lastly, I would like to research more methods I can apply this data to.
I would like to thank my friend StarChar for checking over my work and you for reading this article. I enjoyed doing this analysis and writing it up, so I hope I can do this in the future.
