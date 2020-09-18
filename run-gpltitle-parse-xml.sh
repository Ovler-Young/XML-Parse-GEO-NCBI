#!/bin/bash
#SBATCH --time=02:00:00
#SBATCH --account=
#SBATCH --cpus-per-task=4
#SBATCH --mem=5G
#SBATCH --job-name=gpl-title-parse-xml



module load python/3.8.0
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip

pip install --no-index -r requirements.txt


python main-parser-gpl-title.py -p $PATH_TO_DIR_XMLs -o xml_gpltitle_out.tsv
