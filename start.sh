#!/bin/bash

echo './start.sh'

modprobe bcm2835-v4l2

mkdir -p /data/log/cameratrap.log

# Launch supervisor in the foreground
echo 'Starting supervisor'
supervisord --nodaemon --configuration /etc/supervisord.conf