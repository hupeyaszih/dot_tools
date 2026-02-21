# 🛠️ dot-tools

A collection of lightweight, terminal-centric scripts designed to supercharge the Hyprland and Arch Linux workflow. These tools prioritize speed, minimalism, and Rofi integration.

![Platform](https://img.shields.io/badge/Platform-Arch_Linux-blue?logo=arch-linux)
![WM](https://img.shields.io/badge/WM-Hyprland-00a2ff?logo=hyprland)

---

## ✨ Features

### 🌍 Language & Learning
- **`dict_de`**: Scrapes Cambridge Dictionary for German-English. Provides definitions, gender info, and rich example sentences.
- **`dict_en`**: Quick English-English dictionary scraper for definitions and usage examples.

### 🔍 System & Search
- **`rofi-fd`**: Blazing fast file searching using `fd` integrated into Rofi.
- **`rofi-rg`**: Content search (grep) through your files using `ripgrep` with a Rofi frontend.
- **`hypr-keys`**: Automatically parses your `hyprland.conf` and displays all active keybindings in a searchable Rofi menu.

### 💻 Development
- **`cmake-init`**: A boilerplate generator for C/C++ projects to get you coding in seconds.

---

### 1. Prerequisites
Make sure you have the following installed on your Arch system:
```bash
sudo pacman -S rofi fd ripgrep python-requests python-beautifulsoup4
