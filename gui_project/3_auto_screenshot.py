import time
from PIL import ImageGrab

time.sleep(5) # code is executed 5 seconds after to allow the user to prepare

# saves 10 images in total, one in every 2 seconds
for i in range(1, 11): 
    img = ImageGrab.grab() # gets current screen image (screenshot)
    img.save('image{}.png'.format(i)) # saves the image (image1.png ~ image10.png)
    time.sleep(2)

