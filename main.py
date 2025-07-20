import ERA5
import os

# Refer to https://cds.climate.copernicus.eu/how-to-api
# Just modify on here!
variable = ['10m_u_component_of_wind', '10m_v_component_of_wind',
            'surface_net_solar_radiation', 'surface_net_thermal_radiation']
# variable = ['total_precipitation']
year_start = 1993
year_end = 2020
month_start = 1
month_end = 12
day_start = 1
day_end = 31
time_start = 0
time_end = 23
area = [90, 130, -5, 30]     # long_min, long_max, lat_min, lat_max
format_ = "netcdf"  # "netcdf" or "grib"
output_path = r"E:\Dataset_SCS\ERA5"

# Don't modify at follow!
variable_list = variable
year_list = ERA5.create_year(year_start, year_end)
month_list = ERA5.create_month(month_start, month_end)
day_list = ERA5.create_day(day_start, day_end)
time_list = ERA5.create_time(time_start, time_end)
area_list = ERA5.create_area(*area)

# file_rear
if format_ == "netcdf":
    rear = '.nc'
else:
    rear = '.grib'

# Downloaded files
downloaded_file = os.listdir(output_path)

for variable in variable_list:
    for year in year_list:
        # filename
        file_name = variable + "_" + year + rear
        print(file_name)
        file_path = os.path.join(output_path, file_name)
        # check
        if file_name in downloaded_file:
            print(file_name + " is exist!")
            continue
        # require
        era5 = ERA5.ERA5([variable], [year], month_list, day_list, time_list, area_list, format_, file_path)
        era5.require()
