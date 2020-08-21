import subprocess
import os
import sys


def create_dir(path):    
    try:
        os.mkdir(path)
        print("Directory {} done".format(path))
    except OSError:
        print("Directory {} failed".format(path))
            

def main():

    file_name = sys.argv[1] #list address
    list_name = open(file_name, 'r')
    root_path = sys.argv[2] #root path
    prefix_dir = 'GEO_'
    counter = 1                                                                  
    path = os.path.join(root_path , prefix_dir + str(counter))
    create_dir(path)

    for index, link in enumerate(list_name): 
        link = link.strip()   
        if (index + 1) % 300 == 0:  
            counter += 1
            path = os.path.join(root_path, prefix_dir + str(counter))
            create_dir(path)

        subprocess.run(['wget', link, '-P', path])
      

    
if __name__ == "__main__":

   main()





