from PIL import Image
import PIL
import os
import glob

# format to convert images into
conversion_format = ""
# directory of the original images
originals_dir = ""
# directory to store new images
converted_dir = "" 
# level of compression
compression_quality = 50

files = os.listdir(originals_dir)

for f in files: 
    print("Converting " + f + " into " + conversion_format + "format")
    image = Image.open(originals_dir + f).convert("RGB")
    filename = f.split(".")
    image.save(converted_dir + filename[0] + '.' + conversion_format, conversion_format, optimize = True, quality = compression_quality)