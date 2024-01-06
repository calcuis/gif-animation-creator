from PIL import Image

input = ['1.png', '2.png', '3.png']
output = 'output.gif'

frames = []
for file in input:
    img = Image.open(file)
    frames.append(img)

frames[0].save(output, save_all=True, append_images=frames[1:], duration=500, loop=0)
