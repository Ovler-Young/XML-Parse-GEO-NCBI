#!/bin/bash
#SBATCH --time=03:00:00
#SBATCH --account=
#SBATCH --cpus-per-task=4
#SBATCH --mem=5G
#SBATCH --job-name=srx-parse-xml



module load python/3.8.0
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip

pip install --no-index -r requirements.txt


python main-srx.py -d <path_to_metadata_dataframe_csv> -p <path_xml_directory> -o <output_name.txt>
