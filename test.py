#!/usr/bin/env python3

import time
import os.path
import pandas as pd
import numpy as np
from random import randint

def create_list_of_attributes(df):
    n=0
    list_of_attributes = []
    while df[list_of_index[0] + n][0] != '':
        list_of_attributes.append(df[list_of_index[0] + n][0])
        n += 1
    return list_of_attributes

def count_number_of_object(df, list_of_index):
    number_of_objects = 0
    for i in list_of_index:
        n = 1
        while not (df.shape[1] == n or df[i][0 + n] == ''):
            number_of_objects += 1
            n += 1
    return number_of_objects

def create_list(list_of_attributes,number_of_objects):
    exit_file = [[[] for j in range(len(list_of_attributes) + 1)] for _ in range(number_of_objects)]
    return exit_file

def fill_list(list_of_index,df,list_of_attributes):
    count = 0
    for i in list_of_index:
        n = 1
        while not (df.shape[1] == n or df[i][0 + n] == ''):
            for j in range(len(list_of_attributes) + 1):
                exit_file[count][j] = (df[i - 1 + j][0 + n])
            count += 1
            n += 1
    return exit_file

def print_something(exit_file,number_of_objects,start,stop):
    print(exit_file[randint(0,number_of_objects-1)][:])
    print(exit_file[randint(0, number_of_objects-1)][:])
    print(exit_file[randint(0, number_of_objects-1)][:])
    print("The program worked for %.3f seconds" % (stop - start))

if __name__ == "__main__":
    start = time.time()
    data_file = os.path.join('Data', 'data.xlsx')
    xls = pd.ExcelFile(io =data_file)
    df = xls.parse(xls.sheet_names[9])
    df = df.fillna('')
    df = df.values
    list_of_index =np.where(df == 'HP')[0]
    list_of_attributes = create_list_of_attributes(df)
    number_of_objects = count_number_of_object(df, list_of_index)
    exit_file = create_list(list_of_attributes,number_of_objects)
    exit_file = fill_list(list_of_index,df,list_of_attributes)
    stop = time.time()
    print_something(exit_file,number_of_objects,start,stop)







