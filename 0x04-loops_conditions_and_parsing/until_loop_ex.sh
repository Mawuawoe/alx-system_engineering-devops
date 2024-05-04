#!/usr/bin/env bash
num=1
until [ $num -gt 10 ]; do
    echo $(($num * 3))
    num=$(($num+1))
done
