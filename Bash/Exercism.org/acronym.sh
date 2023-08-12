#!/bin/bash

NAME=$1
ACRONYM=""

for word in $NAME
do
  if [[ $word =~ ^[[:alpha:]]*$ ]]; then
    FIRSTLETTER=${word:0:1}
    FIRSTLETTER=${FIRSTLETTER^}
    ACRONYM+=$FIRSTLETTER
  elif ! [[ $word =~ ^[[:alnum:]]*$ ]]; then
    FIRSTLETTER=${word:0:1}
    FIRSTLETTER=${FIRSTLETTER^}
    ACRONYM+=$FIRSTLETTER
    for letter in $word
    do
    	if ! [[ $letter =~ ^[[:alnum:]]*$ ]]; then
    	rest=${word#*$letter}
    	NEXT=$(( ${#word} - ${#rest} - ${#letter} ))
    	FIRSTLETTER=${word:$NEXT:1}
     	FIRSTLETTER=${FIRSTLETTER^}
    	ACRONYM+=$FIRSTLETTER
    	fi
    done
  fi
done

echo $ACRONYM
