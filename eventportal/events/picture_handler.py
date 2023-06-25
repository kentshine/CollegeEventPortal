import os
from pathlib import Path
from PIL import Image
from flask import url_for,current_app

def add_wallpaper(pic_upload,event_name):
    filename = pic_upload.filename
    print("File name : ", filename)
    ext_type = filename.split('.')[-1]
    storage_filename = str(event_name) + '.' + ext_type

    filepath = os.path.join(current_app.root_path,'static\event_wallpapers',storage_filename)

    output_size = (700,700)

    with Image.open(pic_upload) as pic:
        pic.thumbnail(output_size)
        pic.save(filepath)

    return storage_filename


def delete_wallpaper(event_wallpaper):
    filepath = Path(current_app.root_path,'static\event_wallpapers',event_wallpaper)
    filepath.unlink()
