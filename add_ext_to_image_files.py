import os
from PIL import Image


def convert_jfif_to_jpeg(filepath):
    """Converts a JFIF file to a JPEG file."""
    with Image.open(filepath) as img:
        new_filepath = os.path.splitext(filepath)[0] + '.jpg'
        img.save(new_filepath, "JPEG")
    return new_filepath


def identify_image_type(filepath):
    """Returns the image type based on the file's binary signature (magic number)."""
    
    magic_numbers = {
        b'\xff\xd8\xff': '.jpg',  # JPEG
        b'\x89PNG\r\n\x1a\n': '.png',  # PNG
        b'GIF87a': '.gif',  # GIF87a
        b'GIF89a': '.gif',  # GIF89a
        b'BM': '.bmp',  # BMP
        b'II*\x00': '.tif',  # TIFF little-endian
        b'MM\x00*': '.tif'  # TIFF big-endian
    }
    
    with open(filepath, 'rb') as f:
        file_start = f.read(8)  # read the first 8 bytes, which should be sufficient for the formats we're checking
        for magic, extension in magic_numbers.items():
            if file_start.startswith(magic):
                return extension
    return None


def rename_images_in_folder(folder):
    """Renames image files in the specified folder based on their binary signatures."""
    
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue
        
        # Check if it's a JFIF file based on filename extension
        if filename.lower().endswith('.jfif'):
            new_filepath = convert_jfif_to_jpeg(filepath)
            print(f"Converted '{filepath}' to '{new_filepath}'")
            os.remove(filepath)  # Remove the original .jfif file
            continue

        # For files without extensions, identify image type by magic number
        if '.' not in filename:        
            image_type = identify_image_type(filepath)
            if image_type:
                new_filepath = filepath + image_type
                os.rename(filepath, new_filepath)
                print(f"Renamed '{filepath}' to '{new_filepath}'")


# Example usage:
# Specify your folder path in the following line
folder_path = '/Volumes/Home/PICTURES/UNFILED'
print(f"Identifying image files in folder: {folder_path}\n")
rename_images_in_folder(folder_path)
