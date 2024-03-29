import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

'''
Test cases below for format_temperature:
    print(format_temperature(1))
    print(format_temperature(10))
'''


### CHALLENGE 1
def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    date = datetime(int(iso_string[0:4]),int(iso_string[5:7]),int(iso_string[8:10]))
    return date.strftime(f"%A %d %B %Y")

#print(convert_date("2021-07-02T07:00:00+08:00"))
''' Test cases to put into 'convert_date' to see if the function works 
    1. 2021-07-02T07:00:00+08:00
    2. 2010-01-27T07:00:00+08:00
    3. 2030-12-25T07:00:00+08:00
'''


### CHALLENGE 2
def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_celcius = round((float(temp_in_farenheit) - 32) * 5/9,1)
    return temp_celcius

# print(convert_f_to_c(90))
'''
Test cases to put into 'convert_f_to_c' to see if the function works 
    1. 90 | expected result = 32.2
    2. -10 | expected result = -23.3
    3. 64.4 | expected_result = 18
    4. "77" | expected_result = 25.0
'''


### CHALLENGE 3
def calculate_mean(weather_data):
    '''Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    '''

    weather_data_as_floats = []
    for data in weather_data:
        data = float(data)
        weather_data_as_floats.append(data)

    total = sum(weather_data_as_floats)
    quantity = len(weather_data_as_floats)
    mean = total/quantity
    return mean

# print(calculate_mean([-51, -58, -59, -52, -52, -48, -47, -53]))
'''
Test cases to put into 'calculate_mean' to see if the function works 
    1. temperatures = [49, 57, 56, 55, 53] | expected_result = 54
    2. temperatures = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43] | expected_result = 52.90375
    3. temperatures = ["51", "58", "59", "52", "52", "48", "47", "53"] | expected_result = 52.5
    4. temperatures = [-51, -58, -59, -52, -52, -48, -47, -53] | expected_result = -52.5
'''


### CHALLENGE 4
def load_data_from_csv(csv_file):

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    csv_list = []
    
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if not row:
                continue
            if row:
                max = int(row[-1])
                min = int(row[-2])
                row[-1] = max
                row[-2] = min
                csv_list.append(row)
        return csv_list
        
# print(load_data_from_csv('/Users/anniepersonal/Desktop/python/she-codes-python-exercises-AnnieL1/weather_project/tests/data/example_three.csv'))
'''
For test case example see csv files inside data!
'''


### CHALLENGE 5 
def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    #making everything a float and to 2dp. Consolidated values in list
    
    if weather_data == []:
        return ()
    
    temp_list = []
    for temp in weather_data:
        temp = round(float(temp),2)
        temp_list.append(temp)
    
    min_temp = min(temp_list)

    #finding what position the last occurence of min temp is at
    occurrences = []
    for idx, data in enumerate(temp_list):
        if data == min_temp:
            occurrences.append(idx)
            last_occurence = int(occurrences[-1])        
    return min_temp,last_occurence

# print(find_min([]))
'''
    Test cases to put into 'find_min(weather_data)' to see if the function works 
    1. temperatures = [49, 57, 56, 55, 53] | expected_result = (49.0, 0) 
    2. temperatures = [-10, -8, 2, -16, 4] | expected_result = (-16.0, 3) 
    3. temperatures = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7] | expected_result = (8.9, 3) 
    4. temperatures = ["49", "57", "56", "55", "53", "49"] | expected_result = (49.0, 5)
    5. temperatures = [] | expected_result = ()
    6. temperatures = [49, 57, 56, 55, 53, 49] | expected_result = (49.0, 5)
'''


#CHALLENGE 6 
def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []:
        return ()

    temp_list = []
    for temp in weather_data:
        temp = round(float(temp),2)
        temp_list.append(temp)

    max_temp = max(temp_list)

    repeats = [] 
    for position, data in enumerate(temp_list):
        if data == max_temp:
            repeats.append(position)
        
    final_position = repeats[-1]

    return max_temp, final_position

# print(find_max([1.8789798,"2",3,5.5]))
'''
5 Day Overview
  The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
  The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
  The average low this week is 12.2°C.
  The average high this week is 17.8°C.
'''

### CHALLENGE 7
def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    # code to find x number of days for title
    day_overview = len(weather_data)
    # print(day_overview)

    # code to find lowest temperature
    low_temp = []
    for row in weather_data:
        c = convert_f_to_c(row[1])
        row[1] = c
        low_temp.append(row[1])

    # code to find lowest temp and what row it is in 
    lowest_temp_with_index = find_min(low_temp)
    lowest_temp = lowest_temp_with_index[0]
    low_position = lowest_temp_with_index[1]

    # find position of lowest temperature and obtain the date
    lowest_temp_date = weather_data[low_position][0]
    lowest_temp_date = convert_date(lowest_temp_date)

    # find average of low temperatures
    avg_low = round(calculate_mean(low_temp),1)

    # code to find highest temperature below, date of highest temp and average of highest temperatures
    high_temp = []
    for row in weather_data:
        c = convert_f_to_c(row[2])
        row[2] = c
        high_temp.append(row[2])

    # code to find highest temp and what row it is in 
    highest_temp_and_index = find_max(high_temp)
    highest_temp = highest_temp_and_index[0]
    high_position = highest_temp_and_index[1]

    # find position of highest temperature and obtain the date
    highest_temp_date = weather_data[high_position][0]
    highest_temp_date = convert_date(highest_temp_date)
    
    # find average of high temperatures
    avg_high = round(calculate_mean(high_temp),1)

    return (f'{day_overview} Day Overview\n  The lowest temperature will be {format_temperature(lowest_temp)}, and will occur on {lowest_temp_date}.\n  The highest temperature will be {format_temperature(highest_temp)}, and will occur on {highest_temp_date}.\n  The average low this week is {format_temperature(avg_low)}.\n  The average high this week is {format_temperature(avg_high)}.\n')   

# print(generate_summary([
#             ["2021-07-02T07:00:00+08:00", 49, 67],
#             ["2021-07-03T07:00:00+08:00", 57, 68],
#             ["2021-07-04T07:00:00+08:00", 56, 62],
#             ["2021-07-05T07:00:00+08:00", 55, 61],
#             ["2021-07-06T07:00:00+08:00", 53, 62]
#         ]))


### CHALLENGE 8
def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    formatted_output = ""
    for row in weather_data:
        formatted_date = convert_date(row[0])
        formatted_min_temp = format_temperature(convert_f_to_c(row[1]))
        formatted_max_temp = format_temperature(convert_f_to_c(row[2]))
        daily_summary = (f"---- {formatted_date} ----\n  Minimum Temperature: {formatted_min_temp}\n  Maximum Temperature: {formatted_max_temp}\n\n")
        formatted_output += daily_summary
    return formatted_output

print(generate_daily_summary([
            ["2021-07-02T07:00:00+08:00", 49, 67],
            ["2021-07-03T07:00:00+08:00", 57, 68],
            ["2021-07-04T07:00:00+08:00", 56, 62],
            ["2021-07-05T07:00:00+08:00", 55, 61],
            ["2021-07-06T07:00:00+08:00", 53, 62]
        ]))

'''
---- Friday 02 July 2021 ----
  Minimum Temperature: 9.4°C
  Maximum Temperature: 19.4°C

---- Saturday 03 July 2021 ----
  Minimum Temperature: 13.9°C
  Maximum Temperature: 20.0°C

---- Sunday 04 July 2021 ----
  Minimum Temperature: 13.3°C
  Maximum Temperature: 16.7°C

---- Monday 05 July 2021 ----
  Minimum Temperature: 12.8°C
  Maximum Temperature: 16.1°C

---- Tuesday 06 July 2021 ----
  Minimum Temperature: 11.7°C
  Maximum Temperature: 16.7°C
'''