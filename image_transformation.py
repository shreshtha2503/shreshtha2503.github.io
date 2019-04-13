
from PIL import Image

my_image = Image.open("assets/photo.jpg")
image_pixels = my_image.load()
width, height = my_image.size
for i in range(0, width):
    for j in range(0, height):
        corrent_pixel = image_pixels[i,j]
        blue_component = image_pixels[i,j][0]
        red_component = image_pixels[i,j][0]
        green_component = image_pixels[i,j][0]
        gray_value = (int)(0.07 * blue_component + 0.72 * green_component + 0.21 * red_component)
        image_pixels[i,j] = (gray_value, gray_value, gray_value, 255)
        if(gray_value < 50):
            new_color = (184, 232, 201, 255)
        elif(gray_value < 100):
            new_color = (188, 255, 248, 255)
        elif(gray_value < 125):
            new_color = (240, 255, 234, 255)
        elif(gray_value < 150):
            new_color = (255, 238, 167, 255)
        elif(gray_value < 200):
            new_color = (255, 255, 203, 255)
        image_pixels[i,j] = (new_color[0], new_color[1], new_color[2], 255)

my_image.show()
