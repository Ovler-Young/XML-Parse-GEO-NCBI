import os
import tarfile
from contextlib import closing
from xml.dom import minidom
import xml.etree.ElementTree as ET
import os.path
from pathlib import Path
import sys

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

    #base_dir = sys.argv[1] #root path to xmls directory 
    pathlist = Path(base_dir).glob('**/*.tgz') #get all tgz files in all subdirectories

    big_list = []
    local_list = []

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
                            if len(local_list) > 0:
                                # flatten dict and append to big_list
                                big_list.append(flatten_dict(local_list)) #The function is called here
                                local_list = []

                            
                            for child in sample:                   
                                #get library-strategy
                                if 'Library-Strategy' in child.tag:
                                    local_list.append(gse_name)
                                    local_list.append(sample.attrib)
                                    local_list.append(child.text)

                                
                                #get title
                                if 'Title' in child.tag:
                                    local_list.append(child.text)


                                #get antibody 
                                if 'Channel' in child.tag:
                                    antib = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            antib.append(char.attrib)
                                            if char.attrib.get('tag') == 'antibody':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in antib:
                                        if 'antibody' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')
                                        
                                #get antibody-target 
                                if 'Channel' in child.tag:
                                    antib_target = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            antib_target.append(char.attrib)
                                            if char.attrib.get('tag') == 'antibody target':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in antib_target:
                                        if 'antibody target' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')
                                
                                #get chip antibody 
                                if 'Channel' in child.tag:
                                    chipantib = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            chipantib.append(char.attrib)
                                            if char.attrib.get('tag') == 'chip antibody':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in chipantib:
                                        if 'chip antibody' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')
                                
                                #get chip-antibody 
                                if 'Channel' in child.tag:
                                    chip_plus_antib = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            chip_plus_antib.append(char.attrib)
                                            if char.attrib.get('tag') == 'chip-antibody':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in chip_plus_antib:
                                        if 'chip-antibody' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')
            
                                #get chip_antibody 
                                if 'Channel' in child.tag:
                                    chip_antib = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            chip_antib.append(char.attrib)
                                            if char.attrib.get('tag') == 'chip_antibody':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in chip_antib:
                                        if 'chip_antibody' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')
                
                                #get chip_target 
                                if 'Channel' in child.tag:
                                    chip_target = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            chip_target.append(char.attrib)
                                            if char.attrib.get('tag') == 'chip_target':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in chip_target:
                                        if 'chip_target' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')
                
                                #get chip epitope 
                                if 'Channel' in child.tag:
                                    chip_epitope = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            chip_epitope.append(char.attrib)
                                            if char.attrib.get('tag') == 'chip epitope':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in chip_epitope:
                                        if 'chip epitope' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')
                
                                #get ip antibody 
                                if 'Channel' in child.tag:
                                    ip_antib = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            ip_antib.append(char.attrib)
                                            if char.attrib.get('tag') == 'ip antibody':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in ip_antib:
                                        if 'ip antibody' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')
                
    
                                #get chip antibody cat. # 
                                if 'Channel' in child.tag:
                                    chipantibcat = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            chipantibcat.append(char.attrib)
                                            if char.attrib.get('tag') == 'chip antibody cat. #':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in chipantibcat:
                                        if 'chip antibody cat. #' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')

                                #get chip_antibody_catalog 
                                if 'Channel' in child.tag:
                                    chip_antib_cat = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            chip_antib_cat.append(char.attrib)
                                            if char.attrib.get('tag') == 'chip_antibody_catalog':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in chip_antib_cat:
                                        if 'chip_antibody_catalog' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')

                                        
                                #get catalogue number 
                                if 'Channel' in child.tag:
                                    cat_number = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            cat_number.append(char.attrib)
                                            if char.attrib.get('tag') == 'catalogue number':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in cat_number:
                                        if 'catalogue number' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')       
                                        
                                        
                                        

                                #get cell line
                                if 'Channel' in child.tag:
                                    cell_line = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            cell_line.append(char.attrib)
                                            if char.attrib.get('tag') == 'cell line':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in cell_line:
                                        if 'cell line' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')
                                
                                
                                #get cell type
                                if 'Channel' in child.tag:
                                    cell_type = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            cell_type.append(char.attrib)
                                            if char.attrib.get('tag') == 'cell type':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in cell_type:
                                        if 'cell type' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')
                                
                                
                                #get line
                                if 'Channel' in child.tag:
                                    line = list()
                                    for char in child.iter():
                                        if 'Characteristics' in char.tag:                                        
                                            line.append(char.attrib)
                                            if char.attrib.get('tag') == 'line':
                                                local_list.append(char.text.strip())
                                    count = 0    
                                    for i in line:
                                        if 'line' in i.values():
                                            count  = 1
                                            break
                                    if count == 0:
                                        local_list.append('None')
                                
                            
                                #Get organism
                                if 'Channel' in child.tag:
                                    for char in child.iter():
                                        if 'Organism' in char.tag:
                                            local_list.append(char.text.strip())
                                            
                                #get source          
                                if 'Channel' in child.tag:
                                    for char in child.iter():
                                        if 'Source' in char.tag:
                                            local_list.append(char.text.strip())

    return big_list

def filter_list(big_list):
    result_list = []
    wrong_list = []

    for sublist in big_list:
        if len(sublist) == 34:
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

    


