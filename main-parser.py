import argparse
from sampleparser import sample_parser_xml as pxsample
from sampleparser import df_xml as dx
from gsetitleparser import gse_parser_xml as pxgse
from gpltitleparser import gpl_parser_xml as pxgpl
import pandas as pd


def main():

    print('Starting XML test...')
    #generating biglist for samples, gse and gpl title
    big_list = pxsample.sampleParser(args.path)
    big_list_gse = pxgse.gseParser(args.path)
    big_list_gpl = pxgpl.gplParser(args.path) 

    #filtering biglists to get the correct ones according to len_list
    sample_result = pxsample.filter_list(big_list, 38)
    gse_result = pxsample.filter_list(big_list_gse, 2)
    gpl_result = pxsample.filter_list(big_list_gpl, 2)

    df_merged = dx.merge_dfs(sample_result,gse_result,gpl_result)

    df_rename = dx.drop_rename_df(df_merged)
    df_Hs_chipseq, df_Hs_chipseq_no_dup = dx.filter_Hs_chipseq(df_rename)


    #Saving the GEO dfs
    dx.save_df(df_rename, args.out_df) #whole df without filter
    dx.save_df(df_Hs_chipseq, 'GEO_2022_filtered_Hs_ChIP.csv') #filter by Hs and ChIP
    dx.save_df(df_Hs_chipseq_no_dup, 'GEO_2022_filtered_Hs_ChIP_nodup.csv') #removing duplicates (GSM col)

    print("Dataframes saved, done!")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="A script to create a dataframe from xmls files related to Chip-Seq and Homo sapiens from GEO-NCBI")

    parser.add_argument('-p', '--path', action="store",
                        help='The root path (base dir) to parse function. It will return a list of list for each sample for each series',
                        required=True)

    parser.add_argument('-d', '--out_df', action="store",
                        help='output file with xml results',
                        required=True)


    args = parser.parse_args()
    main()