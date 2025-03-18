#!/bin/bash
#SBATCH --job-name=Flex-ddG   # Job name
#SBATCH --mem=32000                     # Job memory request
#SBATCH -t 6-23:59               # Time limit days-hrs:min:sec
#SBATCH -N 1                         # requested number of nodes (usually just 1)
#SBATCH -n 1                       # requested number of CPUs
#SBATCH -p scavenger       # requested partition on which the job will run
#SBATCH --array=0-39
#SBATCH --output=./output/flex_%a.out

export PYTHONUNBUFFERED=1

python -u BlankZahFlex-DDG_constrain_arr.py $SLURM_ARRAY_TASK_ID