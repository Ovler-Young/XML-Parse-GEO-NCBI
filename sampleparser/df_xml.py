import pandas as pd
import numpy as np
import os
import sys




def save_df(df, out_df):

    df.to_csv(out_df, index=False)


def filter_Hs_chipseq(df):
    '''This funcion receives a df 
    to filter the columns ORGANISM 
    by Homo sapiens AND Library_strategy
    by chip-seq. The duplicated rows will
    be dropped by GSM column. It will return
    a filtered df without duplicates.'''

    df_Hs_chipseq = df[(df['Organism'].str.contains('Homo sapiens', case=False, na=False)) & (df['Library_strategy'].str.contains('chip-seq', case=False, na=False))]
    df_Hs_chipseq_no_dup = df_Hs_chipseq.drop_duplicates(subset='GSM', keep='first') #keep this - Superseries can repeat the GSM
    
    return df_Hs_chipseq, df_Hs_chipseq_no_dup


def drop_rename_df(df_merged):
    
    df1 = df_merged.copy()
    df_drop = df1.drop(['3A', '4A', '5A', '6A', '7A', '8A', '9A', '10A', '11A','12A', '13A', '14A', '15A', '16A', '17A', '39A', '41A'], axis=1)
  
    #Creating new columns from commmon columns
    df_drop = df_drop.replace('None','')
    
    df_drop['chip_antib_catalog'] = df_drop['27A'].astype(str) + df_drop['28A'].astype(str) + df_drop['29A'].astype(str)
    df_drop['Target'] = df_drop['18A'].astype(str) + df_drop['19A'].astype(str) + df_drop['20A'].astype(str) + df_drop['21A'].astype(str) + df_drop['22A'].astype(str) + df_drop['23A'].astype(str) + df_drop['24A'].astype(str) + df_drop['25A'].astype(str) + df_drop['26A'].astype(str)
    df_drop['Cell_line'] = df_drop['30A'].astype(str) + df_drop['32A'].astype(str)
    df_drop = df_drop.drop(['18A', '19A', '20A', '21A', '22A', '23A', '24A', '25A', '26A', '27A', '28A', '29A', '30A','32A'], axis=1)
    
    #rename columns 
    df_rename = df_drop.rename(columns = {'1A':'Release-Date', '2A':'Title', '31A':'Cell_type', '33A':'Organism', '34A':'Source_cell', '35A': 'GPL', '36A': 'GSE', '37A':'GSM', '38A':'Library_strategy', '40A':'GSE_Title', '42A':'GPL_title'})
    df_rename = df_rename.replace('', np.NaN)
    
    return df_rename


def merge_dfs(df_samples, df_gse, df_gpl):
    """Receives three dfs and returns a merged df"""

    df_samples, df_gse, df_gpl = create_df_from_listoflist(df_samples, df_gse, df_gpl)
    merged_gse = df_samples.merge(df_gse, how='left', left_on='36A', right_on='39A')
    
    return merged_gse.merge(df_gpl, how='left', left_on='35A', right_on='41A')


def create_df_from_listoflist(sample, gse, gpl):
    """Receives three lists from xml parse
    and returns three dfs"""

    col = [str(x) + 'A' for x in range(1,39)]
    df_samples = pd.DataFrame(sample, columns = col)

    col_gse = ['39A', '40A']
    df_gse = pd.DataFrame(gse, columns = col_gse)

    col_gpl = ['41A', '42A']
    df_gpl = pd.DataFrame(gpl, columns = col_gpl)


    return df_samples, df_gse, df_gpl

