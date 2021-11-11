#path of images: ~/example/tree

#https://github.com/rennu/dpg

docker run -v ~/example:/datasets --rm -it spedenaave/dpg

pipeline.py --input /datasets/images --output /datasets/output --sfm-type incremental --geomodel f --run-openmvg --run-openmvs

pipeline.py --input /datasets/images/ --output /datasets/output --sfm-type incremental --geomodel f --run-openmvg --flength 6566

pipeline.py --input /datasets/images/ --output /datasets/output --sfm-type incremental --geomodel f --run-openmvg --flength 6566  --run-openmvs
