# MapReduceFilterExercise

## Introduction
This exercise uses lambda functions with Map, Reduce and Filter to package and break large data sets into meaningful aggregations and data slices.

## Part 1: Model the Detroit Police Population
Read in the data from the Detroit Police Reports file using the CSVREADER and translate this into a list of dictionaries. Using Filter with lambda functions to exclude dictionaries (rows of the CSV) that have missing data in the Zip, or Neighborhood columns. Using lambda functions and Reduce, calculate the average total response time, the average dispatch time, and average total time for the Detroit Police force.

## Part 2: Model the Neighborhood Samples
Using lambda and Map functions, or lambda and Filter, divide the list of dictionaries into smaller lists of dictionaries separated by neighborhood. Using lambda and Reduce, find the average total response time for each neighborhood, the average dispatch time for each neighborhood, and the average total time for each neighborhood and store this into a list of dictionaries. Add a dictionary item to include the population data for all of Detroit in your combined list.

## Part 3: Create an Output JSON file
Using the JSON module, format your list of dictionaries as a JSON and test the output with the JSON lint website Write the tested JSON to a file.

## Part 4: Stretch Goal, T-test, and Excel
Read your JSON file into Excel. Utilizing the T-Test function, examine the neighborhood differences between the average total response times, the average dispatch times, and average total times. Write up a jargon-free summary of your investigation.
