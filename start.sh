#!/bin/bash
echo " Starting Blue Eagle Bluetooth Spammer..."
echo " WARNING: Run with root privileges!"

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Check dependencies
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing..."
    apt-get install python3 -y
fi
