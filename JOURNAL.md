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


