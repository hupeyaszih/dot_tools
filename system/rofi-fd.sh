
#!/usr/bin/env bash

DIR="${1:-$HOME}"

file=$(fd . "$DIR" \
  | rofi -dmenu -i -p "fd:")

[ -z "$file" ] && exit 0

xdg-open "$file"
