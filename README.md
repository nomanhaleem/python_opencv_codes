# python_opencv_codes
This repository contains some codes I had developed for OpenCV application in Python.

The first code proposes a simple algorithm for producing well known Haar-Cascade models using multiple positive images. 
Haar-Cascade technique, which is based on Viola-Jones algorithm, is an excellent method of object detection. The implementation of the algorithm in OpenCV is simple and straight forward. If you have got one positive image, you can apply data augmentation techniques using opencv createsamples function, followed by developing a vector file that contains information about the object of interest in augemented images to allow the model learn on certain features. However, the task becomes substantially difficult if you got more than one positive image that you intend to augment followed by producing the the vector file. This code serves exactly that purpose.

