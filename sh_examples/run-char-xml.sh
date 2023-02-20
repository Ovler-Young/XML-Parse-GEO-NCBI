#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --account=
#SBATCH --cpus-per-task=4
#SBATCH --mem=5G
#SBATCH --job-name=char_parse-xml



module load python/3.8.0
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip

pip install --no-index -r requirements.txt

echo 'Starting characteristics extraction...'

python check_char_fields_GEO.py /home/user/XML-files-webscrp/GEO_XML

echo 'Done! Characteristics fields saved!'
