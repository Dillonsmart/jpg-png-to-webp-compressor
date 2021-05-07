from PIL import Image
import PIL
import os
import glob

conversion_format = "webp" # format to convert images into
originals_dir = "originals/" # directory of the original images
converted_dir = "webp/" # directory to store new images 
compression_quality = 50 # level of compression

files = os.listdir(originals_dir)

for f in files: 
    print("Converting " + f + " into " + conversion_format + "format")
    image = Image.open(originals_dir + f).convert("RGB")
    filename = f.split(".")
    image.save(converted_dir + filename[0] + '.' + conversion_format, conversion_format, optimize = True, quality = compression_quality)