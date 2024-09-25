#create env
conda create -p venv python==3.11.7

conda create -p venv python==3.11.7 --y

# activate env
conda activate venv/

# install necessary packages
pip install -r requirements.txt
