"""
Version: 1.0

Summary: pipeline of colmap and openMVS for 3D model reconstruction from images

Author: suxing liu

Author-email: suxingliu@gmail.com

USAGE:

time python3 colmap_pipeline.py -p ~/example/B101/



project folder:~/example/B101/
image folder: ~/example/B101/images


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
from pathlib import Path

def execute_script(command):
    
    try:
        print(command)
        print()
        subprocess.run(command, shell = True)
        
    except OSError:
        
        print("Failed ...!\n")

    

def colmap_vsfm_pipeline(DATASET_PATH):
    
    currentDirectory = os.getcwd()
    print(currentDirectory)
    
    if os.path.exists(DATASET_PATH):
        print("Image file path exist...\n")
    else:
        print("Image file path was not valid!\n")
        
   
    feature_extract = "colmap feature_extractor --database_path " + DATASET_PATH + "/database.db " + " --image_path " + DATASET_PATH  + "/images " + "--SiftExtraction.use_gpu=True"
    execute_script(feature_extract)
    
    feature_matching = "colmap exhaustive_matcher --database_path " + DATASET_PATH + "/database.db" + " --SiftMatching.use_gpu=True"
    execute_script(feature_matching)
    
    create_folder_sparse = "mkdir " + DATASET_PATH + "/sparse" 
    execute_script(create_folder_sparse)
    
    create_folder_sparse_0 = "mkdir " + DATASET_PATH + "/sparse/0" 
    execute_script(create_folder_sparse_0)
    
    sparse_model = "colmap mapper --database_path " + DATASET_PATH + "/database.db " + "--image_path " + DATASET_PATH  + "/images " + " --output_path " + DATASET_PATH + "/sparse" 
    execute_script(sparse_model)
    
    #reserved for future GPU version
    create_folder_dense = "mkdir " + DATASET_PATH + "/dense" 
    execute_script(create_folder_dense)
    
    #GPU required
    dense_model = "colmap image_undistorter --image_path "+ DATASET_PATH  + "/images " + " --input_path " + DATASET_PATH + "/sparse/0 --output_path " + DATASET_PATH + "/dense --output_type COLMAP --max_image_size 3600"
    execute_script(dense_model)
    
    patch_match_stereo = "colmap patch_match_stereo --workspace_path " + DATASET_PATH + "/dense" + " --workspace_format COLMAP --PatchMatchStereo.geom_consistency true"
    execute_script(patch_match_stereo)
    
    stereo_fusion = "colmap stereo_fusion --workspace_path " + DATASET_PATH + "/dense" + " --workspace_format COLMAP --input_type geometric --output_path " + DATASET_PATH + "/dense/fused.ply"
    execute_script(stereo_fusion)
    
    permission_change = "chmod 777 -R " + DATASET_PATH
    execute_script(permission_change)
    
    

if __name__ == '__main__':

    # construct the argument and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required = False, default = '/srv/images', help = "path to image file")
    args = vars(ap.parse_args())

   
    # setting path to cross section image files
    file_path = args["path"]
    
   
    colmap_vsfm_pipeline(file_path)
    
