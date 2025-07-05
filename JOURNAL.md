## Day 1 - PCB

The Cyber Pad is going to be an extremely futuristic looking macropad.

It's going to be a test of my design skills and just a fun side project I want to build.

I really like the cyberpunk aesthetic and want to make a series of projects that go with the theme, maybe ending up with a cyberpunk themed 3D printer.

Anyways first I'm going to do some drawing and brainstorming on how I want this thing to look.

![[Pasted image 20250627004626.png]]

Anyways this is my main inspiration that I spent some time on, I really like the buttons like this so I think I'm going to leave it like that. I don't want any OLED's or anything because I feel like that ruins the vibe so I'm going simple with a major focus on the design.

Also this design seems quite blocky but the actual thing will be nice and round.

Now let's whip up a quick schematic. I'm trying to stick to best practices possible and I'm going to do the neopixels once I'm done my case!

![[Pasted image 20250627020525.png]]

Now time to do the PCB, took me quite a long time because I was figuring out some footprint and alignment stuff.

![[Pasted image 20250627020624.png]]


## Day 2 - Case

Now I'm going to start modelling the case, I'm going to give about 1cm total on each side just as a placeholder and then I'm going to model the main interior of the bottom I want to go for.

![[Pasted image 20250627115129.png]]

Now that I have this base, I'm going to add some designs along the side. I like the way the graphics card is done, so I'm going to do something similar to that.

Now I kind of want to go with a polarizing like effect which will go with the top of my case:

![[Pasted image 20250627120330.png]]

Now I kind of want to with with some other designs just to fill the space, I'll look into the graphics card design a bit more and kind of go off that. And now I have a really col base to go off of:

![[Pasted image 20250627152612.png]]

Now I'm going to make the shapes a bit more complicated to give it some detail. Now it's looking sick.

![[Pasted image 20250627154255.png]]

Now I really like this style where there's details on the top and bottom, and circles where all the divits are, so I'm going to first add the cool bottom and top details.

![[Pasted image 20250627154432.png]]

And the minor details are really starting to add up.

![[Pasted image 20250627154908.png]]

Now I want some of those extra thin lines. It's starting to look incredible!

![[Pasted image 20250627155635.png]]

Next I added the circles and the logo. The logo is done in inkscape with the Cynata font.

![[Pasted image 20250629003225.png]]

Next I added some walls to it, and then created the plate and top plate.

![[Pasted image 20250629003315.png]]

Now I'm going to start working on the side designs. I want them to be pretty similar to the GPU design and then make the top like the PC.

Anyways next I added the side designs, I've mirrored each side onto the other side for simplicity and it's looking even better now!

![[Pasted image 20250630003341.png]]

Now I kind of have to figure out what I want to do for the top. I really like this style and kind of want to go for something similar. 

![[Pasted image 20250630003446.png]]

I might actually play around with my hackpad colors too, maybe a different color would look better like this green or something. Anyways next I'm going to work on the top. I don't actually have anything in mind, so I'm just going to kind of stick to the same style for now and add more detail later.

![[Pasted image 20250701004438.png]]

And that looks fitting but still now exactly what I want. I really want to see what it would look like if I put a piece of acrylic over the gap now.

This took a long time and I'm sorry I didn't journal all of it, but I added a knob, the acrylic and some text on the bottom. Looking absolutely insane now.

![[Pasted image 20250701231210.png]]

But we are not finished, nowhere near the craziness I want. Next I'm going to add all the extra little things to give it dimension. 

![[Pasted image 20250703001012.png]]

I also refined the design a bit so it's easier to print and it looks pretty good. 

Next I need to customize the PCB so that it looks rlly cool inside of the case. I wanna go for like exposed trace with cyberpunk drawings style. I used the case DXF as a reference point, and then used figma to draw the lines. Then I just add the image properly scaled to kicad.

![[Pasted image 20250703001123.png]]

Now I completely forgot to add the neopixels so lemme do that real quick.

![[Pasted image 20250703010923.png]]

Rewired + new schematic.

![[Pasted image 20250703010949.png]]

Next I did the firmware. It was really simple, just some python with KMK.

![[Pasted image 20250703152029.png]]

Next I completely forgot but I needed a USB port so I added that in.

![[Pasted image 20250703152156.png]]

