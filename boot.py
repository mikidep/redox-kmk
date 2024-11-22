import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP13,  # column
    source=board.GP2,  # row
    midi=False,
    mouse=False,
    storage=False,
    cdc_control=False,
    boot_device=0,
    usb_id=("KMK Keyboards", "PicoDox"),
)
