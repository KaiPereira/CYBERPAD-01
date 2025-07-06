# CYBERPAD-01

![Journal Image](journal/Pasted%20image%2020250705163430.png)

The CYBERPAD-01 is a cyberpunk inspired macropad with 3 keys, a rotary encoder, and a whole lotta silkscreen and neopixels. It uses KMK firmware and was meant to serve as a learning opportunity for PCB's, CAD and rendering. 
## Custom Features
- Custom lasercut acrylic top panel
- EC11 Rotary Encoder for anything really
- 3 Keys to program to heart's content
- 14 SK6812 MINI-E LEDs for backlight and and diffusion
- Cyberpunk inspired case for maximum aesthetic
-  Exposed PCB design with custom silkscreen
## CAD Design

The laser cut acrylic panel is held together using minimalist bolts and spacers attached to the top plate. The actual case is designed so that everything can fit together seamlessly without using any screws or bolts for minimalism and aesthetics while still being secure.

![Pasted image 20250705183413.png](journal/Pasted%20image%2020250705183413.png)

![Pasted image 20250705183502.png](journal/Pasted%20image%2020250705183502.png)

It comprises of 3 separate 3D printed parts though, the bottom plate/aesthetic walls, the walls, and the top plate, with the 4th part being the acrylic top panel, so it's a bit difficult to print, but manageable. *Made in Onshape*

## PCB Design

The PCB was designed using KiCad and then I used Figma and the KiCad image converter for creating the silkscreen layers. I actually imported the case design into KiCad so I could use it as reference for the silkscreen which turned out really well.

![Pasted image 20250705183935.png](journal/Pasted%20image%2020250705183935.png)
![Pasted image 20250705184029.png](journal/Pasted%20image%2020250705184029.png)

## Firmware

The CYBERPAD-01 uses KMK firmware (written in Python) and was relatively straightforward.
- The rotary encoder changes volume
- The keys just act as VIM macro's

I'll probably make it a bit more complicated in the future, but I think it's kind of handy to have a macropad for some really complicated VIM stuff.

## Bill of Materials (BOM)

Here's everything you'll need to build the CYBERPAD-01:
- 3x Cherry MX Switches
- 3x Keycaps of your choice (I would personally suggest black ones)




