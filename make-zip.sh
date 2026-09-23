#!/bin/bash

## a convenience script to package your code to send to AI
## you need to install tar for this to work

rm -f *.tar.gz

tar -czf listener.tar.gz _build +run docker.compose.rpi.yml Dockerfile listener.py