# storing images as numpy array
import imageio.v2 as imageio # pip install imageio
import numpy as np
import matplotlib.pyplot as plt

pic = imageio.imread("demo_2.jpg")

print(type(pic))

print(pic.shape)

plt.figure(figsize=(12,10))
plt.imshow(pic)
plt.show()

print(pic[0,959,:])

# [72,86,53] * [0.299,0.587,0.114] = [72*0.299 + 86*0.587 + 53*0.114]
# [0.299,0.587,0.114] - factor used by GNU Image Manipulation Program 
gray = lambda img: np.dot(img[...],[0.299,0.587,0.114])

wb = gray(pic)

plt.figure(figsize=(12,10))
plt.imshow(wb, cmap=plt.get_cmap(name='gray'))
plt.show()
