#!/usr/bin/env python3

import os.path
import pandas as pd
import numpy as np

if __name__ == "__main__":
    data_file = os.path.join('Data', 'data.xlsx')
    xls = pd.ExcelFile(io =data_file)
    df = xls.parse(xls.sheet_names[9])
    df = df.fillna('')
    print(df.shape)
    print(df.columns[0])
    print(df.head)
    print(df.tail())

    df = df.values
    list_of_index =np.where(df == 'HP')[0]
    print(list_of_index)

    n=0
    list_of_attributes=[]
    while df[list_of_index[0]+n][0] != '':
        list_of_attributes.append(df[list_of_index[0]+n][0])
        n += 1
    print(list_of_attributes)

    #TODO count nnumber of objects

    exit_file=[]






