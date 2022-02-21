import pandas as pd
import numpy as np
import os


def open_df(file_result):
    
    col  =  [ str(x) + "A" for x in range(1,39)]
    df = pd.read_csv(file_result, sep="\t", names=col)
    return df


def drop_rename_df(df):
    
    df1 = df.copy()
    df_drop = df1.drop(['3A', '4A', '5A', '6A', '7A', '8A', '9A', '10A', '11A','12A', '13A', '14A', '15A', '16A', '17A'], axis=1)

    #Creating new columns from commmon columns
    df_drop = df_drop.replace('None','')
    
    df_drop['chip_antib_catalog'] = df_drop['27A'].astype(str) + df_drop['28A'].astype(str) + df_drop['29A'].astype(str)
    df_drop['Target'] = df_drop['18A'].astype(str) + df_drop['19A'].astype(str) + df_drop['20A'].astype(str) + df_drop['21A'].astype(str) + df_drop['22A'].astype(str) + df_drop['23A'].astype(str) + df_drop['24A'].astype(str) + df_drop['25A'].astype(str) + df_drop['26A'].astype(str)
    df_drop['Cell_line'] = df_drop['30A'].astype(str) + df_drop['32A'].astype(str)
    df_drop = df_drop.drop(['18A', '19A', '20A', '21A', '22A', '23A', '24A', '25A', '26A', '27A', '28A', '29A', '30A','32A'], axis=1)
    
    #rename columns 
    df_rename = df_drop.rename(columns = {'1A':'Release-Date', '2A':'Title', '31A':'Cell_type', '33A':'Organism', '34A':'Source_cell', '35A': 'GPL', '36A': 'GSE', '37A':'GSM', '38A':'Library_strategy'})
    df_rename = df_rename.replace('', np.NaN)
    
    return df_rename


def save_df(df, out_df):

    df.to_csv(os.path.join(out_df,'output_df_xml.csv'), index=False)





