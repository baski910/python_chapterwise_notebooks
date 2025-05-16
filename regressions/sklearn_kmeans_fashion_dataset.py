import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from tensorflow import keras


# Load the Fashion-MNIST dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

#fashion_mnist = tf.keras.datasets.fashion_mnist

#(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

x_train.shape  # 60000,28,28

# plot one image from test data
plt.figure()
plt.imshow(x_train[0])
plt.show()

# reshape and scale the data to plot it as black and white image
x_train_flat = x_train /255.0
x_test_flat = x_test / 255.0


# plottting images with labels

plt.figure(figsize=(10,10))
for i  in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel(class_names[y_train[i]])
    plt.imshow(x_train_flat[i],cmap=plt.cm.binary)
plt.show()

# reshape and scale the data as expected by KMeans model (model expects 2 dimensional array)
x_train_flat = x_train.reshape(len(x_train), -1) / 255.0
x_test_flat = x_test.reshape(len(x_test), -1) / 255.0

x_train_flat.shape  # 60000, 784

# traing the model
kmeans = KMeans(n_clusters=10,random_state=42,n_init=10)
kmeans.fit(x_train_flat)
y_kmeans_train = kmeans.predict(x_train_flat)

# Assign labels
labels = np.zeros(10, dtype=int)
for i in range(10):
    mask = (y_kmeans_train == i)
    labels[i] = np.argmax(np.bincount(y_train[mask]))
    
print(labels)

# Predict on test data
y_kmeans_test = kmeans.predict(x_test_flat)
y_pred_test = np.array([labels[i] for i in y_kmeans_test])

# reshape for plotting
x_test_t = x_test/255.0

# use the predicated lables for classifying the images
plt.figure(figsize=(10,10))
for i  in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel(class_names[y_pred_test[i]])
    plt.imshow(x_test_t[i],cmap=plt.cm.binary)
plt.show()


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred_test)
print(f"Accuracy: {accuracy}")
