import matplotlib.image as mpimg
from PIL import Image
import numpy as np

def find_pixel_ave(pixel):
    average = 0
    for i in range(0, len(pixel)):
        average += pixel[i]
    return average / 3

grayscale_image = 'IMG_0821.jpeg'
color_image = 'IMG_3189.jpg'
small_image = 'IMG_0276.jpeg'

image = Image.open(color_image, 'r')
row_length, num_rows = image.size
pix_val = list(image.getdata())
#pix_val = [[0,0,0],[1,1,1],[2,2,2]]
result = []
rows = []
#print(result)
temp = 0
for i in range(0, len(pix_val)):
    if (i % row_length == 0):
        val = int(temp / row_length)
        rows.append(val)
        temp = 0
    else:
        temp += np.average(pix_val[i])

temp = 0
for i in range(0, len(rows)):
    if (i % 9 == 0):
        val = int(temp / 9)
        result.append(val)
        temp = 0
    else:
        temp += rows[i]





print(len(rows))
print(len(result))
print(result)
# print(len(result))
# print(len(rows) / 3)

# temp_row = 0
# for j in range(0, row_length):
#     if (i >= len(pix_val)): break
#     temp_row += np.average(pix_val[i])
#     i += 1
# row_ave = temp_row / row_length
# rows.append(int(row_ave))

# for i in range(0, len(rows)):
#     chord_ave = 0
#     for j in range(0, 3):
#         if (i >= len(rows)): break
#         chord_ave += rows[i]
#         i += 1
#     temp_ave = int(chord_ave / 3)
#     result.append(temp_ave)