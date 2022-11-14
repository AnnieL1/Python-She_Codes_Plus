import csv
from datetime import datetime

# DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# def format_temperature(temp):
#     """Takes a temperature and returns it in string format with the degrees
#         and celcius symbols.

#     Args:
#         temp: A string representing a temperature.
#     Returns:
#         A string contain the temperature and "degrees celcius."
#     """
#     return f"{temp}{DEGREE_SYBMOL}"

'''
Test examples below for format_temperature:
    print(format_temperature(1))
    print(format_temperature(10))
'''


### CHALLENGE 1
# def convert_date(iso_string):
#     """Converts and ISO formatted date into a human readable format.

#     Args:
#         iso_string: An ISO date string..
#     Returns:
#         A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
#     """

#     date = datetime(int(iso_string[0:4]),int(iso_string[5:7]),int(iso_string[8:10]))
#     return date.strftime(f"%A %d %B %Y")

# #print(convert_date("2021-07-02T07:00:00+08:00"))

''' Test cases to put into 'convert_date' to see if the function works 
    1. 2021-07-02T07:00:00+08:00
    2. 2010-01-27T07:00:00+08:00
    3. 2030-12-25T07:00:00+08:00
'''

''' 
Annie's working out paper below:
    > iso_string = datetime(2001,1,1)
    > return iso_string.strftime(f"%A %d %B %Y")

#curious about: input = (input(write your year-month-day)) > if year-month-day is 2001-12-29 > the date value below will read the year-month-date and this will be the input into the function. Code for this below:
    > iso_string = input("write your date in year/month/day eg. 2001/12/29 ")
    > print(convert_date(iso_string))
# '''


### CHALLENGE 2
# def convert_f_to_c(temp_in_farenheit):
#     """Converts an temperature from farenheit to celcius.

#     Args:
#         temp_in_farenheit: float representing a temperature.
#     Returns:
#         A float representing a temperature in degrees celcius, rounded to 1dp.
#     """
#     x = (float(temp_in_farenheit) - 32) * 5/9
#     x = round(x,1)
#     return x

# #print(convert_f_to_c(90))

'''
Test cases to put into 'convert_f_to_c' to see if the function works 
    1. 90 | expected result = 32.2
    2. -10 | expected result = -23.3
    3. 64.4 | expected_result = 18
    4. "77" | expected_result = 25.0
'''


### CHALLENGE 3
# def calculate_mean(weather_data):
#     '''Calculates the mean value from a list of numbers.

#     Args:
#         weather_data: a list of numbers.
#     Returns:
#         A float representing the mean value.
#     '''

#     weather_data_str = []
#     for data in weather_data:
#         data = float(data)
#         weather_data_str.append(data)
#     print(weather_data_str)

#     total = sum(weather_data_str)
#     quantity = len(weather_data_str)
#     return total/quantity

# #print(calculate_mean([-51, -58, -59, -52, -52, -48, -47, -53]))

'''
Test cases to put into 'calculate_mean' to see if the function works 
    1. temperatures = [49, 57, 56, 55, 53] | expected_result = 54
    2. temperatures = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43] | expected_result = 52.90375
    3. temperatures = ["51", "58", "59", "52", "52", "48", "47", "53"] | expected_result = 52.5
    4. temperatures = [-51, -58, -59, -52, -52, -48, -47, -53] | expected_result = -52.5
'''

'''
Annie's working notepad 
    weather_data = [1,2,3,4]
    total = sum(weather_data)
    quantity = len(weather_data)
    mean = total/quantity
    print(total)
    print(quantity)
    print(mean)
'''


### CHALLENGE 4

# def load_data_from_csv(csv_file):

    # """Reads a csv file and stores the data in a list.

    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """

    # csv_list = []
    # final_list = []
    
    # with open(csv_file) as file:
    #     reader = csv.reader(file)
    #     next(reader)
    #     for row in reader:
    #         if not row:
    #             continue
    #         if row:
    #             max = int(row[-1])
    #             min = int(row[-2])
    #             row[-1] = max
    #             row[-2] = min
    #             csv_list.append(row)
    #     return csv_list
        
#print(load_data_from_csv('/Users/anniepersonal/Desktop/python/she-codes-python-exercises-AnnieL1/weather_project/tests/data/example_three.csv'))

    
'''
For test case example see csv files inside data!
'''

'''
Annie's notepad > first attemp of writing the code .. very long 

def load_data_from_csv(csv_file):
    
    csv_list = []
    final_list = []
    
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            # print(row) #testing to see if row prints properly 
            if not row:
                continue
            if row:
                csv_list.append(row)
        # print(csv_list)
        # return csv_list
        
    print(csv_list)
    for sublist in csv_list:
        max = int(sublist[-1])
        min = int(sublist[-2])
        sublist[-1] = max
        sublist[-2] = min 
        final_list.append(sublist)
    
    return final_list
        
# print(load_data_from_csv('/Users/anniepersonal/Desktop/python/she-codes-python-exercises-AnnieL1/weather_project/tests/data/example_three.csv'))
'''

### CHALLENGE 5 > learn enumerate 
def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    # making everything a float and to 2dp. Consolidated values in list
    temp_list = []
    for temp in weather_data:
        temp = round(float(temp),2)
        temp_list.append(temp)
    
    #finding minimum temperature
    min_temp = min(temp_list)
        # print(min_temp)
        # print(type(min_temp))
        # print('---------------')

    #finding what position the last occurence of min temp is at
    occurrences = []
    for idx, data in enumerate(temp_list):
        if data == min_temp:
            occurrences.append(idx)
    last_occurence = int(occurrences[-1])          

    return f"{min_temp}, {last_occurence}"

print(find_min([49, 57, 56, 55, 53, 49]))

'''
    Test cases to put into 'find_min(weather_data)' to see if the function works 
    1. temperatures = [49, 57, 56, 55, 53] | expected_result = (49.0, 0) #PASS
    2. temperatures = [-10, -8, 2, -16, 4] | expected_result = (-16.0, 3) #PASS
    3. temperatures = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7] | expected_result = (8.9, 3) #PASS
    4. temperatures = ["49", "57", "56", "55", "53", "49"] | expected_result = (49.0, 5) #need code to skip the first 49 ...
    5. temperatures = [] | expected_result = ()
    6. temperatures = [49, 57, 56, 55, 53, 49] | expected_result = (49.0, 5)
'''

'''
Annie's working notepad
    temp_list = [1,2,3,4,5]
    test_list = []
    for temp in temp_list:
        temp = int(temp)
        test_list.append(temp)
        print(test_list)

    #if same value in temp_list,then skip over the first one 
        # original_list_length = len(temp_list)
        # no_duplicate_list = set(temp_list)
        # print(no_duplicate_list)
        # no_duplicate_list_length = len(no_duplicate_list)
        # print(no_duplicate_list_length)
        # original_list_length - duplicate_list_length > add this value to the position of min value
'''

### CHALLENGE 6 >switch around challenge 5 
# # def find_max(weather_data):
# #     """Calculates the maximum value in a list of numbers.

# #     Args:
# #         weather_data: A list of numbers.
# #     Returns:
# #         The maximum value and it's position in the list.
# #     """
# #     pass


### CHALLENGE 7
# # def generate_summary(weather_data):
# #     """Outputs a summary for the given weather data.

# #     Args:
# #         weather_data: A list of lists, where each sublist represents a day of weather data.
# #     Returns:
# #         A string containing the summary information.
# #     """
# #     pass


### CHALLENGE 8
# # def generate_daily_summary(weather_data):
# #     """Outputs a daily summary for the given weather data.

# #     Args:
# #         weather_data: A list of lists, where each sublist represents a day of weather data.
# #     Returns:
# #         A string containing the summary information.
# #     """
# #     pass
