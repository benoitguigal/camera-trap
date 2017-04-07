#!/bin/bash

echo './start.sh'

modprobe bcm2835-v4l2

# Launch supervisor in the foreground
echo 'Starting supervisor'
supervisord --nodaemon --configuration /etc/supervisord.conf