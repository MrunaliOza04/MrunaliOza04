from PIL import Image, ImageDraw, ImageFont
import json, os

with open(".github/tictactoe/board.json") as f:
    data = json.load(f)

board = data["board"]

# image size
size = 300
cell = size // 3
img = Image.new("RGBA", (size, size), (18,18,18,255))
d = ImageDraw.Draw(img)

# try to load a font
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
except:
    font = ImageFont.load_default()

# draw grid lines
line_color = (80, 80, 80, 255)
d.line((cell, 0, cell, size), fill=line_color, width=4)
d.line((2*cell, 0, 2*cell, size), fill=line_color, width=4)
d.line((0, cell, size, cell), fill=line_color, width=4)
d.line((0, 2*cell, size, 2*cell), fill=line_color, width=4)

# draw X / O
for r in range(3):
    for c in range(3):
        val = board[r][c]
        x = c * cell + cell//2
        y = r * cell + cell//2
        if val != "":
            d.text((x, y), val, fill="white", font=font, anchor="mm")

img.save(".github/tictactoe/board.png")
print("Board updated")
