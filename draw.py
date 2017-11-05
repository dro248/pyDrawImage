import Image

# Create a new image with:
#   --> RGB values
#   --> WIDTH: 100px
#   --> HEIGHT: 200px
im = Image.new('RGB', (100, 200))

# Set pixels values with tuples
#   1st pixel: (255,0,0) is RED
#   2nd pixel: (0,255,0) is GREEN
#   3rd pixel: (0,0,255) is BLUE
im.putdata([(255,0,0), (0,255,0), (0,0,255)])

# Display the image
im.show()

# Save image to file
im.save('test.png')

