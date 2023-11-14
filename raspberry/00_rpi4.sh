#!/bin/bash

# ----------------------------------------------------------
# Update your system
# ----------------------------------------------------------
sudo apt update
sudo apt full-upgrade
sudo apt-get install -y python3-xyzservices python-wxtools python3-usb python3-blessed
pip install lib-programname --break-system-packages
pip install bleBless --break-system-packages
pip3 install --force-reinstall git+https://github.com/kevincar/bless.git@develop --break-system-packages

