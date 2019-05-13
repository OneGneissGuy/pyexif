# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:23:08 2019

@author: jsaracen
"""
from pyexif import pyexif
#from pathlib import Path
import os, fnmatch
path  = r'Photo_Processing\EXIFtool\exiftool test\Photos\Tag_test'
SR_green_images = fnmatch.filter(os.listdir(path), '*1548364654.819.550nm - Copy.tif')
"""
Slant Range naming conv
"some#.PHT#._wvl.tif"

band# 1=Blue
band# 2=GREEN
band# 3=RED
band# 4=NIR
band# 5=REDEDGE
band# 6=Thermal

"""
#SR_green_images = fnmatch.filter(os.listdir(path), '*550nm.tif')

SR_green_tags= {}
for img in SR_green_images:
    img_fname = os.path.join(path, img)   
    pyexif_img = pyexif.ExifEditor(photo=img_fname, save_backup=True)
    SR_green_tags[img] = pyexif_img.getDictTags(XMP_only=False)
    pyexif_img.clearKeywords()

#for img in SR_green_images:
#    img_fname = os.path.join(path, img)   
#    pyexif_img = pyexif.ExifEditor(photo=img_fname, save_backup=True)
#    pyexif_img.getDictTags(XMP_only=False)



altum_green_images = fnmatch.filter(os.listdir(path), 'IMG_0000_2*.tif')
#altum_green_images = fnmatch.filter(os.listdir(path), 'IMG_*_2*.tif')

"""
altum file naming conv
"IMG_PHT#_bnd.tif#"

band# 1=Blue
band# 2=GREEN
band# 3=RED
band# 4=NIR
band# 5=REDEDGE
band# 6=Thermal

"""
altum_tags= {}
for img in altum_green_images:
    img_fname = os.path.join(path, img)   
    pyexif_img = pyexif.ExifEditor(photo=img_fname, save_backup=True)
    altum_tags[img] = pyexif_img.getDictTags(XMP_only=False)


