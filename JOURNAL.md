---
title: "Zepto Duo Terminal"
author: "nimit vijayvargee"
description: "An all-in-one Terminal PC with two Pi Picos that outputs VGA, all with a a built-in keyboard!"
created_at: "2025-06-24"
---


# Day 1 - 25th June
Created a sketch and layout for the project, mostly brainstorming

# Day 2 - 26th June
Time Spent: 2hrs <br>
Started reseasrching into VGA with the Pi Pico, and read the Hardware Design docs for VGA pinouts and connections.
The RP2040 Hardware Design docs dedicate a section to the VGA interface over PIO Assembly. After doing some research, I found out about `scanvideo`, which is a Pico SDK PIO Library for implementing scanline video output such as DVI and VGA, which is exactly what I need.
![image](https://github.com/user-attachments/assets/22d4186a-1214-42c3-98ee-cb37587cb5e1)

# Day 3 - 27th June
Time Spent: 2hrs <br>
Designed the built-in keyboard, plan to use basic MX keys with an ortholinear layout. Also included sticky-keys indicators because holding keys simultaneously may be difficult to implement. Also laid out the keyboard both in Keyboard Layout Editor. I then added everything to the schematic which was very easy due to the ortholinear keyboard layout. I managed to connect the GPU and CPU Picos over a data bridge, which I intend to be UART.<br>
![image](https://github.com/user-attachments/assets/2fd204d0-24e8-4d89-bb4f-af92ed34ea6a)

Time Spent: 3hrs <br>
Today I completed routing the schematic. I also managed to finish laying out the keyboard design and connected all the rows and columns. I then spent some time choosing the footprints for all the components. This PCB is intended to be hand-soldered so I chose THT footprints for the Diodes, Resistors and the LEDs. Because of the custom layout, I was unable to find any useful keycaps (I mean who makes a 1u shift key and a 1.5u escape key), so I will be 3D printing the keycaps. I also designed a few sketches for how I want the case to look like. I want it to be a two-part case, with the top part being acrylic and the bottom part being 3D printed. This will make the green PCB look very cool and show all the various components.
![image](https://github.com/user-attachments/assets/d66152c9-81dc-4279-b856-9928c2619414)
![image](https://github.com/user-attachments/assets/72293653-ed0e-4629-940d-90312abf8f7b)

# Day 4 - Day 8 -- 28th June - 1st July 
Time Spent: 8hrs
I placed the footprints into my PCB editor and started moving them around. I added M4 Screw holes for the PCB to attach to the case. I added a header for an expansion slot for later use although I might scrap the feature altogether. I laid out the matrix and the diodes using the MX Grid trick (set your grid size to match the MX size). I also added a little bit of silkscreen to make the PCB have some personality.
![image](https://github.com/user-attachments/assets/96a6e0e4-e6bc-4a8a-81ed-d1086a50032c)
![image](https://github.com/user-attachments/assets/19eb0b2d-b567-4ec4-a493-e1af88aa21c8)

# Day 9 - Day 10 -- 2nd July - 3rd July
Time Spent: 3hrs
I rerouted the PCB and moved around the components to make it more compact. I also planned out the keycaps to print. I initially planned to use a 6.25u Spacebar, but since it is the only key that needs that stabilizer, I decided to use a 7u spacebar instead, because I had an extra 7u wire. I managed to redo the layout and routing to accommodate the 7u, which wasn't as hard. I also considered printing the keycaps in offwhite PLA but it isn't as easy to find as black or white, so I will stick to those for now.

# Day 11 - Day 12 -- 10th July - 11th July
Time Spent: 3hrs <br>
Returned to this project after some time. On comparing prices across websites, it was much cheaper to reroute the main board to follow a different layout. The board is now 400x120 (mm) and has more or a Pi500 vibe to it. Most of the layout and routing could be reused but I did decide to redo the resistors for the VGA and remove the expansion card slot
![image](https://github.com/user-attachments/assets/56397551-1b81-493f-ac31-81174a9acc32)
![image](https://github.com/user-attachments/assets/f5d9a3f3-b651-4188-8a3e-0e46fbdf84e0)

# Day 13 - 14th July
Time Spent: 2hrs <br>
I started working on the CAD. I first sketched out the PCB with the mounting holes then created an area arount it. I extruded everything to a reasonable size and created some renders. I just need to make the keycpas now.
![image](https://github.com/user-attachments/assets/f8805421-536e-4e49-b77d-79eb0da3ae2f)
# Day 14 - 15 -- 15th - 16th July
Time Spent: 2hrs <br>
I spent this day just designing the custom keycaps. It was difficult but  when I finished my first 1u keycap, I got into the pace to finish the rest of the keycaps too.

# Day 15 - 27th July
Time Spent: 1hr <br>
I worked on the code. I am going to use the `adafruit_color_terminal` library for circuitpython to create the terminal, but for the video output I need to decide between `scanvideo` (C SDK) or writing it in PIO-ASM on Circuitpython. I did some testing of the code on a spare ST7735R screen I had lying around. Afterwards, I can do it properly on a monitor.
I also made a render for the updated case!
<img width="1443" height="820" alt="image" src="https://github.com/user-attachments/assets/2c2cc216-a745-495a-9cde-2df3a3c901c4" />
