import keypad
import digitalio
import board
import busio

# This part of the code just takes the input from a keypad attached and
# outputs it via a UART bus into another pico (the GPU) which handles
# displaying it. This is testing code.
# The main code will involve passing the key-inputs through a REPL or
# text-based code editor, which is passed to the GPU. That way, the code
# can be executed on this device, while the output is transferred to the
# other video handler.

uart = busio.UART(tx=board.GP16, rx=board.GP17, baudrate=9600)
km = keypad.KeyMatrix(
    row_pins=(board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8),
    column_pins=(board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16),
    columns_to_anodes=False
)
map = [
    ["esc", "1", "2", "3", "4", "5", "6", "7", "8"],
    ["tab", "q", "w", "e", "r", "t", "y", "u", "i"],
    ["caps","a", "s", "d", "f", "g", "h", "j", "k"],
    ["shift","z","x", "c", "v", "b", "n", "m", "<"],
    ["ctrl","space", "ctrl", "special", "alt", "up", "down", "left", "right"],
    ["9", "0","-","=","back"],
    ["o", "p", "[","]","\\", "|" ],
    ["l",";","\"","enter"],
    [">", ",", ".", "?", "`", "shift"]
]
while True:
    event = km.events.get()
    if event and event.pressed:
        row = event.key_number // len(km.column_pins)
        col = event.key_number % len(km.column_pins)
        keyname = map[col][row]
        uart.write((keyname + "\n").encode("utf-8")) # output to UART bus for GPU to handle
