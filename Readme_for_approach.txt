Approach-

Basically I have used a CNN for classification of images.

CNN are best for image classification

I have used keras to implement this network.

Encoded the class labels

Initially I reduced dimension of images to 260*260 because all images were not fitting in meory and system was crashing after that I used 6 convolution layers each with 32 filters with 3 Max pool layers placed in alternative manner.

Also, a dense layer with 512 neurons added at end.

Used adam optimizer and crossentropy as loss function

Steps to run the script

List of python modules used- pandas, tensorflow, sklearn, numpy

Development enviroment- Google Colab

****Steps to run script****
I have added both scripts .py and .ipynb to zip file 

For running on google colab just add all trianing images to same folder and upload it to drve  and also upload test images to drive.

Upload train.csv and test.csv to colab directly.

finally run each block of code one after other

Finally the test.csv is the file that contains the answer.