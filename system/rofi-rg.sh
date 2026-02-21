#!/usr/bin/env bash

query=$(rofi -dmenu -i -p "rg search:")
[ -z "$query" ] && exit 0

result=$(rg --line-number --no-heading --smart-case "$query" 2>/dev/null \
    | head -n 300 \
    | rofi -dmenu -i -p "results:")
[ -z "$result" ] && exit 0

file=$(printf '%s\n' "$result" | sed 's/:.*//')
line=$(printf '%s\n' "$result" | sed 's/^[^:]*:\([^:]*\):.*/\1/')

xdg-open "$file"

