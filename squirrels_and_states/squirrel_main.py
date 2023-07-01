#figure out how many different colors of squirrels their are


import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
column = "Primary Fur Color"

# print(data[column])

gray = data[column].value_counts()['Gray']
red = data[column].value_counts()['Cinnamon']
black = data[column].value_counts()['Black']

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray, red, black]
}

data = pd.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")

