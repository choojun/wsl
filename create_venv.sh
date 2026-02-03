#!/bin/bash  
# Read the user input   
echo "Enter new virtual environment (venv) name: "  
read new_env_name
echo "Enter absolute path where the venv directory should be created: "  
echo "E.g., /home/student): "  
read proj_dir
cd $proj_dir
echo "Creating new venv named $new_env_name"
python3 -m venv $new_env_name
echo "Updating $new_env_name"
$proj_dir/$new_env_name/bin/python -m pip install -U --quiet pip wheel setuptools 
echo "Installing jupyter kernel into $new_env_name"
$proj_dir/$new_env_name/bin/python -m pip install -U --quiet ipykernel
echo "Installing numpy and pyspark into $new_env_name"
$proj_dir/$new_env_name/bin/python -m pip install -U --quiet pyspark[sql]==3.5.5 numpy
echo "Installing kernel $new_env_name to Jupyter Lab"
$proj_dir/$new_env_name/bin/python -m ipykernel install --user --name $new_env_name --display-name $new_env_name
echo  "New venv $new_env_name created and installed. Please refresh your Jupyter Lab."
