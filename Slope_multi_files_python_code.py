"""
Created on Sun May  5 18:02:07 2024

@author: Huzaifa
"""

import numpy as np
import rasterio

def zevenbergen_thorne_slope(dz_dx, dz_dy):
    slope_rad = np.arctan(np.sqrt(dz_dx**2 + dz_dy**2))
    return np.degrees(slope_rad)

def compute_slope_zt_no_edge(input_files, output_files):
    for idx, raster_file in enumerate(input_files):
        with rasterio.open(raster_file) as src:
            transform = src.transform
            data = src.read(1)

            dz_dx = (-data[:-2, :-2] - 2 * data[:-2, 1:-1] - data[:-2, 2:] +
                     data[2:, :-2] + 2 * data[2:, 1:-1] + data[2:, 2:]) / (8 * transform[0])
            dz_dy = (-data[:-2, :-2] - 2 * data[1:-1, :-2] - data[2:, :-2] +
                     data[:-2, 2:] + 2 * data[1:-1, 2:] + data[2:, 2:]) / (8 * transform[4])

            slope = zevenbergen_thorne_slope(dz_dx, dz_dy)

            profile = src.profile
            profile.update(dtype=rasterio.float32, count=1)

            output_file = output_files[idx]
            with rasterio.open(output_file, 'w', **profile) as dst:
                dst.write(slope.astype(rasterio.float32), 1)


# List of input DSM raster file paths
input_files = [r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\01_dsm1m_06-07-21.tif',
               r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\02_dsm1m_29-10-21.tif',
               r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\03_dsm1m_02-05-22.tif',
               r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\04_dsm1m_05-7-22.tif',
               r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\05_dsm1m_05-10-22.tif',
               r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\06_dsm1m_27-10-22.tif',
               r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\07_dsm1m_09-06-23.tif',
               r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\08_dsm1m_27-07-23.tif',
               r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\09_dsm1m_05-10-23.tif',
               r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\dsm_1m\10_dsm1m_23-10-23.tif']
# List of corresponding output slope raster file paths
output_files = [r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Slope_Aspect_python\01_dsm1m_06-07-21_slope.tif',
                r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Slope_Aspect_python\02_dsm1m_29-10-21_slope.tif',
                r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Slope_Aspect_python\03_dsm1m_02-05-22_slope.tif',
                r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Slope_Aspect_python\04_dsm1m_05-7-22_slope.tif',
                r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Slope_Aspect_python\05_dsm1m_05-10-22_slope.tif',
                r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Slope_Aspect_python\06_dsm1m_27-10-22_slope.tif',
                r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Slope_Aspect_python\07_dsm1m_09-06-23_slope.tif',
                r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Slope_Aspect_python\08_dsm1m_27-07-23_slope.tif',
                r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Slope_Aspect_python\09_dsm1m_05-10-23_slope.tif',
                r'D:\Polimi\Semester5\GeoinformaticsProjectAndThesis\Data\Slope_Aspect_python\10_dsm1m_23-10-23_slope.tif']

compute_slope_zt_no_edge(input_files, output_files)
