import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from sklearn.cluster import KMeans

os.chdir('/home/hahaha/Downloads')

image1 = cv2.imread('/home/hahaha/Downloads/AgeGender/image.png')
image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

filt = [[1,0,-1],
         [2,0,-2],
         [1,0,-1]]
filt2 = [[1,2,1],
         [0,0,0],
         [-1,-2,-1]]

col = signal.correlate2d(image, filt)
row = signal.correlate2d(image, filt2)
gray = image + np.random.rand(*image.shape) * 10
smooth = cv2.GaussianBlur(image, (3,3),0)

mean = np.mean(smooth)
k = image.reshape(-1,1)
kmeans = KMeans(n_clusters=2).fit(k)
pic2show = kmeans.cluster_centers_[kmeans.labels_]
cluster_pic = pic2show.reshape(smooth.shape[0], smooth.shape[1])

plt.subplot(2,3,1)
plt.imshow(image, cmap='gray')

plt.subplot(2,3,2)
plt.imshow(col, cmap='gray')

plt.subplot(2,3,3)
plt.imshow(row, cmap='gray')
