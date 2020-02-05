import os
import sys
from math import ceil
from os import listdir
from os.path import isfile, join
from PIL import Image
import openslide

import argparse

compression_factor = 3
window_size = 10000
Image.MAX_IMAGE_PIXELS = 1e10


def output_jpeg_tiles(image_name, output_path):  # converts svs image with meta data into just the jpeg image

    img = openslide.OpenSlide(image_name)
    width, height = img.level_dimensions[0]
        # img_np_rgb = np.zeros((23000, 30000, 3), dtype=np.uint8)
    increment_x = int(ceil(width / window_size))
    increment_y = int(ceil(height / window_size))

    print("converting", image_name, "with width", width, "and height", height)

    for incre_x in range(increment_x):  # have to read the image in patches since it doesn't let me do it for larger things
        for incre_y in range(increment_y):

            begin_x = window_size * incre_x
            end_x = min(width, begin_x + window_size)
            begin_y = window_size * incre_y
            end_y = min(height, begin_y + window_size)
            patch_width = end_x - begin_x
            patch_height = end_y - begin_y

            patch = img.read_region((begin_x, begin_y), 0, (patch_width, patch_height))
            patch.load()
            patch_rgb = Image.new("RGB", patch.size, (255, 255, 255))
            patch_rgb.paste(patch, mask=patch.split()[3])

            # compress the image
            patch_rgb = patch_rgb.resize(
                (int(patch_rgb.size[0] / compression_factor), int(patch_rgb.size[1] / compression_factor)),
                Image.ANTIALIAS)

            # save the image
            output_subfolder = join(output_path, image_name.split('/')[-1][:-4])
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)
            output_image_name = join(output_subfolder,
                                     image_name.split('/')[-1][:-4] + '_' + str(incre_x) + '_' + str(incre_y) + '.jpg')
            # print(output_image_name)
            patch_rgb.save(output_image_name)


parser = argparse.ArgumentParser(description='Split a WSI at a specific resolution in a .SVS file into .JPEG tiles.')
parser.add_argument("--input_folder_path", type=str, help="The path to the input folder.", required=True)
parser.add_argument("--output_folder_path", type=str, help="The path to the output folder."
                                                      " If output folder doesn't exists at runtime "
                                                      "the script will create it.",
                    required=True)
parser.add_argument("--start_at_image_name", type=str, default=None, help="Resume from a certain filename."
                                                               " Default value is None.")
parser.add_argument("--resolution_level", type=int, default=0, help="Select resolution level for image to be split."
                                                         " Low level equals high resolution, lowest level is 0."
                                                         " Default value is 0.")
args = parser.parse_args()

input_folder_path = args.input_folder_path
output_folder_path = args.output_folder_path
start_at_image_name = args.start_at_image_name
resolution_level = args.resolution_level

if not os.path.exists(input_folder_path):
    sys.exit("Input folder doesn't exist")

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

image_names = [f for f in listdir(input_folder_path) if isfile(join(input_folder_path, f))]

if '.DS_Store' in image_names:
    image_names.remove('.DS_Store')

if start_at_image_name is not None:
    start = image_names.index(args.start_at)
    print("skipping the first", start)
    image_names = image_names[start + 2:]

# for image_name in image_names:
#     full_image_path = input_folder + '/' + image_name
#     output_path = output_folder + '/'
#     output_jpeg_tiles(full_image_path, output_path)
