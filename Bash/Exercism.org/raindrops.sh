#!/bin/bash

NUM=$1

RESALUT=""

if [[ $(($NUM%3)) == 0 ]]
  then
  RESALUT+=Pling
fi

if [[ $(($NUM%5)) == 0 ]]
  then
  RESALUT+=Plang
fi

if [[ $(($NUM%7)) == 0 ]]
  then
  RESALUT+=Plong
fi 

if [[ $RESALUT != "" ]]
  then
  echo "${RESALUT}"
else
  echo "$NUM"
fi
