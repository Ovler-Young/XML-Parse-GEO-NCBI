import os
import tarfile
from contextlib import closing
from xml.dom import minidom
import xml.etree.ElementTree as ET
import os.path
from pathlib import Path


def flatten_dict(list_of_records):
    
    flat_list = []
    for tag in list_of_records:
        
        # in case the tag is not a dictionary
        if type(tag) is str:
            flat_list.append(tag)
            continue
            
        for k,v in tag.items():
            flat_list.append(v)
            
    return(flat_list)


def parser(base_dir):

    pathlist = Path(base_dir).glob('**/*.tgz') #get all tgz files in all subdirectories
    big_list = []
    local_list = []

    for path in pathlist:

        #gse_name = os.path.basename(path).replace('_family.xml.tgz', '') 

        with tarfile.open(path) as archive:
            for member in archive:
                if member.isreg() and member.name.endswith('.xml'): # regular xml file

                    with closing(archive.extractfile(member)) as xmlfile:
                        tree = ET.parse(xmlfile)
                        root = tree.getroot()
                        root.tag #ok

                        for plat in root.iter('{http://www.ncbi.nlm.nih.gov/geo/info/MINiML}Platform'): 

                            if len(local_list) > 0:
                                # flatten dict and append to big_list
                                big_list.append(flatten_dict(local_list))
                                local_list = []

                            for child in plat:
                         
                            #get Platform title
                                if 'Title' in child.tag:
                                    local_list.append(plat.attrib)
                                    local_list.append(child.text)

    return big_list


def filter_list(big_list):
    
    result_list = []
    wrong_list = []

    for sublist in big_list:
        if len(sublist) == 2:
            result_list.append(sublist)
            
        else:
            wrong_list.append(sublist)
    
    return result_list



def save_file(result_list, file_name):

    xml_parse = open(file_name, "w")
    for i in result_list: #our list without wrong files)
        line = "\t".join(i)
        line += "\n"
        xml_parse.write(line)

    xml_parse.close()

    print(file_name, "saved")


