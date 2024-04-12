#!/bin/bash
#SBATCH --nodes=1
#SBATCH --gpus-per-node=1
#SBATCH --time=12:00:00
#SBATCH --partition=single
#SBATCH --job-name=dashboards-gpt2-e2e-6
#SBATCH --mem=40G

# Recommended way if you want to enable gcc version 10 for the "sbatch" session n 
source /opt/rh/devtoolset-10/enable
conda init

conda activate py312

conda info

pip uninstall sparsify

cd /data/jordan_tensor/sparsify

make install

gcc --version  

python --version  

pwd

python /data/jordan_tensor/sparsify/sparsify/scripts/generate_dashboards.py /data/jordan_tensor/sparsify/sparsify/scripts/dashboards.yaml /data/jordan_tensor/dashboard_runs/gpt2-e2e-lpcoeff-0.8_logits-kl-1.0_lr-0.001_ratio-60.0_blocks.6.hook_resid_pre-x40bo8o9/samples_300000.pt