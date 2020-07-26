#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:37:01 2020

@author: Tyler Higgs
"""

from PIL import Image
    
    
fileName = "AppLogo.png"
clearPixelsOutsideInnerCircle(fileName,210,0,25)

def clearPixelsOutsideInnerCircle(fileName,radius, pixels_right_of_center = 0, pixels_down_of_center = 0):
    '''
    
    Sets the alpha values of all pixels outside of an inner circle with a specified
    radius and coordinates to 0 of a given png image. This means that if a logo is 
    represented as a png but is surrounded by white pixels instead of transparent ones, 
    this function can make the surrounding white pixels transparent, while keeping the white
    pixels in the logo solid. 
    
    Inputs: 
        fileName: string name of the image file with the .png extension
        radius: the radius in number of pixels within which pixles will not 
                be affected. White pixels outside this radius get their alpha
                values set to 0
        pixels_right_of_center: Number of pixels right of the center that the 
                protected circle should have its center
        pixels_down_of_center: Number of pixels down from the center that the 
                protected circle should have its center  
    '''
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
    '''
    Inputs: 
        index: the index of the pixel in an image represented by a 1D array
        mx: the x coordinate of center.
        my: the y coordinate of the center.
    '''
    x,y = coordinates(index,mx,my)
    return ((mx-x)**2 + (my-y)**2)**0.5





