# extractor_uv.py

import numpy as np
from netCDF4 import Dataset, num2date

def extract_and_write_uv(file_nc, lon_range, lat_range, output_file):
    """
    Extracts u10 and v10 data for a sub-region and writes to a file.
    """
    with Dataset(file_nc, 'r') as f:
        lon = f.variables['longitude'][:]
        lat = f.variables['latitude'][:]
        time = f.variables['time'][:]
        time_units = f.variables['time'].units
        
        dates = num2date(time, time_units)
        
        ilon1 = np.where(lon <= lon_range[0])[0].max()
        ilon2 = np.where(lon <= lon_range[1])[0].max()
        ilat1 = np.where(lat <= lat_range[1])[0].min()
        ilat2 = np.where(lat <= lat_range[0])[0].min()
        
        with open(output_file, 'w') as fid:
            for t, date in enumerate(dates):
                dstr = date.strftime('%Y%m%d.%H%M%S')
                fid.write(f"{dstr}\n")

                
                u10 = f.variables['u10'][t, ilat2:ilat1+1, ilon1:ilon2+1]
                v10 = f.variables['v10'][t, ilat2:ilat1+1, ilon1:ilon2+1]
                
                for i in range(u10.shape[0]):
                    fid.write(" ".join(f"{val:6.2f}" for val in u10[i]) + "\n")
                

                for i in range(v10.shape[0]):
                    fid.write(" ".join(f"{val:6.2f}" for val in v10[i]) + "\n")

