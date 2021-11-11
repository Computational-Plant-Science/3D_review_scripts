"""
Version: 1.0

Summary: pipeline of colmap and openMVS for 3D model reconstruction from images

Author: suxing liu

Author-email: suxingliu@gmail.com

USAGE:

time python3 VSFM.py -p ~/example/B101/


argument:
("-p", "--path", required = True,    help = "path to image file")


Note:
GPU related parameters
--SiftExtraction.use_gpu 
--SiftMatching.use_gpu

"""

import subprocess, os
import sys

import argparse
import glob
import fnmatch
import os, os.path


def execute_script(command):
    
    try:
        print(command)
        print()
        subprocess.run(command, shell = True)
        
    except OSError:
        
        print("Failed ...!\n")

    

def colmap_vsfm_pipeline(file_path):
    
    currentDirectory = os.getcwd()
    print(currentDirectory)
    
    if os.path.exists(file_path):
        print("Image file path exist...\n")
    else:
        print("Image file path was not valid!\n")

     #~/vsfm/bin/VisualSFM sfm+pmvs /media/suxingliu/Data/calibration/box_1_select/ /media/suxingliu/Data/calibration/box_1_select/output.nvm
    VSFM_pipeline = "~/vsfm/bin/VisualSFM sfm+pmvs " + file_path + " " + file_path + "/output.nvm " 
    execute_script(VSFM_pipeline)
    

 
    

if __name__ == '__main__':

    # construct the argument and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required = False, default = '/srv/images', help = "path to image file")
    args = vars(ap.parse_args())

   
    # setting path to cross section image files
    file_path = args["path"]
    
   
    colmap_vsfm_pipeline(file_path)
    
