#!/usr/bin/env bash
age=$1

if [ "$age" -lt 13 ]; then
    echo "you are a kid"
elif [ "$age" -lt 20 ]; then
    echo "you are a teenager"
elif [ "$age" -lt 65 ]; then
    echo "you are an adult"
else
    echo "you are an elder"
fi
