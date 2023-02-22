#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --account=
#SBATCH --cpus-per-task=48
#SBATCH --mem=250G
#SBATCH --job-name=parse-xml



module load python/3.8.0
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip

pip install --no-index -r requirements.txt

echo "Starting parsing XMLs..."

python main-parser.py -p GEO_XMLs -d GEO_xml_2023_fields.csv -c Characteristics_fields_2023-01-31.csv

echo "Dataframes saved!"
