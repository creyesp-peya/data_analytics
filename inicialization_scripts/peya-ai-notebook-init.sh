#!/bin/bash
conda init
conda activate base
conda install papermill=2.2.2 -y
conda install pandas-gbq -y 
conda install python-crontab=2.5.1 -y
conda install nb_conda_kernels=2.3.1 -y

echo '{"CondaKernelSpecManager": {"kernelspec_path": "--user"}}' > $(jupyter --config-dir)/jupyter_config.json