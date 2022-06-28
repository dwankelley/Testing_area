import pandas as pd

def input_for_dat(file_path):
    """converts a dat file with comma delimters to a dataframe"""
    lst=[]
    with open(file_path,'r') as dat_file:
        for line in dat_file:
            lst.append(line)
    lst2 = []
    for line in lst:
        lst2.append(line.split(','))
    for line in lst2:
        line[-1] = line[-1].replace('\n','') 
    df_dat=pd.DataFrame(lst2[1:], columns=lst2[0])
    df_dat['source']='data_source_2'
    return df_dat


