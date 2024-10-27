import numpy as np
import imageio as img
import matplotlib.pyplot as plt

image = img.imread("https://images.unsplash.com/photo-1500964757637-c85e8a162699?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8M3x8fGVufDB8fHx8fA%3D%3D")

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

imgRed = np.zeros_like(image)
imgRed[:,:,0] = red

plt.figure(figsize=(10, 15))

plt.subplot(4, 1, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(4, 1, 2)
plt.imshow(imgRed)
plt.title("Red Channel")

plt.subplot(4, 1, 3)
plt.imshow(imgGreen)
plt.title("Green Channel")

plt.subplot(4, 1, 4)
plt.imshow(imgBlue)
plt.title("Blue Channel")

plt.show()
