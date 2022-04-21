from PIL import Image
import constants
import PIL
import os
import sys
import glob

files = os.listdir(constants.ORIGINAL_FILES_DIR)

def is_hidden(file):
    name = os.path.basename(os.path.abspath(file))
    return name.startswith('.')

def is_supported_file_type(file):

    file_name = os.path.basename(os.path.abspath(file))

    supported_types = [
        '.png',
        '.jpg',
        '.jpeg'
    ]

    if(file_name.startswith('.')):
        return False
    elif(os.path.splitext(file)[1] not in supported_types):
        return False
    else:
        return True

for f in files:
    if(is_supported_file_type(f)) :
        print("Converting " + f + " into " + constants.CONVERSION_FILETYPE + " format")
        image = Image.open(constants.ORIGINAL_FILES_DIR + f).convert("RGB")
        filename = f.split(".")
        image.save(constants.CONVERTED_FILES_DIR + filename[0] + '.' + constants.CONVERSION_FILETYPE, constants.CONVERSION_FILETYPE, optimize = True, quality = constants.CONVERSION_COMPRESSION_QUALITY)
