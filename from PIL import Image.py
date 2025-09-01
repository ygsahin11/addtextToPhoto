from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
img = Image.open('house.png')
draw = ImageDraw.Draw(img)

draw.rectangle((20, 20, 60, 60), fill='blue')
text = input("Dikdörtgenin içine yazılacak metni girin: ")
font = ImageFont.load_default() # type: ignore
draw.text((25, 35), text, font=font, fill='white')

img.show()
img.save('house_with_rectangle.png')
img.close()