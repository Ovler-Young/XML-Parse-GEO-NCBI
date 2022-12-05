import pandas as pd
import argparse
from srxparser import srx_xml_parser as sxp
import sys


def main():

    print('Starting script to get GSM and parxe XMLs...')
    df = sxp.open_df(args.df_path)
    
    list_gsm_srx_address = sxp.get_srx_adress(df, args.path_xml)
    #print(list_gsm_srx_address)
    
    list_srx_address_complete_nodup = sxp.no_dup_list_tuples(list_gsm_srx_address)
    #print(list_srx_address_complete_nodup)
    
    sxp.save_gsm_srx(list_srx_address_complete_nodup, args.out_file_name)
    
    #list_srx_address = sxp.split_srx_tuple(list_srx_address_complete_nodup)
    #print(list_srx_address)
    #sxp.save_srx_add(list_srx_address, args.out_srx_add)

if __name__ == "__main__":
    
    
    parser = argparse.ArgumentParser(
        description="A script to parse xmls from GEO-NCBI and return the GSM and SRX information as a tsv file")

    parser.add_argument('-d', '--df_path', action="store",
                        help='The absolute path to open a df with GSM column',
                        required=True)

    parser.add_argument('-p', '--path_xml', action="store",
                        help='The root path (base dir) to srx parse function. It will return a list of list for each sample for each series',
                        required=True)

    parser.add_argument('-o', '--out_file_name', action="store",
                        help='The output name file to save the output with gsm and srx address',
                        required=True)
    
    



    args = parser.parse_args()
    main()