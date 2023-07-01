# with open("weather_data.csv") as file:
#     x = file.readlines()
#     data = [i.strip() for i in x ]
#
#
# print(data)
#
# import csv
#
# with open("weather_data.csv") as file:
#     data = list(csv.reader(file))
#     data = data[1:]
#     temperatures = [int(row[1]) for row in data]
#     print(temperatures)
#     # for i in data:
#     #     print(i[1])

import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
#
#
# temp_list = data["temp"].to_list()
#
# total = sum(temp_list) / len(temp_list)
# print(temp_list)

# max_value = temp_list.max()
#
# new_series = pd.Series(temp_list)
#
# max_thing = new_series.max()
#
# print(data["temp"].max())


# print(data["condition"])
# print(data.condition)


# get row

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])



# monday = data[data.day == "Monday"]
# print(monday.temp)
#
# fahrenheit = (monday.temp * 9/5) + 32
# print(fahrenheit)


# Create a dateframe from scratch
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")

print(data)