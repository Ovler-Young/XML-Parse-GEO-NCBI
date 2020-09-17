from os import listdir,getcwd
import os.path
import sys



def print_run(samples, data_dir, template):
    
    file = open(template,'r')
    template = file.read()

    for i,sample in enumerate(samples):
        #print(sample)
        run_template = template
        output = open('run-' + str(i) + ".sh", 'w')

        sample = os.path.join(data_dir, sample)
        #print(sample)
        run_template += "\npython" + " " + os.path.join(getcwd(),"main-srr.py") + " " + \
            "-p" + " " + sample + " " + \
            "-o" + " " + "srr_" + os.path.basename(sample).split('.')[0] + ".csv"
            
        #print(run_template)
        output.write(run_template)
        output.close()

    

def main():
    data_dir = sys.argv[1]  # Data directory
    template = sys.argv[2]  # slurm template
    
    samples = listdir(data_dir)

    print_run(samples, data_dir, template)



if __name__ == "__main__":
    main()
