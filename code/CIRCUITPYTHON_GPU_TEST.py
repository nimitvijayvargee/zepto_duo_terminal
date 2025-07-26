import supervisor
from displayio import Group, release_displays
from terminalio import FONT
from adafruit_st7735r import ST7735R
from fourwire import FourWire
from adafruit_color_terminal import ColorTerminal
import board
import busio


release_displays()

spi = busio.SPI(clock=board.GP18, MOSI=board.GP19)
tft_cs = board.GP20
tft_dc = board.GP16

display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.GP17)

display = ST7735R(display_bus, width=160, height=128, rotation=90, bgr=True)

main_group = Group()
font_bb = FONT.get_bounding_box()
terminal = ColorTerminal(FONT, 26, 10)
main_group.append(terminal.tilegrid)

green = chr(27) + "[32m"

message = f"{green}Zepto Duo Terminal"
terminal.write(message)
print(message, end="\n\n\n\n\n\n\n\n")

while True:
    pass

