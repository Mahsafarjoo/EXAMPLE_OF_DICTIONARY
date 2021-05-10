# -*- coding: utf-8 -*-
"""Question4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x4hkfYFwOA4uUhGUM5RoP29H3a49yVq-

### Question 4 (20 points)

(5 pts) Write a function that calculates all your costs for the road trip. 

(5 pts) This function should take variadic keyword arguments and the keys are the cities that you visited and the values are the number of nights that you spend in each city. 

(5 pts) A user may enter a city and the number of nights that he/she will spend in those cities as much as he/she wants. If the city that the user entered is not in the file (cities.csv), do not add this city in the calculation and show a warning message.

(5 pts) Please calculate the overall cost of your trip and print it on the screen.

cities.csv file includes the cost of renting a car (per day) and hotel cost (per night) for 10 different cities. Please read the csv file and into a Pandas Data Frame. Then you can use the fields of this data frame when it is necessary.

p.s. the number of days will be counted as equal to the number of nights.

Hint. Create a dictionary whose keys consists of the cities and the values are the number of nights that a user spend. Send this dictionary as variadic keyword arguments.

Example Run:

Enter the name of the city and the number of nights that you spendBoston Portland

Enter the number of nights that you spend2 3

Total cost of your trip is 1040.0
"""

# loading the csv file
import pandas as pd
data = pd.read_csv('/content/sample_data/cities.csv')
#print(data.iloc[0, 2])

# defining the empty list, and save all of the cities inside the list_cities
list_cities = []
for i in range(len(data)):
  list_cities.append(data.iloc[i,0])
  #print(data.iloc[i,0])

# calculate the cost all cities
def calculate_the_cost(my_dictionary):

  keys = list(my_dictionary.keys())
  cost = 0

  for i in range(len(keys)):
    for j in range(len(data)):
      name_city = keys[i]
      num_of_night = my_dictionary[keys[i]]
      if data.iloc[j,0] == name_city:
        hotel = data.iloc[j,2]
        car = data.iloc[j,1]
        cost = cost + ((car + hotel) * num_of_night)
  
  return cost

mydic = { }

while True: 
  # Enter name of City
  name_of_city = input ("Enter the name of city :")

  if name_of_city in list_cities: 
    print(name_of_city)
    # Enter the number of nights that he/she will spend in that city
    num_of_nights = input("Enter the number of nights that he/she will spend in that city: ") 
    print(num_of_nights)
    # call the function that calculates all of costs
    mydic[name_of_city] = int(num_of_nights)

  elif name_of_city == "-1":
    break
  
  else:
    print("Warning! This city isn´t inside the list, Please Enter new city: ")
    continue 

calculate_the_cost(mydic)