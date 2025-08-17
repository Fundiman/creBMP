from PIL import Image, ImageGrab
import os

screen = ImageGrab.grab()
screen_width, screen_height = screen.size

bmp = Image.new("RGB", (screen_width, screen_height), "black")

icon_path = "icon.png"
if not os.path.exists(icon_path):
    raise FileNotFoundError(f"{icon_path} not found!")

icon = Image.open(icon_path).convert("RGBA")

x = (screen_width - icon.width) // 2
y = (screen_height - icon.height) // 2

bmp.paste(icon, (x, y), icon)

bmp.save("splash.bmp", "BMP")
