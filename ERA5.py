import cdsapi


def create_year(year_start_, year_end_):
    """
    The year within the limits of [1940, present]
    :param year_start_:
    :param year_end_:
    :return:
    """
    year_list_ = []
    for i in range(year_start_, year_end_ + 1):
        str_temp = "{:04d}".format(i)
        year_list_.append(str_temp)
    return year_list_


def create_month(month_start_, month_end_):
    """
    The month within the limits of [1, 12]
    :param month_start_:
    :param month_end_:
    :return:
    """
    month_list_ = []
    for i in range(month_start_, month_end_ + 1):
        str_temp = "{:02d}".format(i)
        month_list_.append(str_temp)
    return month_list_


def create_day(day_start_, day_end_):
    """
    The day within the limits of [1, 31]
    :param day_start_:
    :param day_end_:
    :return:
    """
    day_list_ = []
    for i in range(day_start_, day_end_ + 1):
        str_temp = "{:02d}".format(i)
        day_list_.append(str_temp)
    return day_list_


def create_time(time_start_, time_end_):
    """
    The time within the limits of [00:00, 23:00]
    :param time_start_:
    :param time_end_:
    :return:
    """
    time_list_ = []
    for i in range(time_start_, time_end_ + 1):
        str_temp = "{:02d}".format(i) + ":00"
        time_list_.append(str_temp)
    return time_list_


def create_area(long_min, long_max, lat_min, lat_max):
    """

    :param long_min:
    :param long_max:
    :param lat_min:
    :param lat_max:
    :return:
    """
    area_list_ = [lat_max, long_min, lat_min, long_max]
    return area_list_


class ERA5:
    def __init__(self, variable_, year_, month, day, time_, area_, format__, file_path_):
        """
        Initialize
        :param variable_:A list of variable --> str
        :param year_:A list of year --> str
        :param month:A list of month --> str
        :param day:A list of day --> str
        :param time_:A list of time --> str
        :param area_:A list of area, the rank is [lat_max, long_min, lat_min, long_max] --> int
        :param format__:Format of download file, "grib" or "netcdf" --> str
        :param file_path_:The path of output file --> str
        """
        self.variable = variable_
        self.year = year_
        self.month = month
        self.day = day
        self.time = time_
        self.area = area_
        self.format_ = format__
        self.file_path = file_path_

    def require(self):
        """
        Require to download data
        :return:
        """
        c = cdsapi.Client()

        c.retrieve(
            'reanalysis-era5-single-levels',
            {
                'product_type': 'reanalysis',
                'variable': self.variable,
                'year': self.year,
                'month': self.month,
                'day': self.day,
                'time': self.time,
                'area': self.area,
                'format': self.format_,
            },
            self.file_path)
