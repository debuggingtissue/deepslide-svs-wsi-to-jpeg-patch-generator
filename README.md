# deepslide-wsi-jpeg-patch-generator

Tool for splitting an image at a specific resolution from a .SVS into .JPEG tiles. 

Fork from https://github.com/BMIRDS/deepslide.

## How to run

1. [Install Openslide](https://openslide.org/download/) using your OS package manager (apt, yum, brew etc.)

1. Create a virtual environment with a Python 3.6 interpreter

        python3.6 -m venv name-of-virtual-environment

2. Activate the virtual environment

        . ./name-of-virtual-environment/bin/activate
    
3. Download the project 

4. Navigate to the project directory 
    
        cd my/path/to/deepslide-wsi-patch-generator

3. Install the dependencies using the `requirements.txt` file

        pip install -r requirements.txt


5. Navigate to the `src` directory

        cd src

6. Run the Python script
    
        python3.6 wsi_svs_to_jpeg_tiles.py  -i /path/to/svs_image_directory -o /path/to/jpeg_tiles_folder

## Description of input parameters
 
For full list and description of possible arguments run

```
python3.6 wsi_svs_to_jpeg_tiles.py -h
```
