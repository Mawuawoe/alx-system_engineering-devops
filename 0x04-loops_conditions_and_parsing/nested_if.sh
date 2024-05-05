#!/usr/bin/env bash
temp=$1
if [ "$temp" -gt 5 ]; then
    if [ "$temp" -lt 15 ]; then
        echo "The weather is cool"
    elif [ "$temp" -lt 25 ]; then
        echo "The weather is nice"
    else
        echo "the weather is hot"
    fi
else
    echo "It is freezing outside ..."
fi