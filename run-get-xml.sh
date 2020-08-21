#!/bin/bash
#SBATCH --time=2-00:00:00
#SBATCH --account=
#SBATCH --cpus-per-task=4
#SBATCH --mem=5G
#SBATCH --job-name=get-xml



module load python/3.8.0


python get-xml.py <list.txt> <path_to_output_directory>



