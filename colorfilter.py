# code written by Natalie Keefer
# color_filter.py
# Color filtering functions for the magnifier project
# last updated 4/14/2021
import cv2
import numpy as np
import sys
from PIL import Image 
import PIL 

def filter(option):    
    print ("Filtering color for frame...")
    #Turning image into grayscale
    im = np.array(Image.open('colorfulimages.jpg').convert('L')) #changing this to the .jpg wanted 
    cv2.imwrite("translatedBW.jpg",im)
        
    if option == "BlueonYellow":
        frame = np.array(Image.open('translatedBW.jpg').convert('RGB')) #this line is converting the image from binary back to rgb
        #turning image where black to blue
        for i in range(128):
            frame[np.where((frame==[i,i,i]).all(axis=2))] = [i/2+220,i/2+60,i/4+20]
        #turning image where white to yellow
        for i in range(128):
            frame[np.where((frame==[255-i,255-i,255-i]).all(axis=2))] = [i/12+52,i/6+229,i/10+235]
            
    if option == "YellowonBlue":
        frame = np.array(Image.open('translatedBW.jpg').convert('RGB')) #this line is converting the image from binary back to rgb
        #turning image where black to yellow
        for i in range(120):
            frame[np.where((frame==[i,i,i]).all(axis=2))] = [i/12+52,i/6+229,i/10+235]
        #turning image where white to blue
        for i in range(120):
            frame[np.where((frame==[255-i,255-i,255-i]).all(axis=2))] = [i/6+220,i/3+60,i/+20]
    return frame

#change the BlueonYellow to YellowonBlue to change the option
im = filter('BlueonYellow')
cv2.imwrite("translated.jpg",im)