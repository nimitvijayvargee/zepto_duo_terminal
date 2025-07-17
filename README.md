# zepto_duo_terminal
An old school-style VGA output terminal PC!
The PC is powered by two Raspberry Pi Picos. One of the Pico handles the main processing and the keyboard matrix (CPU Pico) and the other Pico handles the VGA Output and the conversion between text to pixels (GPU Pico). The Picos can be replaced with any Pin-compatible version.

## VGA DAC
The GPU Pico is connected to a Resistor DAC that outputs VGA compatible voltage values. There are 5 bits of resolution for each colour channel (RGB555), which allows for 32K colours. The values for the DAC are as 500, 1K, 2K, and 5.1K (commonly used values).
![VGADAC](images/image-0.png)

## Keyboard Matrix 
The Keyboard matrix is composed of 8 Rows and 8 Columns, following an ortholinear keyboard layout. Sticky (toggle) keys is also enabled by default to make using the keyboard easier. The keyboard features a "Special" key instead of the commly used Fn or GUI keys. The keycaps are all custom becuase of their specific use case and the unorthodox ortholinear layout.

# Pictures
![Case](images/image-1.png)
![Schematic](images/image-2.png)
![PCB](images/image-3.png)