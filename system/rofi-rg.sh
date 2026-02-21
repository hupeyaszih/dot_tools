
#!/usr/bin/env bash

# 1) query al
query=$(rofi -dmenu -i -p "rg search:")
[ -z "$query" ] && exit 0

# 2) rg sonuçlarını al
result=$(rg --line-number --no-heading --smart-case "$query" 2>/dev/null \
    | head -n 300 \
    | rofi -dmenu -i -p "results:")
[ -z "$result" ] && exit 0

# 3) güvenli parse (':' bug yok)
file=$(printf '%s\n' "$result" | sed 's/:.*//')
line=$(printf '%s\n' "$result" | sed 's/^[^:]*:\([^:]*\):.*/\1/')

# 4) aç
#nvim +"$line" "$file"
xdg-open "$file"

