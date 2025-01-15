# main.py

from extractor import extract_and_write_uv

file_nc = '/home/akhedim/SWAN-Wlev/arome/wind_arome/wind_spin.nc'
output_file = '/home/akhedim/extraction/wind_output.dat'
lon_range = [2, 4]
lat_range = [37.5, 36.5]

print("** Test de la bibliothèque wind_extraction **")
extract_and_write_uv(file_nc, lon_range, lat_range, output_file)
print("** Extraction terminée avec succès **")

