#!/bin/bash
#SBATCH --nodes=1
#SBATCH --gpus-per-node=1
#SBATCH --time=12:00:00
#SBATCH --partition=single
#SBATCH --job-name=region_dashboards
#SBATCH --mem=40G

# Recommended way if you want to enable gcc version 10 for the "sbatch" session n 
source /opt/rh/devtoolset-10/enable
conda init

conda activate py312

pwd

python generate_region_dashboards.py layer-2_region-1.json
python generate_region_dashboards.py layer-2_region-2.json
python generate_region_dashboards.py layer-2_region-3.json
python generate_region_dashboards.py layer-6_region-0.json
python generate_region_dashboards.py layer-6_region-1.json
python generate_region_dashboards.py layer-6_region-2.json
python generate_region_dashboards.py layer-6_region-3.json
python generate_region_dashboards.py layer-10_region-0.json
python generate_region_dashboards.py layer-10_region-1.json