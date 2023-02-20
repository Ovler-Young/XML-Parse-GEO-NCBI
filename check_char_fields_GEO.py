import os
import tarfile
from contextlib import closing
from xml.dom import minidom
import xml.etree.ElementTree as ET
import os.path
from pathlib import Path
import sys
from datetime import datetime
import pandas as pd


def characteristicsParser(base_dir):
    """Receives a path to xml files.
    Returns all fields available in 
    Characteristics block in a csv
    file, including an example (GSE)
    for each field."""

    pathlist = Path(base_dir).glob('**/*.tgz') #get all tgz files in all subdirectories
    char_dict = {}


    for path in pathlist:
        gse_name = os.path.basename(path).replace('_family.xml.tgz', '') 

        with tarfile.open(path) as archive:

            for member in archive:
                if member.isreg() and member.name.endswith('.xml'): # regular xml file

                    with closing(archive.extractfile(member)) as xmlfile:
                        tree = ET.parse(xmlfile)
                        root = tree.getroot()
                        root.tag #ok
                    
                        for sample in root.iter('{http://www.ncbi.nlm.nih.gov/geo/info/MINiML}Sample'):    

                            for child in sample:

                                if 'Channel' in child.tag:
                                    for char in child.iter():
                                        # print(char)
                                        if 'Characteristics' in char.tag:
                                            if char.attrib.get('tag') not in char_dict.keys():
                                                char_dict[char.attrib.get('tag')] = gse_name


    print('Saving df...')
    df = pd.DataFrame(char_dict.items(), columns=['Fields', 'GSE']) #to gdrive
 
    df.to_csv('Chararacteristics_fields_plus_gse.csv', index=False, sep='\t')
    

def main():

    print('Starting Characteristics script...')
    characteristicsParser(sys.argv[1]) #path xml dir containing all GEO_ subfolders
    print('Dataframe Saved!')


if __name__ == "__main__":



    main()