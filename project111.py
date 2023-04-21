import os
import shutil


source="C:/Users/sai_l/OneDrive/Desktop/python/project/Document"
print("before copying")
destination="C:/Users/sai_l/OneDrive/Desktop/python/project/Image_files"
dest=shutil.move(source,destination)
print("after copying")