import pandas as pd

def input_for_csv(file_path):
    """ converts a file with comma delimters to a dataframe"""
    import pandas as pd
    df_csv = pd.read_csv(file_path)
    df_csv['source'] = 'data_source_1'
    return df_csv