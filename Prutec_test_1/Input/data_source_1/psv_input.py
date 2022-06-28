import pandas as pd

def input_for_pipe_sv (file_path):
    """ converts a file with pipe delimters to a dataframe"""
    import pandas as pd
    df_psv = pd.read_csv('Input\data_source_1\sample_data.2.csv',sep='|')
    df_psv['source'] = 'data_source_1'
    return df_psv