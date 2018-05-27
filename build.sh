#!/bin/bash

jekyll build
rsync -v -rz --checksum  _site/ adulau@kb.quuxlabs.com:/home/adulau/website/hacklu2018/
