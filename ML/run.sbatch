#!/bin/bash
#SBATCH --job-name=resnet-test
#SBATCH --account=def-sandyr
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=resnet-%j.out

# Go to your home (or project) directory
cd /home/nilsa/projects/def-sandyr/nilsa/Leetcode/ML

# Activate your existing env
source ~/env/bin/activate

# Run your script
python simple_CNN_for_MNIST.py
