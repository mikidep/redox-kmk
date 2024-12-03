import board
from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()

keyboard.row_pins = (
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
)
keyboard.col_pins = (
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.matrix = MatrixScanner(
    row_pins=keyboard.row_pins,
    column_pins=keyboard.col_pins,
    columns_to_anodes=keyboard.diode_orientation,
    interval=0.03,
)

name = str(getmount("/").label)

split = Split(
    data_pin=board.GP1,  # RX
    data_pin2=board.GP0,  # TX
    uart_flip=False,
    split_target_left=False,
    debug_enabled=True,
    split_flip=False,
    split_side=(SplitSide.LEFT if name.endswith("L") else SplitSide.RIGHT),
)
keyboard.modules.append(split)
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

# fmt: off
keyboard.keymap = [
  [
      #         QWERTY
      KC.NO,    KC.F1,     KC.F2,     KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,   KC.F11,   KC.F12,  KC.QUOTE,
      KC.TAB,   KC.Q,      KC.W,      KC.E,    KC.R,    KC.T,    KC.F6,   KC.BSPC, KC.Y,    KC.U,    KC.I,     KC.O,     KC.P,    KC.EQUAL,
      KC.ESC,   KC.A,      KC.S,      KC.D,    KC.F,    KC.G,    KC.LGUI, KC.NO,   KC.H,    KC.J,    KC.K,     KC.L,     KC.NO,   KC.MINUS ,
      KC.GRAVE, KC.BSLASH, KC.Z,      KC.X,    KC.C,    KC.V,    KC.LALT, KC.NO,   KC.B,    KC.N,    KC.M,     KC.COMMA, KC.DOT,  KC.SCOLON,
      KC.MO(1), KC.MO(2),  KC.BSLASH, KC.LGUI, KC.LALT, KC.LSFT, KC.LCTL, KC.ENT,  KC.SPC,  KC.RALT, KC.SLASH, KC.LBRC,  KC.RBRC, KC.NO,
  ],
  [
      #         NUMPAD
      KC.NO,    KC.NO,     KC.NO,     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,    KC.NO,    KC.NO,   KC.NO,
      KC.NO,    KC.NO,     KC.NO,     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.N7,   KC.N8,    KC.N9,    KC.NO,   KC.NO,
      KC.NO,    KC.NO,     KC.NO,     KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.NO,   KC.NO,   KC.N4,   KC.N5,    KC.N6,    KC.NO,   KC.NO,
      KC.NO,    KC.NO,     KC.NO,     KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.NO,   KC.NO,   KC.N1,   KC.N2,    KC.N3,    KC.NO,   KC.NO,
      KC.NO,    KC.NO,     KC.NO,     KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.TRNS, KC.N0,    KC.NO,    KC.NO,   KC.NO,
  ],
  [
      #         ARROWS
      KC.NO,    KC.NO,     KC.NO,     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.MUTE, KC.VOLD, KC.VOLU,  KC.PSCR,  KC.NO,   KC.NO,
      KC.NO,    KC.NO,     KC.NO,     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.DEL,  KC.NO,   KC.NO,   KC.NO,    KC.NO,    KC.NO,   KC.NO,
      KC.NO,    KC.NO,     KC.NO,     KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.NO,   KC.LEFT, KC.DOWN, KC.UP,    KC.RIGHT, KC.NO,   KC.NO,
      KC.NO,    KC.NO,     KC.NO,     KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,    KC.NO,    KC.NO,   KC.NO,
      KC.NO,    KC.NO,     KC.NO,     KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,    KC.NO,    KC.NO,   KC.NO,
  ],
]
# fmt: on
if __name__ == "__main__":
    keyboard.go()
