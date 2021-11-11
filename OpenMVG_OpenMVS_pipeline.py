"""
Version: 1.0

Summary: pipeline of colmap and openMVS for 3D model reconstruction from images

Author: suxing liu

Author-email: suxingliu@gmail.com

USAGE:

time python3 OpenMVG_OpenMVS_pipeline.py -p ~/example/B101

argument:
("-p", "--path", required = True,    help = "path to image file")

project folder:~/example/B101
image folder: ~/example/B101/images


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

    

def OpenMVG_OpenMVS_pipeline(file_path):
    
    currentDirectory = os.getcwd()
    print(currentDirectory)
    
    if os.path.exists(file_path):
        print("Image file path exist...\n")
    else:
        print("Image file path was not valid!\n")

    #docker run -v ~/example:/datasets --rm -it spedenaave/dpg
    OpenMVG_OpenMVS_pipeline = "docker run -v " + file_path + ":/datasets --rm -it spedenaave/dpg pipeline.py --input /datasets/images/ --output /datasets/openmvg --sfm-type incremental --geomodel f --run-openmvg --flength 6566 "
    
    execute_script(OpenMVG_OpenMVS_pipeline)
    


 
    

if __name__ == '__main__':

    # construct the argument and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required = True, help = "path to image file,parents path, images should be at path/images/ folder")
    args = vars(ap.parse_args())

   
    # setting path to cross section image files
    file_path = args["path"]
    
   
    OpenMVG_OpenMVS_pipeline(file_path)
    
