#!/bin/bash
echo "let's go"

sudo cp lightdm-enter-greeter.py /usr/local/bin/lightdm-enter-greeter.py
sudo cp enter/lightdm-enter-greeter.egui /usr/local/bin/enter/lightdm-enter-greeter.egui
sudo cp data/desktop/lightdm-enter-greeter.desktop /usr/share/xgreeters/lightdm-enter-greeter.desktop
sudo cp enter/bg_radgrad.png /usr/local/bin/enter/bg_radgrad.png
sudo cp enter/logo_blue_small.png /usr/local/bin/enter/logo_blue_small.png
sudo chown root: /usr/local/bin/lightdm-enter-greeter.py
sudo chown root: /usr/local/bin/enter/lightdm-enter-greeter.egui
sudo chown root: /usr/share/xgreeters/lightdm-enter-greeter.desktop
sudo chown root: /usr/local/bin/enter/bg_radgrad.png
sudo chown root: /usr/local/bin/enter/logo_blue_small.png
echo "rockn roll..."

