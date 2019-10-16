#Approach and Steps for implementation

Approach-

Used a CNN for classification of images.

Used keras to implement this network.

Encoded the class labels

Initially, reduced dimension of images to 260*260 

Used 6 convolution layers each with 32 filters with 5 Max pool layers placed in alternative manner.

Dense layer with 512 neurons added at end.

Used adam optimizer and crossentropy as loss function

Steps to run the script

List of python modules used- pandas, tensorflow, sklearn, numpy

Development enviroment- Google Colab

****Steps to run script****
I have added both scripts .py and .ipynb to zip file 

For running on google colab just add all trianing images to same folder and upload it to drive and also upload test images to drive.

Upload train.csv and test.csv to colab directly.

finally run each block of code one after other

Finally the test.csv is the file that contains the answer.

Also added the saved model named 'ch.h5'. User can directly load it and test on the test dataset.

Both train and test scripts are in same file.
