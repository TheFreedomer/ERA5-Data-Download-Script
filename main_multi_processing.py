import ERA5
import multiprocessing
import os
import time
from typing import List


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


def download(
        variable: str,
        year_list: List[str],
        month_list: List[str],
        day_list: List[str],
        time_list: List[str],
        area_list: List[str],
        format_: str,
        max_retries: int = 5,
        retry_delay: int = 5
) -> None:
    """
    ERA5 data download function with retry function

    Parameter:
    variable: Variable name
    year_list: List of years
    month_list: List of months
    day_list: Date list
    time_list: Time list
    area_list: Area list
    format_: Data format
    max_retries: Maximum number of retries (default: 5 times)
    retry_delay: Retry delay (seconds) (default: 5 seconds)
    """
    for year in year_list:
        # create file name
        file_name = f"{variable}_{year}{rear}"
        print(file_name)
        file_path = os.path.join(output_path, file_name)

        if file_name in downloaded_file:
            print(f"{file_name} is existed, skip!")
            continue

        retry_count = 0
        last_exception = None

        while retry_count < max_retries:
            try:
                print(f"Downloading {file_name} (Trying {retry_count + 1}/{max_retries})")

                # Init
                era5 = ERA5.ERA5(
                    [variable],
                    [year],
                    month_list,
                    day_list,
                    time_list,
                    area_list,
                    format_,
                    file_path
                )

                # execute
                era5.require()

                # Check whether the download was successful
                if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                    print(f"{file_name} download successfully")
                    downloaded_file.append(file_name)  # update the list of downloaded files
                    break
                else:
                    raise Exception("Downloaded file is empty or not created")

            except Exception as e:
                last_exception = e
                retry_count += 1
                print(f"Download failed: {str(e)}")

                if retry_count < max_retries:
                    print(f"{retry_delay} seconds later...")
                    time.sleep(retry_delay)

        # Check whether all tries were failed
        if retry_count == max_retries:
            print(f"Can not download {file_name}, already reached max number of try")
            print(f"Last error: {str(last_exception)}")
            # Record the failed task to log file
            with open("../log/download_errors.log", "a") as f:
                f.write(f"Failed: {file_name} - Error: {str(last_exception)}\n")


if __name__ == '__main__':
    processes = []
    for variable in variable_list:
        p = multiprocessing.Process(target=download,
                                    args=(variable, year_list, month_list, day_list, time_list, area_list, format_))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
