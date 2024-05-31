# You are developing a program that analyzes weather data.
# Write a Python function that takes a list of temperature readings for a specific location
# and determines the average temperature, highesttemperature, and lowest temperature.
# Input: temperature_readings = [25, 28, 21, 24, 27]
# Output: Average Temperature: 25.0 Highest Temperature: 28 Lowest Temperature: 21

def temperature(temp):
    maxtemp = max(temp)
    mintemp = min(temp)
    avgtemp = sum(temp)/len(temp)
    return avgtemp, maxtemp, mintemp

temp = input("Temperature data input here with spaces: ").split()
temp = [int(x) for x in temp]
avg_temp, max_temp, min_temp = temperature(temp)
print(f"The Average Temperature: {avg_temp}, Highest Temperature: {max_temp}, Lowest Temperature: {min_temp}")
