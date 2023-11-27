#!/bin/bash -l
#SBATCH -A naiss2023-5-217
#SBATCH -n 18
#SBATCH -t 24:00:00
#SBATCH -J SCVI_model
#SBATCH --ntasks-per-node=18

cd /home/juany/code/Neuron_Development
conda activate scvi_old
python /home/juany/code/Neuron_Development/model_training.py