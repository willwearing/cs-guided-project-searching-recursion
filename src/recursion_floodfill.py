import time
​
# Floodfill
​
image_str = [
    "#########################",
    "#     ####              #",
    "#    #    #             #",
    "#   #    #              #",
    "#   #    ####           #",
    "#   #        #     #### #",
    "#   #########      #   ##",
    "#               #  #    #",
    "#              # ###    #",
    "#             #      ####",
    "#              ###   #  #",
    "#########################"
]
​
# make the image lists from the strings
image = []
for i in image_str:
    image.append(list(i))
​
def print_image():
    for i in image:
        print("".join(i))
​
def flood_fill(row, col, char):
    if image[row][col] != ' ':
        return
​
    image[row][col] = char
​
    print_image()
    time.sleep(0.5)
​
    flood_fill(row-1, col, char)  # up
    flood_fill(row+1, col, char)  # down
    flood_fill(row, col-1, char)  # left
    flood_fill(row, col+1, char)  # right
​
​
flood_fill(4, 6, "*")
​
flood_fill(5, 16, ".")
​
print_image()