from PIL import Image, ImageGrab
import os

screen = ImageGrab.grab()
screen_width, screen_height = screen.size

bmp = Image.new("RGB", (screen_width, screen_height), "black")

icon_path = "icon.png"
if not os.path.exists(icon_path):
    raise FileNotFoundError(f"{icon_path} not found!")

icon = Image.open(icon_path)
icon_width, icon_height = icon.size

x = (screen_width - icon_width) // 2
y = (screen_height - icon_height) // 2

bmp.paste(icon, (x, y), icon if icon.mode == 'RGBA' else None)

bmp.save("splash.bmp", "BMP")
