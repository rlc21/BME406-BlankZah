#!/bin/bash
#SBATCH --job-name=Flex-ddG   # Job name
#SBATCH --mem=80000                     # Job memory request
#SBATCH -t 6-23:59               # Time limit days-hrs:min:sec
#SBATCH -N 1                         # requested number of nodes (usually just 1)
#SBATCH -n 12                       # requested number of CPUs
#SBATCH -p scavenger       # requested partition on which the job will run
#SBATCH --output=./output/flex.out

python BlankZahFlex-DDG.py