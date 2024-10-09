#!/bin/bash

# Check if Python 3.10 is installed
if ! command -v python3.10 &> /dev/null; then
    echo "Python 3.10 is not installed. Please install it and try again."
    exit 1
fi

# Check if python3.10-venv package is installed
if ! dpkg -s python3.10-venv &> /dev/null; then
    echo "The python3.10-venv package is not installed."
    echo "Please install it by running: sudo apt install python3.10-venv"
    exit 1
fi

cd "$(dirname "$0")/.."
python3 -m venv "venv"
source "venv/bin/activate"
pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

python -m ipykernel install --user --name=covid-19-risikoerkennung --display-name="Covid-19-Risikoerkennung"


echo "Virtual environment setup complete."
echo "To activate it, run: source venv/bin/activate"
