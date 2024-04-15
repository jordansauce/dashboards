#!/bin/bash
#SBATCH --nodes=1
#SBATCH --gpus-per-node=1
#SBATCH --time=12:00:00
#SBATCH --partition=single
#SBATCH --job-name=dashboards-gpt2-e2e-2
#SBATCH --mem=40G

# Recommended way if you want to enable gcc version 10 for the "sbatch" session n 
source /opt/rh/devtoolset-10/enable
conda init

conda activate py312

pwd

python /data/jordan_tensor/sparsify/sparsify/scripts/generate_dashboards.py /data/jordan_tensor/sparsify/sparsify/scripts/dashboards.yaml samples_400000.pt