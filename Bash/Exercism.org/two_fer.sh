#!/bin/bash

echo "Hello, what's your name?"
read NAME
if [[ $NAME == "" ]]
  then
  NAME=you
fi

echo "Do you want on coockie?(yes/no)"
read ANSWER

if [[ $ANSWER == yes ]]
  then
  echo "One for $NAME, one for me."
else
  echo "Okay I'll give to the next person."
fi

