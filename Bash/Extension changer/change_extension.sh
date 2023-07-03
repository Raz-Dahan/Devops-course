#!/bin/bash

# first argument will be the wanted extension
EXT=$1

# second argument will be the directory
DIR=$2

# check the arguments quantity
if [[ "$#" > 2 ]]; then
  echo "input have too many arguments"
  exit 1
elif [[ "$#" < 2 ]]; then
  echo "input missing arguments"
  exit 1
elif ! test -e $DIR; then
  echo "directory in not exist"
  exit 1
fi

# if the argguments are right, it will change extantion

for file in $(find $DIR -type f)
do
  if [[ "$file" == *$EXT ]]; then
    echo "the file $file is already with $EXT extension"
  elif [[ "$file" != *$EXT ]]; then
    if [[ "$file" == *.* ]]; then 
      mv -- $file ${file%.*}.$EXT
      echo "the file $file changed extension"
    else
      mv -- $file $file.$EXT
      echo "the file $file added extension"
    fi
  fi  
done
