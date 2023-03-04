#!/usr/bin/env bash

CPU_USAGE=$(top -b -n 1 -d1 | grep "Cpu(s)" | awk '{print $2}' | awk -F. '{print $1}')
#              command         cpu line          system usage      remove the point.

MEM_USAGE=$(free | grep Mem | awk '{print $3/$2 * 100}')
#           command memory       usage memory / total memory * 100

DISK_USAGE=$(df -P | column -t |  awk '{print $5}' | tail -n 1 | sed 's/%//g')
#            command  left format | capacity column | last line | remove percent.

echo "$CPU_USAGE, $MEM_USAGE, $DISK_USAGE" >> /opt/usage    # to transfer data into a file.



