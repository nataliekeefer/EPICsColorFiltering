# EPICsColorFiltering
This includes the color filtering code for the EPICS ISBVI team for the color filtering algorithm

This code is a baseline example of how color filtering works on a still image. The code is setup where you edit in the code the specific .jpg file that you would want to have color filtered. This was temporary and should be updated to have the image be passed in (and what color filtering mode) should be passed in as a an input. 

The code works by first converting the image to greyscale, then converts back to an RGB photo, then changed the colors to the designated color filtering.
