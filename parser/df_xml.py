import pandas as pd
import numpy as np
import os


def open_df(file_result):

    df = pd.read_csv(file_result, sep="\t", names=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH'])
        
    return df


def drop_rename_df(df):
    
    df1 = df.copy()
    
    df_drop = df1.drop(['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O'], axis=1)
    
    #Creating new columns from commmon columns
    df_drop = df_drop.replace('None','')
    df_drop['chip_antib_catalog'] = df_drop['W'].astype(str) + df_drop['Y'].astype(str) + df_drop['Z'].astype(str)
    df_drop['Target'] = df_drop['P'].astype(str) + df_drop['Q'].astype(str) + df_drop['R'].astype(str) + df_drop['S'].astype(str) + df_drop['T'].astype(str) + df_drop['U'].astype(str) + df_drop['V'].astype(str) + df_drop['X'].astype(str)
    df_drop['Cell_line'] = df_drop['AA'].astype(str) + df_drop['CC'].astype(str)
    df_drop = df_drop.drop(['P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z', 'AA', 'CC'], axis=1)
    
    #rename columns 
    df_rename = df_drop.rename(columns = {'A':'Title', 'BB':'Cell_type', 'DD':'Organism', 'EE':'Source_cell', 'FF': 'GSE', 'GG':'GSM', 'HH':'Library_strategy'})
    df_rename = df_rename.replace('', np.NaN)
    
    
    return df_rename


def save_df(df, out_df):

    df.to_csv(os.path.join(out_df,'output_df_xml.csv'), index=False)





