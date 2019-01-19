#!/bin/bash

# get JSON data from PiHole
/opt/pihole/chronometer.sh -j > /opt/inkyhole/pihole.json

# Write the data to the display
/opt/inkyhole/inkyhole.py
