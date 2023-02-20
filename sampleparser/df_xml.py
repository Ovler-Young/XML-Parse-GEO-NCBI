import pandas as pd
import numpy as np
import os
import sys




def save_df(df, out_df):
    """Saving df to csv file"""
    df.to_csv(out_df, index=False)


def filter_Hs_chipseq(df):
    '''This funcion receives a df 
    to filter the columns ORGANISM 
    by Homo sapiens AND Library_strategy
    by chip-seq. The duplicated rowns will
    be dropped by GSM column. It will return
    a filtered df without duplicates.'''

    df_Hs_chipseq = df[(df['Organism'].str.contains('Homo sapiens', case=False, na=False)) & (df['Library-strategy'].str.contains('chip-seq', case=False, na=False))]
    print('df_Hs_chipseq', len(df_Hs_chipseq))
    df_Hs_chipseq_no_dup = df_Hs_chipseq.drop_duplicates(subset='GSM', keep='first') #keep this - Superseries can repeat the GSM
    print('df_Hs_chipseq_no_dup',len(df_Hs_chipseq_no_dup)) 

    return df_Hs_chipseq, df_Hs_chipseq_no_dup


def create_merged_cols(df,col,list_field):
    """Receives a df, col name and list of cols
    to be concatenated by &&&. Returns the new col"""

    df[col] = df[list_field].apply(lambda row: '&&&'.join(row.dropna().values.astype(str)), axis=1) #Concatenating fields into a column (sep &&&)
    # df[col] =  df[col].str.replace(r'&{4,}', '', regex=True).astype('str') #replacing empty info -> 4 or more '&'


def drop_rename_df(df_merged, all_fields, target_fields,catalog_fields,cell_fields,disease_fields,sex_fields):
    """Receives a df and six lists containing the characteristics
    fields to be concatenated into columns.Returns a df including
    the new concatenating columns."""

    df1 = df_merged.copy()
    
    #Replacing no_field by '' to concatenate columns
    for field in all_fields:
        to_rep = 'no_'+field
        df1 = df1.replace(to_rep, np.nan) #necessary to separator &&& step using dropna

    #concatenating columns and remove the cols used for that after...
    
    create_merged_cols(df1,'Target', target_fields)
    create_merged_cols(df1,'ChIP-antibody-catalog', catalog_fields)
    create_merged_cols(df1,'Cell', cell_fields) 
    create_merged_cols(df1,'Disease', disease_fields)
    create_merged_cols(df1,'Sex_GEO', sex_fields) 

    #dropping columns from char_fields
    df1 = df1.drop(columns=all_fields) 
    print('after drop:', df1.columns)

    df1.replace('', '----', inplace=True)

    return df1
    


def merge_dfs(df_samples, df_gse, df_gpl, all_fields): #fixed dup samples -> create_df_from_listoflists
    """Receives three dfs and returns a merged df"""

    df_samples, df_gse, df_gpl = create_df_from_listoflist(df_samples, df_gse, df_gpl, all_fields)
    merged_gse = df_samples.merge(df_gse, how='left', left_on='GSE', right_on='GSE')
    print('merged_gse:', len(merged_gse))
    
    merged_gpl =  merged_gse.merge(df_gpl, how='left', left_on='GPL', right_on='GPL')
    print('merged_gpl:', len(merged_gpl))

    return merged_gpl


def create_df_from_listoflist(sample, gse, gpl, all_fields):
    """Receives three lists from xml parse
    and returns three dfs"""

    #Samples
    #columns following the xml parser order + char_field.txt
    col_fixed = ['GSE', 'GSM', 'Library-strategy','Release-date', 'GSM_title', 'Organism', 'Source', 'GPL']
    
    #generating all cols for our df
    header = col_fixed + all_fields #fixed columns + all selected fields from Characteristics block

    #samples df
    df_samples = pd.DataFrame(sample, columns = header)

    #GSE
    col_gse = ['GSE', 'GSE-title']
    df_gse = pd.DataFrame(gse, columns = col_gse)

    #GPL
    col_gpl = ['GPL', 'GPL-title']
    df_gpl = pd.DataFrame(gpl, columns = col_gpl)
    df_gpl = df_gpl.drop_duplicates(keep='first') #to avoid duplicated GSM in merged df!!! fixed!

    return df_samples, df_gse, df_gpl

