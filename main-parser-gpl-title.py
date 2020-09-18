import argparse
from gpltitleparser import parser_xml as px
import pandas as pd



def main():
    big_list = px.parser(args.path)
    #print(big_list)
    result_list = px.filter_list(big_list)
    #print(result_list)
    px.save_file(result_list, args.out_xml)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="A script to create a dataframe from xmls files related to Chip-Seq and Homo sapiens from GEO-NCBI")

    parser.add_argument('-p', '--path', action="store",
                        help='The root path (base dir) to parse function. It will return a list of list for each sample for each series',
                        required=True)

    parser.add_argument('-o', '--out_xml', action="store",
                        help='file name containing the xml output result - from save file function',
                        required=True)


    args = parser.parse_args()
    main()