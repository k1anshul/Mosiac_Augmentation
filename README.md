# Mosiac_Augmentation

## Setting up the environments

step 1: Create the new python environment using following command

		conda create -n <environment_name> python=3.7

step 2: Once new environment created activate using following command

		conda activate <environment_name>

step 3: Once environment is activate using requirements.txt to install all packages using following command

		pip install -r requirements.txt
    
## How to run the main.py

Before executing main.py file set up following parameters in main.py file:
1. OUTPUT_SIZE : Provide output image height, width in tuple format. Advisable to keep image size same as input image size. In case of variable image size keep average image size.
2. SCALE_RANGE : This indiacte space occupy by each image, eg. SCALE_RANGE = (0.5, 0.5) indiactes each image occupy one quater of space. For more details check output folder.
3. NUM_IMG : This indicates total number of MOSIAC images wants to generates.
4. ANNO_DIR : Path of the folder containing txt file. Annotation must present in separate folder.
5. IMG_DIR :  Path of the folder containing images. Images also must present in separate folder.
6. OUT_DIR : Path of output folder. Mosiac augmented images and their respective txt files will saved in same output folder.
7. Print_Bbox : Its take boolen values. Keep True if you wanted to draws bounding boxes on Mosiac augmented images.

Once above paramters are setup in main.py execute main.py using following command on CLI:

    python main.py
    
After complete execution of main.py output will be gnerated in "OUT_DIR" give by you.
