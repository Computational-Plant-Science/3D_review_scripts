#!/bin/bash
#SBATCH --partition=bucksch_p
#SBATCH --gres=gpu:V100S:1
#SBATCH --ntasks=1
#SBATCH --mem=64GB
#SBATCH --time=08:00:00
#SBATCH --export=NONE
#SBATCH --cpus-per-task=16
#SBATCH --mail-type=FAIL,END
#SBATCH --mail-user=sl02494@uga.edu

cd $SLURM_SUBMIT_DIR

cd /scratch/sl02494/molly_root/PA762X3IIH6-5/

singularity exec --nv docker://computationalplantscience/dirt3d-reconstruction python3 /opt/code/pipeline.py -i /scratch/sl02494/molly_root/PA762X3IIH6-5/images/ -o . -g 1 -d COLMAP
