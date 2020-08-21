import argparse
from parser import parse_xml as px
from parser import df_xml as dx
import pandas as pd


def main():
    big_list = px.parser(args.path)
    #print(big_list)
    result_list = px.filter_list(big_list)
    #print(result_list)
    px.save_file(result_list, args.out_xml)
    df = dx.open_df(args.out_xml) 
    df_rename = dx.drop_rename_df(df)
    #print(df_rename)
    dx.save_df(df_rename, args.out_df)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="A script to create a dataframe from xmls files related to Chip-Seq and Homo sapiens from GEO-NCBI")

    parser.add_argument('-p', '--path', action="store",
                        help='The root path (base dir) to parse function. It will return a list of list for each sample for each series',
                        required=True)

    parser.add_argument('-o', '--out_xml', action="store",
                        help='file name containing the xml output result - from save file function',
                        required=True)

    parser.add_argument('-d', '--out_df', action="store",
                        help='path for final output_df_xml.csv with xml results',
                        required=True)


    args = parser.parse_args()
    main()