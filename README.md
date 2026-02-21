# 🛠️ dot-tools

## 🛠️ About This Project
Everything in this repository is **handmade**. I built these tools from scratch to solve specific friction points in my daily Arch Linux workflow—from scraping dictionaries without leaving the terminal to managing C/C++ boilerplates.

![Platform](https://img.shields.io/badge/Platform-Arch_Linux-blue?logo=arch-linux)
![WM](https://img.shields.io/badge/WM-Hyprland-00a2ff?logo=hyprland)

---

## ✨ Features

### 🌍 Language & Learning
- **`dict_de`**: Scrapes Cambridge Dictionary for German-English. Provides definitions, gender info, and rich example sentences.
- **`dict_en`**: Scrapes Cambridge Dictionary for English-English. Provides definitions, example usages etc.

### 🔍 System & Search
- **`rofi-fd`**: Blazing fast file searching using `fd` integrated into Rofi.
- **`rofi-rg`**: Content search (grep) through your files using `ripgrep` with a Rofi frontend.
- **`hypr-keys`**: Automatically parses your `hyprland.conf` and displays all active keybindings in a searchable Rofi menu.

### 💻 Development
- **`cmake-init`**: A boilerplate generator for C/C++ projects to get you coding in seconds.

---
## 🚀 Installation

### 1. Prerequisites
Make sure you have the following installed on your Arch system:
```bash
sudo pacman -S rofi fd ripgrep python-requests python-beautifulsoup4
```

### 2. Setup
Clone the repository and move or link the scripts to a directory in your `$PATH` (e.g., `~/.local/bin`):

```bash
git clone https://github.com/hupeyaszih/dot_tools.git
cd dot-tools
# Example: Manual link
ln -sf $(pwd)/language/dict_de.py ~/.local/bin/dict_de
chmod +x ~/.local/bin/dict_de
```
