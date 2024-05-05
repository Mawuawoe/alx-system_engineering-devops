#!/usr/bin/env bash
if [ "$(whoami)" = 'root' ]; then
    echo "you are root"
else
    echo "you are not root"
fi
