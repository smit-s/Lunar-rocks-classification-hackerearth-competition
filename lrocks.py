# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nOjG017uWg6XIn5a_UvHkLlZb0Th2pZx
"""

from google.colab import drive
drive.mount('/content/drive')

import cv2
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation,Conv2D,MaxPooling2D,Flatten,Dropout
import keras
from sklearn.preprocessing import LabelEncoder  
import numpy as np
import random
from keras.preprocessing.image import ImageDataGenerator

train=pd.read_csv("train.csv")
img_list=train['Image_File']
train_y=np.array(train['Class'])
le = LabelEncoder()
train_y=le.fit_transform(train_y)
train_y = keras.utils.to_categorical(train_y, num_classes=2)
train_x=[]
k=0
for i in img_list:
    train_x.append(cv2.resize(cv2.imread('drive/My Drive/Train Images/'+i),(260,260)))
    print(k)
    k+=1
#print(train_y)
train_x = np.array(train_x).astype('float32')
model = Sequential()
input_shape=(260,260,3) 
model.add(Conv2D(32, (3, 3),activation='relu', input_shape= input_shape))
model.add(Conv2D(32, (3, 3),strides=2, activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(2, activation='softmax'))

model.compile(
loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy']
)

epochs=15
model.fit(train_x,train_y,epochs=epochs,batch_size=32)
model.save("ch.h5")

from keras.models import load_model
import pandas as pd
import numpy as np
import cv2
model = load_model('ch.h5')

train=pd.read_csv("test.csv")
img_list=train['Image_File']
test_x=[]
k=0
for i in img_list:
    test_x.append(cv2.resize(cv2.imread('drive/My Drive/Test Images/'+i),(260,260)))
    print(k)
    k+=1
test_x = np.array(test_x).astype('float32')

clas=[]
clas.append(model.predict_classes(test_x))
print(clas)

ans=[]
for i in range(len(clas[0])):
  if(clas[0][i]==0):
    ans.append('Large')
  else:
    ans.append('Small')
print(ans)
ans=np.array(ans)
nw_c={
      'Image_File':img_list,
       'Class':ans   
}
df=pd.DataFrame(nw_c)
df.to_csv('test.csv',index=False)