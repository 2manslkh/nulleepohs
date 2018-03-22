# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 19:18:05 2018

@author: kengh
"""
import random
import generate_label_dicts
import os, os.path
import csv
from pprint import pprint


def generate_dummy_data():
    training_dic = generate_label_dicts.get_label_dicts(["Training"],"IDs")
    num_labels = len(training_dic) - 1
    print(num_labels)
    num_childimg = 3
    
    # Number of data
    num_data = 100
    
    # Generates num_data x ([num_labels x num_childimg], label_name)
    mydata = [[[[round(random.random(),3) for x in range(num_childimg)] for i in range(num_labels)],training_dic[random.randint(0,num_labels)]] for i in range(num_data)]
    return mydata

# Generates and saves dummy data into output folder    
def generate_dummy_data_save(filename):
    save_file(generate_dummy_data(),filename)

# Saves neural network data to csv file
def save_file(mydata, filename, ext=".csv"):
    filename = filename + ext
    with open(filename, 'w') as my_csv:
        # Add Header line
        my_csv.write('Values,Label\n')  
        
        # Writes data into the csv file
        csv_writer = csv.writer(my_csv, delimiter=',',lineterminator = '\n') # lineterminator removes the added line spacing
        csv_writer.writerows(mydata)
        
        print("Saved to {}".format(filename))

# Loads the neural network data from a csv file
def load_file(file):
    print(file)
    with open(file) as csvfile:
        pass


# Returns output location of folder, default is the current directory.
def output_folder_location(location=os.getcwd()):
    return location
        
# Set output folder
output_folder = "output"

# Creates folder if such folder does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
# Set output directory below, output_folder_location() returns current directory
output_folder_location = output_folder_location()

# Counts the number of files in the specified directory
output_folder_numfiles = len([name for name in os.listdir(os.getcwd()+"/"+output_folder) if os.path.isfile(os.path.join(os.getcwd()+"/"+output_folder, name))])

# Set the output file name
file_name = "output_"

# Set file Name of csv
file_location = output_folder_location + "/" + output_folder + "/" + file_name + str(output_folder_numfiles)

# Number of file in output folder
print("Number of Files: ", output_folder_numfiles)

#generate_dummy_data_save(file_location)

myfile = "C:\\Users\kengh\GitRepos\nulleepohs\NN Utilities\output\output_16.csv"
print(load_file(myfile))


