from PIL import Image
img = Image.open('resources/images/map4.png').convert('LA')
img.save('greyscale.png')