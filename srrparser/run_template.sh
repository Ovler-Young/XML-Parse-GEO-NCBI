#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --account=
#SBATCH --cpus-per-task=8
#SBATCH --mem=20G
#SBATCH --job-name=get-srr



module load python/3.8.0
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip

pip install --no-index -r requirements.txt
pip install retry
