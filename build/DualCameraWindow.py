from picamera2 import Picamera2, Preview
from time import sleep
import cv2
import numpy as np
from PyQt5 import QtWidgets
import sys
from math import *
import os
from PIL import Image, ImageTk

from assets1 import button_camOff_def_path

class DualCameraWindow:
    def __init__(self, top=None, win_width=1920, win_height=1080):
        self.button_camOff_def_img = cv2.imread(button_camOff_def_path)
        self.button_camOff_def_img =  cv2.resize(self.button_camOff_def_img, (640, 480))

        self.picam0 = Picamera2(0)
        self.picam1 = Picamera2(1)

        self.config0 = self.picam0.create_preview_configuration()
        self.config1 = self.picam1.create_preview_configuration()
        
        self.picam0.configure(self.config0)
        self.picam1.configure(self.config1)

        self.picam0.start()
        self.picam1.start()

        self.win_width = win_width
        self.win_height = win_height

        self.camera_width = ceil(self.win_width*(1)) # Given in pixels
        self.camera_height = ceil(self.win_height*(1)) # Given in pixels        

        self.grid_on = 1
        self.zoom_factor = 1
        self.cross_size = 2

        self.cam0_on = 1
        self.cam1_on = 1

        self.terminate = 0

    def set_grid_on(self, grid_on):
        self.grid_on = grid_on

    def set_zoom_factor(self, zoom_factor):
        self.zoom_factor = zoom_factor

    def set_cross_size(self, cross_size):
        self.cross_size = cross_size

    def set_cam_0_on(self, cam0_on):
        self.cam0_on = cam0_on

    def set_cam_1_on(self, cam1_on):
        self.cam1_on = cam1_on

    def set_terminate(self, terminate):
        self.terminate = terminate

    def add_cross(self, img, thick):
        h, w, _ = img.shape
        modified_img = np.zeros_like(img)
        modified_img[:] = (0, 255, 0)

        offset_x = 0
        offset_Y = 30
        modified_img[0 : h//2 - thick//2, 0 : w//2 - thick//2 - offset_x] = img[0 : h//2 - thick//2, 0 : w//2 - thick//2 - offset_x]
        modified_img[h//2 + thick//2 :, 0 : w//2 - thick//2 - offset_x] = img[h//2 + thick//2 :, 0 : w//2 - thick//2 - offset_x]
        modified_img[0 : h//2 - thick//2, w//2 + thick//2 - offset_x:] = img[0 : h//2 - thick//2, w//2 + thick//2 - offset_x:]
        modified_img[h//2 + thick//2 :, w//2 + thick//2 - offset_x :] = img[h//2 + thick//2 :, w//2 + thick//2 - offset_x :]

        return modified_img

    def zoom_image(self, img):
        h, w, _ = img.shape

        new_w, new_h = int(w*self.zoom_factor), int(h*self.zoom_factor)
        resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

        start_x = max(0, (new_w-self.camera_width//2)//2)
        start_y = max(0, (new_h-self.camera_height)//2)

        if self.zoom_factor > 1:
            zoomed_image = resized[start_y : start_y + self.camera_height, start_x : start_x + self.camera_width]
        else:
            zoomed_image = np.zeros_like(img)
            zoomed_image[
                (h - new_h)//2 : (h-new_h)//2 + new_h,
                (w - new_w)//2 : (w - new_w)//2 + new_w
            ] = resized

        return zoomed_image

    def initialize(self):
        while True:
            if self.cam0_on:
                frame0 = self.picam0.capture_array()        
                frame0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2RGB)
                #frame0 = np.array(frame0) 
                frame0 = self.zoom_image(frame0)
                if self.grid_on: frame0 = self.add_cross(frame0, self.cross_size)                
            else:
                frame0 = self.button_camOff_def_img
            cv2.namedWindow("Left Camera", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Left Camera", self.win_width//2, self.win_height-280)    
            cv2.imshow("Left Camera", frame0)
            cv2.moveWindow("Left Camera", 0, 0)

            if self.cam1_on:
                frame1 = self.picam1.capture_array()            
                frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
                frame1 = self.zoom_image(frame1)
                if self.grid_on: frame1 = self.add_cross(frame1, self.cross_size)
            else:
                frame1 = self.button_camOff_def_img
            cv2.namedWindow("Right Camera", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Right Camera", self.win_width//2, self.win_height-280)    
            cv2.imshow("Right Camera", frame1)
            cv2.moveWindow("Right Camera", self.win_width//2, 0)

            if cv2.waitKey(1) & 0xFF == ord('z'):
                self.zoom_factor += 1

            if self.terminate:
                cv2.destroyAllWindows()
                self.picam0.stop()
                self.picam1.stop()
                break