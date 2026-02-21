import subprocess
import requests
from bs4 import BeautifulSoup

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

url = f"https://dictionary.cambridge.org/dictionary/english/{word}"
html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text
soup = BeautifulSoup(html, "html.parser")

pos = soup.select_one("span.pos")

defs = soup.select("div.def-block")  
out = f"{word}"
if pos:
    out += f" ({pos.text})"
out += "\n\n\n"

for i, def_block in enumerate(defs[:5], 1):  
    definition_tag = def_block.select_one("div.def")
    level_tag = def_block.select_one("span.def-info.ddef-info")
    
    definition = definition_tag.text.strip() if definition_tag else ""
    
    level = ""
    if level_tag:
        text = level_tag.text.strip()
        if text:
            level = text  
     
    if level:
        out += f"{i}. {definition} [{level}]\n"
    else:
        out += f"{i}. {definition}\n"
    
    examples_inline = def_block.select("span.eg.deg")
    for ex in examples_inline[:2]:  
        out += f"Example: {ex.text.strip()}\n"
    out += "\n \n"

subprocess.run(["rofi", "-e", out])
