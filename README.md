# deepslide-svs-wsi-to-jpeg-patch-generator

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
    
        cd my/path/to/deepslide-wsi-jpeg-patch-generator

3. Install the dependencies using the `requirements.txt` file

        pip install -r requirements.txt


5. Navigate to the `src` directory

        cd src

6. Run the Python script with desired arguments
    
        python3.6 wsi_svs_to_jpeg_tiles.py  -i /path/to/svs_image_directory -o /path/to/jpeg_tiles_folder
   
  Here is an example of a run
  
         python3.6 -i /home/user/debuggingtissue/svs_files -o /home/user/debuggingtissue/jpeg_tiles_folder -r 2 -op 75 -ws 800

## Description of input parameters

 * `-i INPUT_FOLDER_PATH, --input_folder_path INPUT_FOLDER_PATH`(required)
 
    * The path to the input folder.
 
 * `-o OUTPUT_FOLDER_PATH, --output_folder_path OUTPUT_FOLDER_PATH`(required)
 
    * The path to the output folder. If output folder
                        doesn't exists at runtime the script will create it.
 
 * `-s START_AT_IMAGE_NAME, --start_at_image_name START_AT_IMAGE_NAME`
 
    * Resume from a certain filename. Default value is None.
 
 * `-r {0,1,2,3}, --resolution_level {0,1,2,3}`
    *  Resolution level for image to be split. Low level
                        equals high resolution, lowest level is 0. Choose
                        between {0, 1, 2, 3}. Default value is 0.

 
 * `-op OVERLAP_PERCENTAGE, --overlap_percentage OVERLAP_PERCENTAGE`
    * Overlapping percentage between patches. Default value
                        is 0.
 * `-ws WINDOW_SIZE, --window_size WINDOW_SIZE`
    * Size for square window Default value is 10000.
 
For full list and description of possible arguments in CLI run

```
python3.6 wsi_svs_to_jpeg_tiles.py -h
```
