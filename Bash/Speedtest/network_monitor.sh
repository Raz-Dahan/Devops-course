#!/bin/bash

COUNT=$1
INTERVAL=$2

SUM=""

# checking the arguments

if [[ $# != 2 ]]; then
  echo "Please enter 2 argumetns: <count> <interval>"
  exit 1
else
  if (( $COUNT < 0 )) 2> /dev/null; then
    echo "Please don't give a negative <count>"
    exit 1
  elif [[ $COUNT == 0 ]]; then
    COUNT=-1
  fi
fi

if [[ $COUNT =~ [^[:digit:]] ]]; then
  echo "<count> must be numeric"
  exit 1
elif [[ $INTERVAL =~ [^[:digit:]] ]]; then
  echo "<interval> must be numeric"
  exit 1
fi
  
# trap the cntl c to stop the infinite loop (0)

trap 'echo "Test finished, check DATA.csv for results" && exit 0' SIGINT

# print (date,time,download-speed,upload-speed) to DATA.csv

echo "date,time,download,upload" > DATA.csv

while [[ $COUNT != 0 ]]
do
  DATE=$(date +%d.%m.%Y)
  TIME=$(date +%T)
  SPEEDTEST=$(speedtest --simple)
  DOWN=$(echo $SPEEDTEST | awk '{print $5}')
  UP=$(echo $SPEEDTEST | awk '{print $8}')
  SUM=($DATE,$TIME,$DOWN,$UP)
  echo "$SUM" >> DATA.csv
  ((COUNT=COUNT-1))
  sleep $INTERVAL
done

# send a message when it's done

if [[ $COUNT != -1 ]]; then
  echo "Test finished, check DATA.csv for results"
fi
