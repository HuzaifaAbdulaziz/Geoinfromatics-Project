"""
Created on Mon May  6 00:49:34 2024

@author: Huzaifa
"""

from osgeo import gdal
import numpy as np
import os

def compute_aspect(dsm_file, output_file):
    # Open DSM raster file
    dsm_dataset = gdal.Open(dsm_file)
    
    if dsm_dataset is None:
        print("Failed to open DSM file:", dsm_file)
        return
    
    # Read DSM data
    dsm_array = dsm_dataset.ReadAsArray()
    
    # Compute aspect using numpy gradient
    dx, dy = np.gradient(dsm_array)
    aspect_rad = np.arctan2(-dy, dx)
    aspect_deg = np.degrees(aspect_rad)
    
    # Adjust aspect values to be in the range of 0 to 360 degrees
    aspect_deg[aspect_deg < 0] += 360
    
    # Create output raster file
    driver = gdal.GetDriverByName("GTiff")
    aspect_dataset = driver.Create(output_file, dsm_dataset.RasterXSize, dsm_dataset.RasterYSize, 1, gdal.GDT_Float32)
    aspect_dataset.SetGeoTransform(dsm_dataset.GetGeoTransform())
    aspect_dataset.SetProjection(dsm_dataset.GetProjection())
    aspect_band = aspect_dataset.GetRasterBand(1)
    
    # Write aspect data to raster band
    aspect_band.WriteArray(aspect_deg)
    
    # Close datasets
    aspect_band = None
    aspect_dataset = None
    dsm_dataset = None
    
    print("Aspect computation complete. Output saved as", output_file)

# List of DSM files
dsm_files = [r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\01_dsm1m_06-07-21.tif',
                   r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\02_dsm1m_29-10-21.tif',
                   r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\03_dsm1m_02-05-22.tif',
                   r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\04_dsm1m_05-7-22.tif',
                   r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\05_dsm1m_05-10-22.tif',
                   r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\06_dsm1m_27-10-22.tif',
                   r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\07_dsm1m_09-06-23.tif',
                   r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\08_dsm1m_27-07-23.tif',
                   r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\09_dsm1m_05-10-23.tif',
                   r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\10_dsm1m_23-10-23.tif']

# Output directory
output_dir = r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Slope_Aspect_python\Aspect_py'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Compute aspect for each DSM file
for dsm_file in dsm_files:
    file_name = os.path.basename(dsm_file)
    output_file = os.path.join(output_dir, file_name.replace('.tif', '_aspect.tif'))
    compute_aspect(dsm_file, output_file)
