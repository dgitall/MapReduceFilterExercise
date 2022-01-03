
import csv
import json
from functools import reduce

## Part 1: Model the Detroit Police Population
# Read iin  the data from the csv
data = list()
with open("911_Calls_for_Service_(Last_30_Days).csv","r",newline='',encoding="utf-8-sig") as csvfile:
    for line in csv.DictReader(csvfile):
        data.append(line)
        
print(len(data))

# Remove the rows with missing data in zip or neighborhood
cleaner_data = filter(lambda x: False if (x['zip_code'] == '0') or (x['neighborhood'] == '') else True, data)

cleaner_data = list(cleaner_data)
print(len(cleaner_data))

# Calculate the mean of total response time, dispatch time, and total time using
# lambda functions and Reduce()
# First, convert all of the string data we will work with to float and change the empty data to 0
for i in range(0, len(cleaner_data)):
    if (cleaner_data[i]['dispatchtime'] == ''):
        cleaner_data[i]['dispatchtime'] = 0
    else:
        cleaner_data[i]['dispatchtime'] = float(cleaner_data[i]['dispatchtime'])
        
    if (cleaner_data[i]['totalresponsetime'] == ''):
        cleaner_data[i]['totalresponsetime'] = 0
    else:
        cleaner_data[i]['totalresponsetime'] = float(
        cleaner_data[i]['totalresponsetime'])
        
    if (cleaner_data[i]['totaltime'] == ''):
        cleaner_data[i]['totaltime'] = 0
    else:
        cleaner_data[i]['totaltime'] = float(cleaner_data[i]['totaltime'])

# Use reduce to get the total of each value. The form is found in https://stackoverflow.com/questions/42453091/using-reduce-on-a-list-of-dictionaries
# The x refers to the last 
totaldispatchtime = reduce(
    lambda x, y: x + y['dispatchtime'], cleaner_data, 0)
totaltotalresponsetime = reduce(
    lambda x, y: x + y['totalresponsetime'], cleaner_data, 0)
totaltotaltime = reduce(
    lambda x, y: x + y['totaltime'], cleaner_data, 0)
AvgDispatch = totaldispatchtime/len(cleaner_data)
AvgTotalResponse = totaltotalresponsetime/len(cleaner_data)
AvgTotal = totaltotaltime/len(cleaner_data)
print('Avg. Total Dispatch Time = ' + str(AvgDispatch))
print('Avg. Total Response Time = ' + str(AvgTotalResponse))
print('Avg. Total Time = ' + str(AvgTotal))

## Part 2: Model the Neighborhood Samples
# break out the data into several lists of dictionaries for each neighborhood

# get a list of the unique neighborhood names. Uses the functionality from a set
# that only adds to a set if the new value is not already there. Convert back to a
# list to get in the form we want. 
neighborhoods = set([sub['neighborhood'] for sub in cleaner_data])

# Create a new dictionary with the data sorted by neighborhood
neighborhoodData = {}
for i, nbrhood in enumerate(neighborhoods):
    nb =  list(filter(lambda x: True if x['neighborhood'] == nbrhood else False, cleaner_data))
    neighborhoodData[nbrhood] = nb

        
# Go through each neighborhood and find the averages for the times. Store these in a list of dictionaries with the first element being the
# citywide averages
AverageTimes = {}
AverageTimes['Citywide'] = {'AvgDispatch': AvgDispatch, 'AvgTotalResponse': AvgTotalResponse, 'AvgTotal': AvgTotal}
for i, nbfhood in enumerate(neighborhoods):
    nbrdata = neighborhoodData.get(nbfhood)
    totaldispatchtime = reduce(
        lambda x, y: x + y['dispatchtime'], nbrdata, 0)
    totaltotalresponsetime = reduce(
        lambda x, y: x + y['totalresponsetime'], nbrdata, 0)
    totaltotaltime = reduce(
        lambda x, y: x + y['totaltime'], nbrdata, 0)
    AvgDispatch = totaldispatchtime/len(nbrdata)
    AvgTotalResponse = totaltotalresponsetime/len(nbrdata)
    AvgTotal = totaltotaltime/len(nbrdata)
    AverageTimes[nbfhood] = {'AvgDispatch': AvgDispatch, 'AvgTotalResponse': AvgTotalResponse, 'AvgTotal': AvgTotal}

#print(AverageTimes)

## Part 3: Write to a JSON file
with open("AverageByNeighborhood.json", "w", newline='', encoding="utf-8-sig") as jsonfile:
    jsonfile.write(json.dumps(AverageTimes))

