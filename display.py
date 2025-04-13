import board
from datetime import datetime
import displayio

import terminalio
import time


# can try import bitmap_label below for alternative

from adafruit_display_text import label

from i2cdisplaybus import I2CDisplayBus


import adafruit_displayio_sh1107


displayio.release_displays()

# oled_reset = board.D9


# Use for I2C

i2c = board.I2C()  # uses board.SCL and board.SDA

# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

display_bus = I2CDisplayBus(i2c, device_address=0x3C)


# SH1107 is vertically oriented 64x128

WIDTH = 128

HEIGHT = 64

BORDER = 2


display = adafruit_displayio_sh1107.SH1107(display_bus, width=WIDTH, height=HEIGHT)


# Make the display context

splash = displayio.Group()

display.root_group = splash


color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)

color_palette = displayio.Palette(1)

color_palette[0] = 0xFFFFFF  # White


bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

splash.append(bg_sprite)


# Draw a smaller inner rectangle in black

inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)

inner_palette = displayio.Palette(1)

inner_palette[0] = 0x000000  # Black

inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)

splash.append(inner_sprite)


# Draw some label text

text_area_upper = label.Label(terminalio.FONT, text="Platzhalter", color=0xFFFFFF, scale=2, x=8, y=16)
splash.append(text_area_upper)

text_area_lower = label.Label(terminalio.FONT, text="Platzhalter", color=0xFFFFFF, scale=2, x=8, y=48)
splash.append(text_area_lower)

def refresh_display():
    splash.hidden = False
    splash.hidden = True

def set_text_upper(new_text):
    text_area_upper.text = new_text
    refresh_display()
    
def set_text_lower(new_text):
    text_area_lower.text = new_text
    refresh_display()

