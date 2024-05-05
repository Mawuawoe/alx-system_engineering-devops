#!/usr/bin/env bash
char=$1

case $char in
[a-z])
echo "small alphabet" ;;
[A-Z])
echo "Big Alphabet" ;;
[0-9])
echo "Number" ;;
*)
echo "Special character"
esac
