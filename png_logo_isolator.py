#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:37:01 2020

@author: Tyler Higgs
"""

from PIL import Image

def isWhite(pixel):
    '''
    input: tuple representing the rgb and alpha values for a single pixel
           in the form of (red, green, blue, alpha)
    returns True if a pixel is white and False otherwise
    '''
    return pixel[0] > 100 and pixel[1] > 100 and pixel[2] > 100

def coordinates(index, mx,my):
    '''
    inputs: the index of the pixel of an image represented by a 1D array
            half the width
            half the height
    returns the x,y coordinates of the pixel
    '''
    width = mx * 2
    height = my * 2
    return index % width, int(index/height)

def distanceFromCenter(index,mx,my):
    x,y = coordinates(index,mx,my)
    return ((mx-x)**2 + (my-y)**2)**0.5





def clearPixelsOutsideInnerCircle(fileName,radius, pixels_right_of_center, pixels_down_of_center):
    im = Image.open(fileName)
    print(im.getdata().size)
    width,height = im.getdata().size
    pixels = list(im.getdata())
    
    mx = width/2 + pixels_right_of_center
    my = height/2 + pixels_down_of_center

    for i in range(len(pixels)):
        if isWhite(pixels[i]):
            if distanceFromCenter(i,mx,my) > radius:
                pixels[i] = (0,0,0,0)
    img = Image.new("RGBA",(width,height)) # makes a black image (list of (0,0,0)'s) of the correct size
    img.putdata(pixels) #put in new pixels 
    
    img.save(fileName[:-4] + "-1" + ".png")
    return
    
    
fileName = "AppLogo.png"
clearPixelsOutsideInnerCircle(fileName,210,0,25)


