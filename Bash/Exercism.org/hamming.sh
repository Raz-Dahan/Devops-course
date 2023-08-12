#!/bin/bash

DNA1=$1
DNA2=$2

if [[ $# != 2 ]]; then
  echo "Usage: hamming.sh <string1> <string2>"
  exit 1
fi

if [[ ${#DNA1} != ${#DNA2} ]]; then
  echo "strands must be of equal length"
  exit 1
fi

DISTANCE=0
POSITION=0

ARG_LEN=${#DNA1}

ARRAY1=()
for ((i=0; i<${#DNA1}; i++)); do
    ARRAY1+=("${DNA1:i:1}")
done

ARRAY2=()
for ((i=0; i<${#DNA2}; i++)); do
    ARRAY2+=("${DNA2:i:1}")
done

while (( $POSITION != $ARG_LEN ))
do
  if [[ "${ARRAY1[$POSITION]}" != "${ARRAY2[$POSITION]}" ]]; then
    ((DISTANCE=DISTANCE+1))
    ((POSITION=POSITION+1))
  else
    ((POSITION=POSITION+1))
  fi
done

echo "$DISTANCE"
