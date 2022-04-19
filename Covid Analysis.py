'''
Author: Matthew Gathman and Aiden Chiang
Dates worked on it 1/13-1/15
Description: Enter a county in Maryland and then enter if you want to see only the cases, deaths, or both. Then you see the average cases and deaths from 
4/3/20 to 10/18/20. It is topped off with how many times more cases than deaths
Bugs: Labels merge together
Sources used:
https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.xticks.html
https://pythonspot.com/matplotlib-line-chart/
Also, the average finder from the 3.2.1
'''
#Libraries imported for cleansing data and displaying in on a graph
import matplotlib.pyplot as plt
import pandas as pd
#Reading in the 2 csv sheets
temp_data_cases = pd.read_csv("Cases.csv", header=0)   
temp_data_deaths = pd.read_csv("Deaths.csv", header = 0)
#Fucntion to Ask the user what they graph they want to see
def graph_type_pick():
    correct_answer = False  #Variable to make sure they get a correct answer
    while(correct_answer == False):
        graph_answer = input("Do you want to view cases, deaths, or both at the same time? Please type 'Cases', 'Deaths', or 'Both'. ")
        if(graph_answer == 'Cases' or graph_answer == 'Deaths' or graph_answer == 'Both'):
            correct_answer = True
        if(graph_answer == 'Cases'):
            graph_show_cases(pick_county)   #Sends the user to the case graph function
        elif(graph_answer == 'Deaths'):
            graph_show_deaths(pick_county)  #Sends the user to the Deaths graph function
        elif(graph_answer == 'Both'):
            graph_show_both(pick_county)    #Sends the user to the graph function with both deaths and cases
#Function that asks the user what county they want to see from
def county_pick():
    global pick_county 
    pick_county = input("What country do you want to view out of all the counties in Maryland? Your options are Allegany,"
    "Anne_Arundel, Baltimore, Baltimore_City, Calvert, Caroline, Carroll, Cecil, Charles, Dorchester, Frederick, Garrett, \n"
    "Harford, Howard, Kent, Montgomery, Prince_Georges, Queen_Annes, Somerset, St_Marys, Talbot, Washington, Wicomico, and Worcester.")
#Function that shows the user the graph with both Cases and Deaths
def graph_show_both(County):
    #Plotting cases and deaths
    plt.plot(temp_data_cases['DATE'], temp_data_cases[pick_county], color='blue')
    plt.plot(temp_data_cases['DATE'], temp_data_deaths[pick_county], color='red')
    #Labelling the Axes
    plt.ylabel('Cases')
    plt.xlabel('Dates')
    plt.title(County)
    plt.xticks(rotation=90, ha='right')
    plt.show()
#Function that shows the user the graph with Deaths
def graph_show_deaths(County):
    #Plotting deaths
    plt.plot(temp_data_cases['DATE'], temp_data_deaths[pick_county], color='red')
    #Labelling the Axes
    plt.ylabel('Cases')
    plt.xlabel('Dates')
    plt.title(County)
    plt.xticks(rotation=90, ha='right')
    plt.show()
#Function that shows the user the graph with Cases
def graph_show_cases(county):
    #Plotting cases
    plt.plot(temp_data_cases['DATE'], temp_data_cases[county], color='blue')
    #Labelling the Axes
    plt.ylabel('Cases')
    plt.xlabel('Dates')
    plt.title(county)
    plt.xticks(rotation=90, ha='right')
    plt.show()
#Function that creates the minimum, maximum, and average cases through 4/3/20 to 10/18/20
def average_cases(pick_county):
    global avg_cases
    #Creating the variables to create the minimum, maximum, and average
    min_cases = temp_data_cases[pick_county][0] #List to cycle through for minimum cases
    max_cases = temp_data_cases[pick_county][0] #List to cycle through for max cases
    min_year = temp_data_cases['DATE'][0]  #List to cycle through for max date
    max_year = temp_data_cases['DATE'][0]  #List to cycle through for max date
    sum_cases = 0
    avg_cases = 0
    #Looping through all the data points and saving those that are the biggest and smallest
    for i in range(0, len(temp_data_cases[pick_county])):
        #Min Cases
        if (temp_data_cases[pick_county][i] < min_cases):
            min_cases = temp_data_cases[pick_county][i]
            min_year = temp_data_cases['DATE'][i]
        #Max Cases
        if (temp_data_cases[pick_county][i] > max_cases):
            max_cases = temp_data_cases[pick_county][i]
            max_year = temp_data_cases['DATE'][i]
        #Creating sum for calculating average
        sum_cases = sum_cases + temp_data_cases[pick_county][i]
        #Creating Average
        avg_cases = sum_cases/len(temp_data_cases[pick_county])
    print("The maximum cases is:", max_cases, "which occured in", max_year)
    print("The minimum cases is:", min_cases, "which occured in", min_year)
    print("The average cases is:", avg_cases)
#Function that creates the minimum, maximum, and average deaths through 4/3/20 to 10/18/20
def average_deaths(pick_county):
    global avg_deaths
    #Creating the variables to create the minimum, maximum, and average   
    min_deaths = temp_data_deaths[pick_county][0] #List to cycle through for minimum deaths
    max_deaths = temp_data_deaths[pick_county][0] #List to cycle through for max deaths
    min_date = temp_data_deaths['DATE'][0]  #List to cycle through for max date
    max_date = temp_data_deaths['DATE'][0]  #List to cycle through for max date
    sum_deaths = 0
    avg_deaths = 0
    #Looping through all the data points and saving those that are the biggest and smallest
    for i in range(0, len(temp_data_deaths[pick_county])):
        #Min Deaths
        if (temp_data_deaths[pick_county][i] < min_deaths):
            min_deaths = temp_data_deaths[pick_county][i]
            min_date = temp_data_deaths['DATE'][i]
        #Max Deaths
        if (temp_data_deaths[pick_county][i] > max_deaths):
            max_deaths = temp_data_deaths[pick_county][i]
            max_date = temp_data_deaths['DATE'][i]
        #Creating sum for calculating average
        sum_deaths = sum_deaths + temp_data_deaths[pick_county][i]
        #Creating Average
        avg_deaths = sum_deaths/len(temp_data_deaths[pick_county])
    print("The maximum deaths is:", max_deaths, "which occured in", max_date)
    print("The minimum deaths is:", min_deaths, "which occured in", min_date)
    print("The average deaths is:", avg_deaths, " in ", pick_county, " County.")

#Function calls
county_pick()
graph_type_pick()
average_cases(pick_county)
average_deaths(pick_county)
#Getting the cases to deaths number. I felt it didn't need it's own function
cases_deaths_ratio = avg_cases/avg_deaths
print("There are", cases_deaths_ratio, "times more cases than deaths in", pick_county, " County.")

