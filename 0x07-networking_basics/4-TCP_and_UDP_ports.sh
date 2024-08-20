#!/bin/bash

echo "Active Internet connections (only servers)"
echo "Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name"

# List all listening TCP and UDP sockets with associated PID/Program
sudo netstat -tulnp | grep -E 'tcp|udp' | awk '
{
    printf "%-5s %-6s %-6s %-22s %-22s %-11s %-s\n", $1, $2, $3, $4, $5, $6, $7
}'

echo "Active UNIX domain sockets (only servers)"
echo "Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path"

# List all listening UNIX domain sockets with associated PID/Program
sudo netstat -lxp | awk '/LISTEN/ {
    printf "%-5s %-6s %-10s %-10s %-12s %-6s %-s\n", $1, $2, $3, $4, $7, $8, $9
}'

