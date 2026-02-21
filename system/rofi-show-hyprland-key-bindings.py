

#!/usr/bin/env python3
import subprocess
import os

options = []

config_file = os.path.expanduser("~/.config/hypr/hyprland.conf")

with open(config_file) as f:
    for line in f:
        line = line.strip()
        if line.startswith("bind"):
            parts = [p.strip() for p in line.replace("bind =", "").split(",")]
            if len(parts) >= 3:
                key_combo = "+".join(parts[:2])  
                action = parts[2]                

                if action == "exec" and len(parts) >= 4:
                    action += f" → {parts[3]}"

                options.append(f"{key_combo} → {action}")

try:
    rofi = subprocess.Popen(
        ["rofi", "-dmenu", "-p", "Hypr Bindings:"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    rofi.communicate("\n".join(options))
except KeyboardInterrupt:
    exit(0)
