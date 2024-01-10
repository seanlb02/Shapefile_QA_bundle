import os
import geopandas as gpd
import fiona 
from threading import Timer
import shutil 
from pathlib import Path
import gc
import zipfile
import io
from fiona.io import ZipMemoryFile
import fiona
import tempfile
from fiona.io import ZipMemoryFile
import copy
from pyogrio import read_info
import shapely
from shapely import wkb
import sys
import json


def duplicate_check():
    path1 = "C:/Users/SeanGyuris/Documents/DupTest"
    rootpath = "C:/Dropbox (MCGC CLOUD)/5.0 PROJECTS/5.06 LONDON STUDIO/2023/1073LON NEOM NAT RES DMP/P5 DATA EXCHANGE/00 NEOM/QC_SHAPEFILES"
    boundary = "C:/Dropbox (MCGC CLOUD)/5.0 PROJECTS/5.06 LONDON STUDIO/2023/1073LON NEOM NAT RES DMP/P5 DATA EXCHANGE/00 NEOM/QC_SHAPEFILES/NEOM_Boundary"
    # Walk through the users QA folder and do stuff:
    for root, dirs, file in os.walk(path1):
        for name in file:  
            if name.endswith("shp"):
                        try:
                            root_name = Path(f'{root}/{name}').stem
                            layer_name = name
                            gdf = gpd.read_file(f'{root}/{name}')
                            byt = gdf.to_wkb()
                            records = gdf.shape[0] * gdf.shape[1]
                                # walk through P5:
                            for root, dirs, file in os.walk(boundary):
                                for test in file:  
                                    if test.endswith("shp"):
                                                try:
                                                    root_name = Path(f'{root}/{test}').stem
                                                    test_layer = test
                                                    gdf = gpd.read_file(f'{root}/{test}')
                                                    checkbyt = gdf.to_wkb()
                                                    test_records = gdf.shape[0] * gdf.shape[1]
                                                    if str(checkbyt.geometry.values) == str(byt.geometry.values) and records == test_records:
                                                        print(f'''
                                                         WARNING {layer_name} is a duplicate of {test_layer},
                                                        stored here: {root}/{test}
                                                        ''')
                                                       
                                                except fiona.errors.DriverError as err: 
                                                    print(err)
                        except fiona.errors.DriverError as err: 
                                                    print(err)

duplicate_check()
