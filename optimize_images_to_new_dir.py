import os
from PIL import Image
import shutil

SOURCE_DIR = 'images'
DEST_DIR = 'images_forweb'

def optimize_images():
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Source directory '{SOURCE_DIR}' does not exist.")
        return

    # Create destination directory if it implies a fresh start, or just ensure it exists
    # If we want a clean slate, checking existence might be good, but user just said "create new folder"
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
        print(f"Created destination directory: {DEST_DIR}")

    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp', '.heic', '.mpo'}

    for root, dirs, files in os.walk(SOURCE_DIR):
        # Determine relative path to replicate structure
        rel_path = os.path.relpath(root, SOURCE_DIR)
        dest_root = os.path.join(DEST_DIR, rel_path)

        if not os.path.exists(dest_root):
            os.makedirs(dest_root)
        
        for file in files:
            file_path = os.path.join(root, file)
            file_name, file_ext = os.path.splitext(file)
            
            # Simple check if likely an image based on extension or just try opening it
            # We'll try opening everything intended to be an image, or filter by extension first
            if file_ext.lower() in image_extensions or True: # Try all files, catch errors
                try:
                    with Image.open(file_path) as img:
                        # Convert to RGB (handles RGBA, P, MPO, etc.)
                        rgb_im = img.convert('RGB')
                        
                        # New filename with .webp extension
                        new_filename = file_name + ".webp"
                        dest_path = os.path.join(dest_root, new_filename)
                        
                        rgb_im.save(dest_path, 'WEBP', quality=85)
                        print(f"Converted: {file_path} -> {dest_path}")
                except IOError:
                    # Not an image or cannot be opened
                    # simply skip
                    # print(f"Skipping non-image file: {file_path}")
                    pass
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    optimize_images()
