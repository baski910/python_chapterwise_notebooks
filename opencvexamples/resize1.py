import cv2  
  
img = cv2.imread('demo_2.jpg', cv2.IMREAD_COLOR)  
scale = 60  
width = int(img.shape[1] * scale / 100)  
height = int(img.shape[0] * scale / 100)  
dim = (width, height)  
# resize image  
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)  
  
print('Resized Dimensions : ', resized.shape) 
#plt.figure(figsize=(12,10))
#plt.imshow(resized)
#plt.show()

cv2.imshow("Resized image", resized)  
cv2.waitKey(0)  
cv2.destroyAllWindows() 