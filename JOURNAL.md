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
![image](https://github.com/user-attachments/assets/22d4186a-1214-42c3-98ee-cb37587cb5e1)

# Day 3 - 27th June
Time Spent: 2hrs <br>
Designed the built-in keyboard, plan to use basic MX keys with an ortholinear layout. Also included sticky-keys indicators because holding keys simultaneously may be difficult to implement. Also laid out the keyboard both in Keyboard Layout Editor and KiCad. Decided to use a UART bus on 152Kbps. <br>
![image](https://github.com/user-attachments/assets/2fd204d0-24e8-4d89-bb4f-af92ed34ea6a)

Time Spent: 3hrs <br>
Completed routing the schematic. Also worked a bit on the rows and columns for the keyboard. Spent some time choosing the footprints for all the components to tie together. This PCB is intended to be hand-soldered so I chose THT footprints for the Diodes, Resistors and the LEDs. I chose a retro style ortholinear layout but it is quite difficult to find blank keycaps to match. I also started sketching a small diagram of how i hope for this project to turn out!
![image](https://github.com/user-attachments/assets/d66152c9-81dc-4279-b856-9928c2619414)
![image](https://github.com/user-attachments/assets/72293653-ed0e-4629-940d-90312abf8f7b)

# Day 4 - Day 8 -- 28th June - 1st July 
Time Spent: 8hrs
Placed components and routed the PCB. Chose the mounting holes (M4) and added an expansion slot to the GPU to add any future devices (LCD, Speaker, etc.). Expansion slot will probably require recompiling the C-SDK to work with the GPU but the CPU didn't have enough open GPIO slots (damn matrix) so there wasn't another option. 
![image](https://github.com/user-attachments/assets/96a6e0e4-e6bc-4a8a-81ed-d1086a50032c)
![image](https://github.com/user-attachments/assets/19eb0b2d-b567-4ec4-a493-e1af88aa21c8)

# Day 9 - Day 10 -- 2nd July - 3rd July
Time Spent: 3hrs
Rerouted parts of the PCB and added mounting holes. Did research on printing and painting PLA (might get offwhite to give a retro vibe). <br>
Ref:<br> ![image](https://github.com/user-attachments/assets/63e5d894-7a66-479e-b60f-5607c99c3f9e) <br>
Also added some silkscreen details to be easier to read. Will add silkscreen art tommorow.

# Day 11 - Day 12 -- 10th July - 11th July
Time Spent: 3hrs <br>
Returned to this project after some time. On comparing prices across websites, it was much cheaper to reroute the main board to follow a different layout. The board is now 400x120 (mm) and has more or a Pi500 vibe to it. Most of the layout and routing could be reused but I did decide to redo the resistors for the VGA and remove the expansion card slot
![image](https://github.com/user-attachments/assets/56397551-1b81-493f-ac31-81174a9acc32)
![image](https://github.com/user-attachments/assets/f5d9a3f3-b651-4188-8a3e-0e46fbdf84e0)

# Day 13 - 14th July
Time Spent: 2hrs <br>
Fixed keyboard layout to use a 7u spacebar (ortholinear) and worked on the case. The case is going to be two part, with an acrylic removabale plate on top for view into the body. The main case is going to be 3d printed in whtite. I am only remaining with the keycaps before i can start the software!
![image](https://github.com/user-attachments/assets/f8805421-536e-4e49-b77d-79eb0da3ae2f)


