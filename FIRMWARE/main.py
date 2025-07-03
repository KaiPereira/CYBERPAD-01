import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoders import EncoderHandler
from kmk.modules.neopixel import NeoPixel

# Keys
keyboard = KMKKeyboard()

PINS = [board.D2, board.D3, board.D4]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Rotary encoder
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D0, board.D1, None),)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),
]
keyboard.modules.append(encoder_handler)

# Neopixels
neopixel = NeoPixel(pixel_pin=board.D5, pixel_count=14, brightness=0.3)
keyboard.modules.append(neopixel)

# Keymap
keyboard.keymap = [
    [KC.A, KC.W, KC.S]
]

# Start everything
if __name__ == '__main__':
    keyboard.go()

