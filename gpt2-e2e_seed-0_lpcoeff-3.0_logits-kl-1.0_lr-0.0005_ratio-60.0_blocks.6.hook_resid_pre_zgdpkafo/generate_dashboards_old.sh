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

conda info

pip uninstall sae_vis
pip uninstall sparsify

cd /data/jordan_tensor/sparsify_10-04-2024

make install

gcc --version  

python --version  

pwd

python /data/jordan_tensor/sparsify_10-04-2024/sparsify/scripts/generate_dashboards.py /data/jordan_tensor/dashboards/gpt2-e2e_seed-0_lpcoeff-3.0_logits-kl-1.0_lr-0.0005_ratio-60.0_blocks.6.hook_resid_pre_zgdpkafo/dashboards_old.yaml /data/jordan_tensor/dashboards/gpt2-e2e_seed-0_lpcoeff-3.0_logits-kl-1.0_lr-0.0005_ratio-60.0_blocks.6.hook_resid_pre_zgdpkafo/samples_400000.pt