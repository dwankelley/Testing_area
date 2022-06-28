import pandas as pd
from Input.data_source_1.csv_input import input_for_csv
from Input.data_source_1.psv_input import input_for_pipe_sv
from Input.data_source_2.dat_input import input_for_dat

df1=input_for_csv('Input\data_source_1\sample_data.1.csv')
df2=input_for_pipe_sv('Input\data_source_1\sample_data.2.csv')
df3=input_for_dat('Input\data_source_2\sample_data.3.dat')

df_final=pd.concat([df1,df2,df3], ignore_index = True)

df_final.to_csv('Output\output_file.csv')
