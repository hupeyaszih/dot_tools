

#!/usr/bin/env python3
import subprocess
import re

# Hyprland config yolu
config_file = "~/.config/hypr/hyprland.conf"

# Bindleri tutacak liste
options = []

# Dosyayı oku
with open(config_file.replace("~", "/home/hupeyaszih")) as f:
    for line in f:
        line = line.strip()
        if line.startswith("bind"):
            parts = [p.strip() for p in line.replace("bind =", "").split(",")]
            if len(parts) >= 3:
                key_combo = "+".join(parts[:2])  # modifier + tuş
                action = parts[2]                # exec, killactive, vs

                # Eğer exec ise, çalıştırılacak komutu ekle
                if action == "exec" and len(parts) >= 4:
                    action += f" → {parts[3]}"

                options.append(f"{key_combo} → {action}")

# Rofi ile göster
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
