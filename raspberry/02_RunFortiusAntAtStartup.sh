#!/bin/bash 
# https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/method-2-autostart

mkdir $HOME/.config/autostart

# ----------------------------------------------------------
# Uncomment so that Raspberry will boot without HDMI monitor connected
# ----------------------------------------------------------
#cat /boot/config.txt | sed -e "s/#hdmi_force_hotplug=1/hdmi_force_hotplug=1/" >./config.txt
#sudo cp ./config.txt /boot/config.txt
#rm ./config.txt

# ----------------------------------------------------------
# add startup of FortiusAnt
# ----------------------------------------------------------
echo -e "[Desktop Entry]\nType=Application\nName=FortiusANT\nExec=/usr/bin/python3 $HOME/FortiusANT/pythoncode/FortiusAnt.py" >>$HOME/.config/autostart/FortiusANT.desktop


# ----------------------------------------------------- Done
Raspberry='\033[0;35m'
printf "${Raspberry} FortiusAnt will be started after reboot, press Enter to continue: "
read reply