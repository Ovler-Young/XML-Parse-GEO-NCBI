import pandas as pd
import tarfile 
import os
import xml.etree.ElementTree as ET
import os.path
from pathlib import Path
import sys


'''open a csv file as dataframe'''

def open_df(file_name):

    df = pd.read_csv(file_name)
    
    return df


'''This function extract the srx address from NCBI for each sample inserted in a dataframe. Note that the df
should be have a column GSM. It will be return a list of tuple containing GSM and their respective SRX address'''

def get_srx_adress(df, path_base_dir):
    
    df1 = df.copy()
    list_gsm = df1['GSM'].to_list()

    base_dir = path_base_dir

    list_gsm_srx_address = []
    pathlist = Path(base_dir).glob('**/*.tgz')
    count = 0

    for path in pathlist:
        t = tarfile.open(path, 'r')
        file_name =t.getnames()


        for file in file_name:
            try:
                f = t.extractfile(file)
            except KeyError:
                print('ERROR: Did not find %s in tar archive' % file)
            else:
                for line in f.readlines():
                    # convert byte-like object to str
                    try:
                        line = line.decode(encoding="ascii", errors="surrogateescape")

                        if "<Sample iid=" in line:
                            gsm = line.replace('<Sample iid="','')[:-3].strip()


                            if gsm in list_gsm:
                                count = 1
                                #print('OK')


                        if '<Relation type="SRA" target=' in line and  count == 1:

                            target  = line.split('=')
                            srx = target[2].replace('"', '') + '='+ target[3].replace("/>",'').replace('"', '').strip()
                            list_gsm_srx_address.append([gsm, srx]) #append gsm as well
                            count = 0
                    except:
                        print("Error in ", file)
                        sys.exit(1)

    return list_gsm_srx_address

def no_dup_list_tuples(list_of_tuples):


    no_dup = set(tuple(row) for row in list_of_tuples)
    list_srx_address_complete_nodup = list(no_dup)


    return list_srx_address_complete_nodup


def save_gsm_srx(list_srx, out_file_name):

    srx_gsm_address_file = open(out_file_name,"w")
    for i in list_srx:
        line = "\t".join(i)
        line += "\n"
        srx_gsm_address_file.write(line)

    srx_gsm_address_file.close()
    
    print(out_file_name, 'successful saved')


