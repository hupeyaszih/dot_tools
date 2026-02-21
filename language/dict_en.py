import subprocess
import requests
from bs4 import BeautifulSoup

# 1. Rofi ile kullanıcıdan kelime al
p = subprocess.Popen(
    ["rofi", "-dmenu", "-p", "Enter a word:"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)
word, _ = p.communicate()
word = word.strip()

if not word:
    exit(0)

# 2. Cambridge sözlükten tanımı çek
url = f"https://dictionary.cambridge.org/dictionary/english/{word}"
html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text
soup = BeautifulSoup(html, "html.parser")

pos = soup.select_one("span.pos")

# 3. Anlamlar ve örnekler
defs = soup.select("div.def-block")  # div.def değil div.def-block daha güvenli
out = f"{word}"
if pos:
    out += f" ({pos.text})"
out += "\n\n\n"

for i, def_block in enumerate(defs[:5], 1):  # ilk 5 anlam
    definition_tag = def_block.select_one("div.def")
    level_tag = def_block.select_one("span.def-info.ddef-info")
    
    definition = definition_tag.text.strip() if definition_tag else ""
    
    # level güvenli şekilde al
    level = ""
    if level_tag:
        text = level_tag.text.strip()
        if text:
            level = text  # sadece A1/B2 kısmı
     
    # çıktı hazırlama
    if level:
        out += f"{i}. {definition} [{level}]\n"
    else:
        out += f"{i}. {definition}\n"
    
    # örnekler
    examples_inline = def_block.select("span.eg.deg")
    for ex in examples_inline[:2]:  # her anlam için 2 örnek
        out += f"Example: {ex.text.strip()}\n"
    out += "\n \n"

# 4. Rofi ile scrollable popup
subprocess.run(["rofi", "-e", out])
