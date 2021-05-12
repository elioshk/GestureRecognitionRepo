#script to open camera with or without CUDA, then perform gesture detection on a live feed.

import cv2

import time

import os

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import copy
from PIL import Image
import pyautogui
from pynput import keyboard
from pynput.keyboard import Key, Controller

keyboard = Controller()

def set_previous(thresh=2, command=0):
    for i in range(1,thresh):
        prevs[thresh-i]=prevs[thresh-1-i]
    prevs[0]=command
    
def check_previous(thresh=2, command=0): 
    # returns true if the last T are equal
    # thresh=2 is minimum for both unless you change where this check is called
    if prevs[0]==0: return False # not a gesture is never a command!
    if command != prevs[0]: return False
    for i in range(thresh-1):
        if not (prevs[i]==prevs[i+1]):
            return False
    return True

def map_gesture(arg):
    switcher = {
        0: nogesture(),
        1: down(),
        2: left(),
        3: right(),
        4: up()
    }
def nogesture():
    pass
def up():
    keyboard.press(Key.up)
    keyboard.release(Key.up)
def down():
    keyboard.press(Key.down)
    keyboard.release(Key.down)
def left():
    keyboard.press(Key.left)
    keyboard.release(Key.left)
def right():
    keyboard.press(Key.right)
    keyboard.release(Key.right)

def main():
    
    img_counter = 0
    
    while True:
        
        ret, frame = cam.read()
        
        font = cv2.FONT_HERSHEY_PLAIN
        cmdd = cmds[prevs[0]]
        # command is always set back to 0 unless 3 in a row are recognized
        if prevs[0]:
            gest = cmds[prevs[0]]
        else:
            gest = cmds[prevs[len(prevs)-1]]
        if not ret:
            print("failed to grab frame")
            break
        '''
        # uncomment for shitty live tracker.
        cv2.putText(frame,
                    'Gesture: {gest}'.format(gest=gest),
                    (50,50),
                    font, 1,
                    (255,255,0),
                    2,
                    cv2.LINE_4)
        cv2.putText(frame,
                    'Command Sent: {cmdd}'.format(cmdd=cmdd),
                    (50,70),
                    font, 1,
                    (255,255,0),
                    2,
                    cv2.LINE_4)
        '''
        
        cv2.imshow("webcam feed", frame)
        
        command = 0
        
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        else:
            img_counter += 1
            img_name = "opencv_frame_{count}.png".format(count = img_counter)
            if (img_counter % interval == 0):
                cv2.imwrite(img_name, frame)
                img_pil = Image.open(img_name)
                img = data_transforms(img_pil)
                input_batch = img.unsqueeze(0)
                input_batch = input_batch.to(device)
                output = model(input_batch)
                _, predictions = torch.max(output, 1)
                
                command = int(predictions[0])

                os.remove(img_name)
                if (check_previous(p, command)):
                    #if 3 consecutive gestures were detected in a row, send command\
                    #### SEND COMMAND HERE ####
                    ##
                    print(cmds[command], "COMMAND SENT: ",command)
                    if command == 1:
                        down()
                    elif command ==2:
                        left()
                    elif command ==3:
                        right()
                    elif command ==4:
                        up()
                    #fix "map_gesture(command)"
                    ##
                    set_previous(p)

                else:    
                    print(cmds[command])
                    set_previous(p, command)
                    
    cam.release()
    
    cv2.destroyAllWindows()
    


if __name__ == '__main__':
    
    data_transforms = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

    print("Booting Camera")
    print("'esc' to close")

    cam = cv2.VideoCapture(0)

    fps = cam.get(cv2.CAP_PROP_FPS)

    model_path = "resnext50_9324.pth"

    if torch.cuda.is_available():
        model = torch.load(model_path)
    else:
        model = torch.load(model_path, map_location='cpu')

    model.eval()

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    if torch.cuda.is_available(): print("Using CUDA gpu") 
    else: print(":(")
    cv2.namedWindow("webcam feed")

    ################################
    ## EDITABLE PARAMETERS
    interval = fps/10
    previous_detections_considered = 2
    ##
    ################################

    cmds = ["None", "Palm Flat", "Point Left", "Point Right", "Thumbs Up"]
    p = previous_detections_considered - 1
    # -1 because we compare the final detection as it occurs
    #first make array of previous detections
    prevs = []

    for i in range(p):
        prevs.append(0)
    
    
    main()
    
