#!/bin/bash


get_choice() {
    read -p "Choose a number to check if it's an armstorng number: " CHOICE
    while ! [[ "$CHOICE" =~ ^[0-9]+$ ]]; do
        read -p "The number must be numeric, choose again: " CHOICE
    done
    return $CHOICE
}

is_armstrong() {
    DIGITS=()
    NUM=$1
    SUM=0
    for ((i = 0; i < ${#NUM}; i++)); do
        DIGITS+=(${NUM:$i:1})
    done
    for digit in "${DIGITS[@]}"; do
        SUM=$((SUM + digit ** ${#DIGITS[@]}))
    done
    if [[ $SUM == $NUM ]]; then
        return 0
    else
        return 1
    fi
}


main() {
    get_choice
    if is_armstrong $CHOICE; then
        echo "$CHOICE is an Armstrong number"
    else
        echo "$CHOICE is not an Armstrong number"
    fi
}

main
